# AI Model Bridge

A secure Python application for connecting Claude and an external AI model
through a unified provider interface.

## Features

- Claude API integration
- External AI API integration
- Provider routing
- Token usage tracking
- Environment-based secrets
- Git-safe configuration
- Modular architecture
- Easy provider extension

## Requirements

Python 3.10+

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:
```cmd
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env`.

Windows PowerShell:
```powershell
Copy-Item .env.example .env
```

macOS/Linux:
```bash
cp .env.example .env
```

Edit `.env` and add your real credentials.

**Never commit `.env`.**

## Run
```bash
python -m app.main
```

Choose:
```
claude
```
or:
```
external
```

## Tests
```bash
pytest
```

## Git

Initialize:
```bash
git init
```

Check files:
```bash
git status
```

Commit:
```bash
git add .
git commit -m "Initial AI model bridge"
```

Connect GitHub:
```bash
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Security

Never:

- hardcode API keys
- commit .env
- put API keys in README
- print API keys
- log Authorization headers
- upload secrets to GitHub

If a key is exposed publicly, revoke it and create a new key.

## Token usage

Claude usage is reported separately from external-model usage.

The application does not convert external-model tokens into Claude tokens.

Claude tokens belong to Anthropic.

External-model tokens belong to the external provider.

## Adding another provider

Create a new client inside:
`app/`

Return the common:
`ProviderResponse`

Then register the provider in:
`app/router.py`

## External API

The current external adapter assumes an OpenAI-compatible API.

If the external provider uses a different request or response format,
modify:
`app/external_client.py`

Do not modify the security architecture or hardcode credentials.
