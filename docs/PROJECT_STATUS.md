# Project Status

## Portfolio Scope

A local observability lab with runnable Grafana, Prometheus, Elasticsearch/Kibana, Netdata, and OpenTelemetry Collector components, plus documented extension points for SigNoz and enterprise SaaS observability tools.

## Intended Deployment Path

Copy `.env.example` to `.env`, set a local Grafana password, run `docker compose config`, then `docker compose up -d`. SaaS backends are not started by the local compose stack.

## Safety and Validation

This repository contains **non-production reference configuration** unless its deployment guide explicitly states otherwise. Review every Terraform plan and Kubernetes manifest in an isolated account, project, subscription, compartment, or cluster before use. Do not commit credentials, cloud access keys, API tokens, or live state files.

## What to Discuss in an Interview

Explain the architecture, the operational trade-offs, how you would validate a change, how you would roll it back, and the parts that require organisation-specific configuration.
