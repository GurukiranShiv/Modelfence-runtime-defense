FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install --upgrade pip
COPY pyproject.toml README.md LICENSE ./
COPY aegisrt ./aegisrt
COPY docs ./docs
COPY examples ./examples

RUN pip install -e ".[web]"

EXPOSE 8484
CMD ["aegisrt", "serve"]
