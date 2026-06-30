# ModelFence Runtime Defense

**Security testing and runtime defense framework for LLM applications, RAG systems, and agent workflows.**

ModelFence Runtime Defense helps security teams, developers, and SOC analysts evaluate LLM-powered applications for prompt injection, jailbreaks, sensitive-data leakage, unsafe tool use, RAG poisoning, policy violations, and OWASP LLM Top 10 risks. It produces risk scores, mitigation guidance, compliance-style summaries, and CI/CD-ready security reports.

> **Author:** Gurukiran Shivashankar  
> **Project Type:** LLM Security Testing · Runtime Defense · Red Teaming · SOC/AppSec Reporting  
> **CLI Command:** `aegisrt`  
> **License:** MIT

---

## GitHub Description

Use this as your GitHub repo description:

```text
Security testing and runtime defense framework for LLM apps, RAG systems, and agent workflows with prompt-injection detection, jailbreak testing, data-leakage checks, risk scoring, and CI/CD-ready reports.
```

---

## Why This Project Matters

Modern organizations are rapidly adopting chatbots, copilots, RAG pipelines, and tool-calling agents. These systems introduce new security risks that traditional web scanners and SIEM rules do not fully cover.

ModelFence Runtime Defense provides a practical way to test and document risks such as:

- Prompt injection and indirect prompt injection
- Jailbreak attempts and unsafe response generation
- Sensitive-data leakage and system prompt exposure
- RAG poisoning and malicious retrieved context
- Unsafe tool calls and excessive agency in agent workflows
- Hallucination, weak citations, and unreliable outputs
- Policy violations and insecure model behavior
- CI/CD security validation for LLM applications

---

## Key Features

| Capability | Description |
|---|---|
| Prompt Injection Testing | Tests whether an LLM application follows malicious or hidden instructions. |
| Jailbreak Testing | Evaluates resistance against bypass attempts and unsafe prompt patterns. |
| Data Leakage Checks | Detects sensitive output, system prompt leakage, and confidential data exposure. |
| RAG Security Testing | Reviews retrieval-augmented generation risks such as poisoned context and weak citations. |
| Agent/Tool Misuse Testing | Assesses unsafe tool execution, excessive permissions, and risky workflow behavior. |
| OWASP LLM Mapping | Maps findings to OWASP LLM Top 10 style risk categories. |
| Risk Scoring | Converts test results into severity-based risk scores. |
| Reports | Generates JSON, HTML, SARIF, and JUnit-style outputs for review and automation. |
| Dashboard | Provides a local web dashboard for reviewing results visually. |
| CI/CD Ready | Supports automated security checks in development pipelines. |

---

## Screenshots

### 1. Dashboard Overview

![Dashboard Overview](Screenshots/01-dashboard-overview.png)

### 2. OWASP LLM Top 10 Compliance View

![OWASP LLM Top 10 Compliance](Screenshots/02-owasp-llm-top10-compliance.png)

### 3. Prompt Injection Results

![Prompt Injection Results](Screenshots/03-prompt-injection-results.png)

### 4. Resistance Profile

![Resistance Profile](Screenshots/04-resistance-profile.png)

### 5. Test Suite Validation

![Test Suite Validation](Screenshots/06-test-suite-validation.png)

### 6. Full Dashboard View

![Full Dashboard View](Screenshots/07-dashboard-full-view.png)

---

## Tech Stack

- **Language:** Python
- **Frameworks/Libraries:** FastAPI, Pydantic, HTTPX, Rich, PyYAML, Jinja2
- **Testing:** Pytest, pytest-asyncio
- **Security/Reporting:** SARIF, JUnit XML, JSON, HTML reports
- **Deployment:** Docker, Docker Compose
- **Use Cases:** LLM security, AppSec validation, SOC triage evidence, CI/CD security gates

---

## Project Structure

```text
ModelFence Runtime Defense/
├── aegisrt/                    # Core framework source code
├── docs/                       # Architecture, security mappings, and usage documentation
├── examples/                   # Demo targets and sample scan configurations
├── tests/                      # Unit and integration tests
├── Screenshots/                # Project screenshots for README/GitHub
├── Dockerfile                  # Container build file
├── docker-compose.yml          # Local container runtime
├── pyproject.toml              # Python package configuration
├── EXECUTION_STEPS.md          # Step-by-step run instructions
├── SECURITY.md                 # Security policy
├── THREAT_MODEL.md             # Threat model
└── README.md                   # Project overview
```

---

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/GurukiranShiv/Modelfence-runtime-defense.git
cd Modelfence-runtime-defense
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### 4. Install the project

```powershell
pip install -e ".[web,dev,llm]"
```

---

## Validate the Project

Run the test suite:

```powershell
pytest
```

Compile-check the source code:

```powershell
python -m compileall aegisrt
```

Check the CLI version:

```powershell
python -m aegisrt --version
```

---

## Run the No-API-Key Demo

This demo runs locally and does not require an external LLM API key.

```powershell
python examples/local-callback-demo.py
```

---

## Run a Local HTTP Security Scan

### Terminal 1: Start the local target

```powershell
python examples/local_http_target.py
```

### Terminal 2: Run a quick OWASP-style scan

```powershell
aegisrt run -c examples/owasp-2025-quick.yaml --compliance
```

### Optional: Run an enterprise-style scan

```powershell
aegisrt run -c examples/owasp-2025-enterprise.yaml --compliance
```

---

## Start the Dashboard

```powershell
aegisrt serve
```

Then open:

```text
http://localhost:8484
```

---

## Reports and Outputs

ModelFence Runtime Defense can generate evidence that is useful for security review, SOC workflows, and CI/CD pipelines.

Supported output formats include:

- `report.json` — structured scan results
- `report.html` — human-readable security report
- `report.sarif.json` — SARIF output for code/security platforms
- `report.junit.xml` — CI/CD test-style output

Generated reports are stored under `.aegisrt/runs/` when scans are executed.

---

## Example Security Workflow

1. Define the target LLM application or local demo target.
2. Select a scan profile from the `examples/` folder.
3. Run prompt-injection, jailbreak, RAG, and tool-misuse tests.
4. Review risk scoring and compliance mappings.
5. Export JSON, HTML, SARIF, or JUnit reports.
6. Use the findings for remediation, documentation, or CI/CD gates.

---

## CI/CD Usage

The project supports CI/CD-friendly validation using CLI scans and machine-readable outputs.

Recommended command:

```powershell
aegisrt run -c examples/owasp-2025-quick.yaml --compliance
```

A security team can use this as a pipeline gate to fail builds when high-risk findings are detected.

---

## Documentation

Important documentation included in this project:

| File | Purpose |
|---|---|
| `EXECUTION_STEPS.md` | Exact setup and execution steps |
| `THREAT_MODEL.md` | Threat model for LLM application security testing |
| `SECURITY.md` | Responsible disclosure and security policy |
| `docs/architecture.md` | System design and framework architecture |
| `docs/owasp-2025-coverage.md` | OWASP LLM risk coverage |
| `docs/nist-ai-rmf-crosswalk.md` | NIST AI RMF-style crosswalk |
| `docs/mitre-atlas-mapping.md` | MITRE ATLAS-style adversarial mapping |
| `docs/agentic-ai-security.md` | Agent and tool-calling security guidance |
| `docs/soc-siem-integration.md` | SOC and SIEM integration guidance |

---

## Portfolio Value

This project demonstrates practical skills in:

- LLM application security testing
- Prompt injection and jailbreak analysis
- RAG and agent workflow risk assessment
- Security automation using Python
- CI/CD security reporting
- SOC/AppSec-style evidence generation
- OWASP-style risk mapping and remediation documentation

It is suitable for cybersecurity, SOC analyst, security engineer, AppSec, and AI/LLM security portfolio demonstrations.

---

## Responsible Use

ModelFence Runtime Defense is intended for defensive security testing, education, secure development, and authorized assessments only.

Use this tool only on systems you own or have permission to test. Do not use it to attack third-party systems, bypass security controls, or expose sensitive data without authorization.

---

## Author

**Gurukiran Shivashankar**  
MS Cybersecurity

---

## License

This project is released under the MIT License.
