# Portfolio Notes

## My focus

This repository is a local troubleshooting lab. I use it to demonstrate how metrics, logs, host telemetry, and OTLP data fit together and how to validate the path before adding an enterprise backend.

## Evidence I can show

- `docker-compose.yml` for runnable local services and health checks.
- `stacks/grafana/prometheus.yml` and datasource provisioning.
- `stacks/signoz/otel-collector-config.yaml` for receiver, processor, and exporter flow.
- `docs/LOCAL_VALIDATION.md` for health checks and scope.

## Known boundary

The local collector uses a debug exporter, not a persistent trace backend. SigNoz, Datadog, New Relic, and Splunk require separately approved integrations, credentials, retention, and access controls.
