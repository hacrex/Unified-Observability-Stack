# Triage Note Template: Metric Present, Trace Missing

## Symptom

A request reaches `demo-service`, and Prometheus shows the request metric, but Jaeger does not show the service or trace.

## Checks

1. Check the demo service OTLP endpoint environment variable.
2. Check the collector health endpoint and collector logs.
3. Confirm the Collector trace pipeline includes the OTLP receiver and Jaeger exporter.
4. Confirm the Jaeger endpoint used by the Collector is reachable from the Compose network.
5. Send a new request and wait briefly before concluding the trace is missing.

## Notes

| Time | Check | Observation | Decision |
|---|---|---|---|
| | | | |

## Outcome

State the smallest change that restored the signal. If the issue is unresolved, record the next hypothesis rather than guessing.
