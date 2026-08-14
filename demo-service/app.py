import json
import logging
import os
import time
from datetime import datetime, timezone

from flask import Flask, jsonify, request
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from prometheus_client import Counter, Histogram, start_http_server

SERVICE_NAME = os.getenv("SERVICE_NAME", "demo-service")
OTLP_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "http://otel-collector:4318/v1/traces")

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(SERVICE_NAME)

provider = TracerProvider(resource=Resource.create({"service.name": SERVICE_NAME}))
provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=OTLP_ENDPOINT)))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

REQUESTS = Counter("demo_service_requests_total", "Requests received by route and status", ["route", "status"])
LATENCY = Histogram("demo_service_request_duration_seconds", "Request latency", ["route"])

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)


@app.get("/healthz")
def healthz():
    return jsonify(status="ok", service=SERVICE_NAME)


@app.get("/")
def index():
    started = time.perf_counter()
    request_id = request.headers.get("x-request-id", "demo-request")
    with tracer.start_as_current_span("demo-work") as span:
        span.set_attribute("demo.request_id", request_id)
        span.set_attribute("demo.endpoint", "/")
        time.sleep(0.03)
    elapsed = time.perf_counter() - started
    LATENCY.labels(route="/").observe(elapsed)
    REQUESTS.labels(route="/", status="200").inc()
    logger.info(json.dumps({"event": "request_completed", "request_id": request_id, "latency_ms": round(elapsed * 1000, 2), "timestamp": datetime.now(timezone.utc).isoformat()}))
    return jsonify(service=SERVICE_NAME, requestId=request_id, message="telemetry emitted")


if __name__ == "__main__":
    start_http_server(9464)
    app.run(host="0.0.0.0", port=8080)
