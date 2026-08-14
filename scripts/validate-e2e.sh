#!/usr/bin/env bash
set -euo pipefail

for command in curl docker; do
  command -v "$command" >/dev/null 2>&1 || {
    echo "Required command not found: $command" >&2
    exit 127
  }
done

for attempt in $(seq 1 30); do
  if curl --fail --silent http://localhost:8088/healthz >/dev/null; then
    break
  fi
  test "$attempt" = 30 && { echo "demo-service did not become healthy" >&2; exit 1; }
  sleep 2
done

for number in 1 2 3 4 5; do
  curl --fail --silent -H "x-request-id: e2e-$number" http://localhost:8088/ >/dev/null
done

for attempt in $(seq 1 30); do
  metric="$(curl --fail --silent 'http://localhost:9090/api/v1/query?query=demo_service_requests_total' || true)"
  trace_services="$(curl --fail --silent http://localhost:16686/api/services || true)"
  if printf '%s' "$metric" | grep -q 'demo_service_requests_total' && printf '%s' "$trace_services" | grep -q 'demo-service'; then
    echo "E2E observability validation passed: metrics and traces are available."
    exit 0
  fi
  sleep 2
done

echo "Timed out waiting for metrics or traces." >&2
exit 1
