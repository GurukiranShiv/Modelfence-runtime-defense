# SOC and SIEM Integration

AegisRT findings can support SOC triage, AI AppSec dashboards, and continuous security monitoring.

## Useful outputs

| Output | Use |
|---|---|
| JSON | Splunk/Elastic ingestion |
| SARIF | GitHub code scanning/security view |
| JUnit | CI/CD test gate and build history |
| HTML | Manager/executive review |
| Terminal | Developer feedback loop |

## Suggested Splunk fields

- `run_id`
- `target.type`
- `target.url`
- `probe.id`
- `probe.family`
- `severity`
- `confidence`
- `passed`
- `detectors`
- `evidence`
- `timestamp`

## Suggested alert rules

- Critical finding in production target
- Repeated prompt-injection failure across releases
- Sensitive data leakage detected
- Tool misuse or missing approval detected
- Token/cost budget exceeded

## SOC playbook flow

1. Ingest JSON report.
2. Normalize fields by probe, severity, and target.
3. Alert on high/critical failures.
4. Attach generated evidence to ticket.
5. Route to AppSec, platform, or AI engineering owner.
6. Re-run aegisRT after remediation.
