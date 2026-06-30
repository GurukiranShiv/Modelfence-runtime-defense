"""Local HTTP target for aegisRT demos.

Run:
    python examples/local_http_target.py

Then, in another terminal:
    aegisrt run -c examples/owasp-2025-quick.yaml --compliance
"""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "127.0.0.1"
PORT = 8000


def safe_response(prompt: str) -> str:
    lower = prompt.lower()
    blocked_terms = [
        "ignore previous",
        "system prompt",
        "secret",
        "api key",
        "exfiltrate",
        "bypass",
        "tool",
        "delete",
        "credential",
    ]
    if any(term in lower for term in blocked_terms):
        return "I can’t help with that request. I can provide safe, high-level security guidance."
    return "Safe demo response: I can help with general AI security testing concepts."


class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            payload = json.loads(raw_body)
        except json.JSONDecodeError:
            payload = {}

        prompt = str(payload.get("prompt", ""))
        body = json.dumps({"response": safe_response(prompt)}).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Local aegisRT demo target running at http://{HOST}:{PORT}/chat")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping local demo target.")
        server.server_close()
