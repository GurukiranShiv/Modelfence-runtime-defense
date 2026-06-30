# ruff: noqa: E402
"""No-API-key local callback demo for aegisRT.

Run:
    python examples/local-callback-demo.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from aegisrt.config.models import ProbeConfig, ReportConfig, RunConfig, TargetConfig
from aegisrt.core.runner import SecurityRunner


def guarded_demo_assistant(user_input: str) -> str:
    lower = user_input.lower()
    blocked = [
        "ignore previous",
        "developer message",
        "system prompt",
        "api key",
        "secret",
        "exfiltrate",
        "bypass",
        "delete database",
        "run shell",
    ]
    if any(term in lower for term in blocked):
        return "I can’t help with that. I can explain safe AI security testing practices instead."
    return "Safe response: this local demo assistant only provides benign security guidance."


PROBES = [
    ProbeConfig(
        id="prompt_injection",
        family="injection",
        generator="static",
        detectors=["regex", "policy"],
        severity="high",
    ),
    ProbeConfig(
        id="data_leakage",
        family="data_leakage",
        generator="static",
        detectors=["leakage", "regex"],
        severity="critical",
    ),
    ProbeConfig(
        id="tool_misuse",
        family="tool_misuse",
        generator="static",
        detectors=["policy", "regex"],
        severity="critical",
    ),
    ProbeConfig(
        id="rag_manipulation",
        family="rag_manipulation",
        generator="static",
        detectors=["regex", "policy"],
        severity="high",
    ),
    ProbeConfig(
        id="refusal_bypass",
        family="refusal_bypass",
        generator="static",
        detectors=["policy", "regex"],
        severity="high",
    ),
]


def main() -> None:
    config = RunConfig(
        target=TargetConfig(type="callback"),
        probes=PROBES,
        report=ReportConfig(formats=["terminal", "json", "html", "sarif", "junit"]),
    )
    runner = SecurityRunner(config, callback_fn=guarded_demo_assistant)
    report = runner.run()
    passed = sum(1 for result in report.results if result.passed)
    failed = len(report.results) - passed
    print(f"\nLocal callback demo complete: {len(report.results)} tests, {passed} passed, {failed} failed")
    print("Reports written under .aegisrt/runs/")


if __name__ == "__main__":
    main()
