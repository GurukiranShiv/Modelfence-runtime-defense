# NIST AI RMF / NIST AI 600-1 Crosswalk

This crosswalk explains how aegisRT supports AI risk management activities.

| NIST AI RMF Function | How aegisRT Helps | Example Evidence |
|---|---|---|
| Govern | Provides repeatable AI security test policy and risk categories | README, threat model, security policy, compliance report |
| Map | Connects LLM/RAG/agent risks to system behavior | Target metadata, probe families, OWASP mapping |
| Measure | Runs tests and generates measurable findings | JSON, SARIF, JUnit, HTML reports |
| Manage | Supports remediation prioritization and CI/CD gates | Severity, confidence, fail policy, GitHub Actions |

## GenAI Profile relevance

For generative AI systems, aegisRT helps evaluate risks around prompt injection, leakage, unsafe tool use, hallucination, data exposure, and resource consumption. These are useful signals for secure design reviews, pre-production checks, and continuous monitoring.

## Suggested enterprise evidence package

- Test configuration YAML
- Generated report JSON
- HTML executive report
- SARIF/JUnit CI artifacts
- OWASP coverage table
- Threat model
- Known limitations and remediation notes
