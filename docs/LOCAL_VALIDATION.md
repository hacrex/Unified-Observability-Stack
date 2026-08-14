# Local Validation

## Start the local stack

```bash
cp .env.example .env
# Set a non-default local Grafana password in .env.
docker compose config
docker compose up -d
```

## Health checks

```bash
curl -fsS http://localhost:9090/-/healthy
curl -fsS http://localhost:9200/_cluster/health
curl -fsS http://localhost:13133/
```

Open Grafana on `http://localhost:3000`, Prometheus on `http://localhost:9090`, Kibana on `http://localhost:5601`, and Netdata on `http://localhost:19999`.

## Scope

The local compose stack provides Prometheus, Grafana, Elasticsearch/Kibana, Netdata, and an OpenTelemetry Collector with a `debug` exporter. SigNoz, Datadog, Splunk, and New Relic integrations remain documented extension points; they require their own accounts, tokens, storage/backends, and organisation-approved routing before operational use.
