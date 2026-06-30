# aegisRT — AI Red Teaming & LLM Security Testing Framework

**aegisRT** is a Python-native AI security testing framework for evaluating LLM applications, RAG systems, and agentic AI workflows against prompt injection, sensitive data leakage, tool misuse, excessive agency, system prompt leakage, hallucination, unsafe code generation, vector/retrieval attacks, and OWASP LLM Top 10 2025 risks.

This upgraded version is positioned for current AI security, SOC, AppSec, platform security, and AI governance expectations. It includes CLI scans, web dashboard support, compliance summaries, SARIF/JUnit/JSON/HTML output, static audit capability, dataset-driven probes, benchmark mode, agent trace inspection, and CI/CD-ready reporting.

## Why this project matters now

Modern companies are adopting LLM apps, RAG pipelines, copilots, workflow agents, and tool-calling systems. Security teams now need repeatable tests for:

- Prompt injection and indirect prompt injection
- Sensitive information disclosure and system prompt leakage
- Excessive agency and unsafe tool execution
- RAG poisoning, malicious retrieved content, and vector weakness
- Unsafe code generation and improper output handling
- Misinformation, weak citations, and hallucination risk
- Resource exhaustion, denial-of-wallet, and unbounded consumption
- Evidence capture for security review, SOC triage, and audit reports

## Core capabilities

| Capability | Included |
|---|---:|
| LLM red-team probes | Yes |
| OWASP LLM Top 10 2025 mapping | Yes |
| RAG and vector security guidance | Yes |
| Agentic AI/tool misuse guidance | Yes |
| NIST AI RMF / NIST AI 600-1 crosswalk | Yes |
| MITRE ATLAS-style mapping | Yes |
| SARIF output for GitHub security workflows | Yes |
| JUnit output for CI test gates | Yes |
| JSON/HTML reports | Yes |
| Static audit mode | Yes |
| Web dashboard | Yes |
| Docker support | Yes |
| GitHub Actions CI/security workflows | Yes |

## Install locally

```powershell
cd aegisRT-market-ready
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[web,dev,llm]"
```

## Validate the project

```powershell
pytest
python -m compileall aegisrt
python -m aegisrt --version
```

## Run the no-API-key demo

```powershell
python examples/local-callback-demo.py
```

## Run a local HTTP OWASP 2025 scan

Terminal 1:

```powershell
python examples/local_http_target.py
```

Terminal 2:

```powershell
aegisrt run -c examples/owasp-2025-quick.yaml --compliance
```

Enterprise-style scan:

```powershell
aegisrt run -c examples/owasp-2025-enterprise.yaml --compliance
```

## Start the dashboard

```powershell
aegisrt serve
```

Open: `http://localhost:8484`

## CI/CD usage

The repository includes GitHub Actions examples:

- `.github/workflows/ci.yml` — lint, tests, package build
- `.github/workflows/security.yml` — dependency audit, static security scan, Bandit, and SARIF upload pattern

Recommended CI gate:

```powershell
aegisrt run -c examples/owasp-2025-quick.yaml --compliance
```

Fail the build when high/critical findings exceed your policy threshold.

## Documentation added for market readiness

- `EXECUTION_STEPS.md` — exact setup and run instructions
- `UPGRADE_REPORT.md` — what changed and why
- `SECURITY.md` — vulnerability reporting policy
- `THREAT_MODEL.md` — framework threat model
- `docs/owasp-2025-coverage.md` — OWASP LLM Top 10 2025 mapping
- `docs/nist-ai-rmf-crosswalk.md` — AI RMF and GenAI Profile crosswalk
- `docs/mitre-atlas-mapping.md` — adversarial AI technique mapping
- `docs/agentic-ai-security.md` — agent/tool security testing guidance
- `docs/soc-siem-integration.md` — SOC and SIEM export guidance

## Portfolio positioning

Use this GitHub description:

> Python-native AI red-teaming framework for testing LLM, RAG, and agentic AI applications against OWASP LLM Top 10 2025 risks, prompt injection, sensitive data leakage, tool misuse, excessive agency, hallucination, unsafe code generation, and unbounded consumption with CI/CD-ready SARIF, JUnit, JSON, and HTML reports.

## Responsible use

Use aegisRT only against systems you own or are authorized to test. The project is intended for defensive evaluation, secure development, compliance evidence, and security validation.
