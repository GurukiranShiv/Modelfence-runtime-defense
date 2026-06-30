# Agentic AI Security Guide

Agentic AI systems introduce risk because LLMs can plan, call tools, access memory, retrieve documents, and trigger actions.

## Key risks to test

1. **Excessive agency** — model can take actions beyond intended scope.
2. **Unsafe tool execution** — tool calls happen without validation or approval.
3. **Cross-tenant memory leakage** — one user/session can access another user's data.
4. **Indirect prompt injection** — retrieved documents or web pages inject instructions.
5. **Missing human approval** — high-risk actions execute automatically.
6. **Tool output overtrust** — agent blindly trusts untrusted tool output.

## Recommended aegisRT tests

- `tool_misuse`
- `prompt_injection`
- `data_exfiltration`
- `data_leakage`
- `rag_manipulation`
- `refusal_bypass`

## Secure design checklist

- Require allowlists for tools.
- Validate tool arguments server-side.
- Separate user memory, tenant memory, and system memory.
- Mark retrieved content as untrusted.
- Require human approval for payment, deletion, privilege, or external-send actions.
- Log every tool call with user, session, arguments, output, and approval state.
