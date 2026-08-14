# End-to-End Observability Demo

The local stack now contains a small instrumented service, Prometheus metrics, an OpenTelemetry Collector, and Jaeger tracing. This creates a repeatable path from one HTTP request to a metric and trace.

## Start

```bash
cp .env.example .env
docker compose config
docker compose up --build -d
./scripts/validate-e2e.sh
```

Open the following local endpoints after validation:

| Endpoint | Purpose |
|---|---|
| `http://localhost:8088/` | Generates a request, JSON log, Prometheus metric, and trace. |
| `http://localhost:9090/` | Prometheus query UI. |
| `http://localhost:16686/` | Jaeger trace UI; look for `demo-service`. |
| `http://localhost:3000/` | Grafana with Prometheus and Jaeger datasources provisioned. |
| `http://localhost:5601/` | Kibana; Elasticsearch is started but this demo does not ship application logs to it. |

## Scope

The demo proves a local metrics and tracing path. It does **not** prove production telemetry security, high availability, data-retention controls, or a SaaS integration. The demo service emits JSON logs to its container stdout; a separate log shipper and approved log-retention policy are still required before calling Elasticsearch/Kibana an application-log solution.

## Failure scenario

If the request metric appears but no trace reaches Jaeger, check the demo service environment, collector health endpoint, collector logs, the OTLP exporter, and the `otlp/jaeger` exporter endpoint. Do not treat a container being up as proof that a telemetry pipeline is correctly wired.
