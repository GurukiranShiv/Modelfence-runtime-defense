# aegisRT Market-Ready Execution Steps

These steps are written for Windows PowerShell from the project root.

## 1. Unzip and enter the project

```powershell
Expand-Archive .\aegisRT-market-ready.zip -DestinationPath .
cd .\aegisRT-market-ready
```

## 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -e ".[web,dev,llm]"
```

## 4. Validate the installation

```powershell
python -m aegisrt --version
pytest
python -m compileall aegisrt
```

Expected result: tests should pass and the package should print the installed aegisRT version.

## 5. Run without any API key

```powershell
python examples/local-callback-demo.py
```

This runs aegisRT against a local Python callback target and writes reports under `.aegisrt/runs/`.

## 6. Run local HTTP demo target

Open Terminal 1:

```powershell
python examples/local_http_target.py
```

Open Terminal 2:

```powershell
aegisrt run -c examples/owasp-2025-quick.yaml --compliance
```

## 7. Run the enterprise OWASP profile

```powershell
aegisrt run -c examples/owasp-2025-enterprise.yaml --compliance
```

## 8. Start the web dashboard

```powershell
aegisrt serve
```

Open this URL in your browser:

```text
http://localhost:8484
```

## 9. Run Docker

```powershell
docker build -t aegisrt:market-ready .
docker run --rm -it -p 8484:8484 aegisrt:market-ready aegisrt --help
```

With Docker Compose:

```powershell
docker compose up --build
```

## 10. GitHub push steps

```powershell
git init
git add .
git commit -m "Upgrade aegisRT for AI security market readiness"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 11. Recommended demo flow for recruiters/interviewers

1. Show the README title and description.
2. Run `pytest` to show engineering quality.
3. Run `python examples/local-callback-demo.py` to show no-API-key execution.
4. Run `aegisrt run -c examples/owasp-2025-quick.yaml --compliance` with the local target.
5. Open the generated JSON/HTML report from `.aegisrt/runs/`.
6. Explain OWASP/NIST/MITRE mappings from the docs folder.
