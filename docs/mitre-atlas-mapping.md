# MITRE ATLAS-Style Mapping

MITRE ATLAS is commonly used by AI security teams to reason about adversarial tactics and techniques against AI-enabled systems. This file maps aegisRT test areas to ATLAS-style behavior categories.

| aegisRT Area | ATLAS-Style Behavior | Security Question |
|---|---|---|
| prompt_injection | Instruction manipulation | Can user input override developer/system intent? |
| refusal_bypass | Safety control bypass | Can the model be pushed past refusal boundaries? |
| data_leakage | Sensitive data disclosure | Does the model expose secrets, PII, or internal context? |
| data_exfiltration | Data extraction | Can attackers extract hidden or cross-tenant information? |
| tool_misuse | Agent/tool abuse | Can the model invoke tools without proper authorization? |
| rag_manipulation | Retrieval manipulation | Can malicious retrieved content control the answer? |
| hallucination/factuality | Misinformation generation | Does the system fabricate facts, sources, or claims? |
| resource_exhaustion | Denial of wallet / consumption abuse | Can attackers force excessive cost, tokens, or latency? |

## Recommended additions

- Add technique IDs if your organization uses a formal ATLAS control library.
- Link each finding to a remediation playbook.
- Track repeated failures across releases as security regression risk.
