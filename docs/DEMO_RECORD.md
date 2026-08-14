# Local Observability Demo Record

Complete this after running the local stack. The useful evidence is one request flowing into a metric and a trace, not a list of tools.

## Run details

| Item | Record |
|---|---|
| Date | |
| Host or environment | |
| Compose version | |
| Demo service image/build | |

## Commands run

```bash
docker compose up --build -d
./scripts/validate-e2e.sh
```

## Evidence checklist

| Signal | What to capture | Result |
|---|---|---|
| Metric | Prometheus query for `demo_service_requests_total` | |
| Trace | Jaeger service list and one trace for `demo-service` | |
| Log | `docker compose logs demo-service` with a JSON request record | |
| Dashboard | Grafana datasource or panel view | |

Add screenshots only after the command succeeds. Redact local usernames, tokens, and unrelated browser tabs before committing images.

## One useful observation

Write a real note from the run, such as collector startup order, trace arrival delay, or a query correction.
