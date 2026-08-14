# Collector Hardening: Next Steps

The local collector is intentionally small. A production design should add bounded queues/retry storage, TLS/mTLS for OTLP, attribute filtering and PII redaction, cardinality controls, collector self-monitoring, resource limits, and separate routing for metrics, logs, traces, and security events. These controls should be added after defining real data classes, retention requirements, and backend ownership.
