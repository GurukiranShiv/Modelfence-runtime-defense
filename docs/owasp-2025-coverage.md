# OWASP LLM Top 10 2025 Coverage

This document maps aegisRT capabilities to the OWASP Top 10 for LLM and Generative AI Applications 2025 risk areas.

| OWASP 2025 Risk | aegisRT Coverage | Evidence / Probe Area | Recommended Next Improvement |
|---|---|---|---|
| LLM01 Prompt Injection | Strong | prompt_injection, refusal_bypass, converters | Add more indirect prompt injection payloads from retrieved docs |
| LLM02 Sensitive Information Disclosure | Strong | data_leakage, data_exfiltration | Add richer PII, secret, token, and tenant-boundary evidence |
| LLM03 Supply Chain | Partial | static audit, dependency workflow | Add SBOM generation and model/provider allowlist checks |
| LLM04 Data and Model Poisoning | Partial | rag_manipulation, dataset-driven prompts | Add poisoned corpus and retrieval poisoning fixtures |
| LLM05 Improper Output Handling | Strong | unsafe output and code-related probes | Add sink-specific tests for SQL, shell, HTML, and API calls |
| LLM06 Excessive Agency | Strong | tool_misuse, agent trace inspection | Add approval-gate and human-in-loop failure checks |
| LLM07 System Prompt Leakage | Strong | leakage and injection probes | Add explicit system-prompt extraction scoring |
| LLM08 Vector and Embedding Weaknesses | Partial | rag_manipulation | Add vector similarity abuse and cross-document leakage tests |
| LLM09 Misinformation | Strong | hallucination/factuality style checks | Add citation verification and source quality scoring |
| LLM10 Unbounded Consumption | Strong | runtime controls, cost guard | Add denial-of-wallet stress profiles and budget policy examples |

## How to use this mapping

Security teams can use this file to explain what each test family covers, what evidence is produced, and which gaps remain for enterprise adoption.

Recommended command:

```powershell
aegisrt run -c examples/owasp-2025-enterprise.yaml --compliance
```
