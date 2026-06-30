# aegisRT Threat Model

## Assets

- Test configurations
- Prompt datasets
- Target URLs and headers
- API keys and environment variables
- Generated reports and evidence
- Agent traces and retrieved context
- CI/CD artifacts

## Trust boundaries

1. Developer workstation
2. CI/CD runner
3. Target LLM application
4. Model provider API
5. Report storage directory
6. Web dashboard
7. SIEM/SOC export destination

## Primary threats

| Threat | Risk | Mitigation |
|---|---|---|
| Secret leakage in configs | API keys may be committed | Use environment variables and secret scanning |
| Unsafe target testing | Scans may hit unauthorized systems | Require explicit target ownership/permission |
| Sensitive evidence in reports | Reports may contain PII/secrets | Restrict report access and redact before sharing |
| CI/CD credential exposure | Logs may leak tokens | Mask secrets and avoid printing headers |
| Malicious prompt datasets | Dataset content may include unsafe payloads | Treat datasets as untrusted and review before use |
| Dashboard exposure | Local web UI may expose results | Bind locally or protect behind auth in enterprise use |

## Design assumptions

- Users are authorized to test the configured target.
- API keys are supplied through environment variables.
- Reports are stored in a controlled workspace.
- CI artifacts are access-controlled by the repository/organization.

## Recommended controls

- Use `.env` locally but never commit it.
- Add secret scanning to GitHub.
- Keep generated reports out of public repos unless sanitized.
- Use SARIF/JUnit for security gates.
- Apply least privilege to model/API credentials.
