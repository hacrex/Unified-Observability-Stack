# Unified Observability Stack

A local lab for Grafana, Prometheus, OpenTelemetry Collector, Jaeger, Elasticsearch, Kibana, and Netdata. It includes a small Flask service that emits a Prometheus metric, an OTLP trace, and a JSON log for each request.

## Run the demo

```bash
cp .env.example .env
docker compose up --build -d
./scripts/validate-e2e.sh
```

The validation script waits for the service, sends a few requests, then checks that `demo_service_requests_total` is available in Prometheus and that `demo-service` appears in Jaeger.

| URL | Use |
|---|---|
| `http://localhost:8088/` | Demo service. |
| `http://localhost:9090/` | Prometheus. |
| `http://localhost:16686/` | Jaeger. |
| `http://localhost:3000/` | Grafana. |
| `http://localhost:5601/` | Kibana. |

The demo currently writes application logs to container stdout. Elasticsearch and Kibana are available for experiments, but there is no production log-shipping path in this repository. `docs/END_TO_END_DEMO.md` explains the local trace and metric path and where to look when it breaks.
