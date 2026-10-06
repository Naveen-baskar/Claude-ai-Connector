import requests

from .config import require_external_config, settings
from .models import ProviderResponse


class ExternalClient:
    def __init__(self):
        require_external_config()

    def ask(self, prompt: str) -> ProviderResponse:

        headers = {
            "Authorization": (
                f"Bearer {settings.external_api_key}"
            ),
            "Content-Type": "application/json",
        }

        payload = {
            "model": settings.external_model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "max_tokens": 2000,
        }

        try:
            response = requests.post(
                settings.external_api_url,
                headers=headers,
                json=payload,
                timeout=120,
            )

            response.raise_for_status()

        except requests.Timeout:
            raise RuntimeError(
                "External AI request timed out."
            )

        except requests.HTTPError as exc:
            raise RuntimeError(
                f"External AI HTTP error: {exc}"
            )

        except requests.RequestException as exc:
            raise RuntimeError(
                f"External AI connection failed: {exc}"
            )

        try:
            data = response.json()
        except ValueError:
            raise RuntimeError(
                "External AI returned invalid JSON."
            )

        try:
            text = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            raise RuntimeError(
                "Unexpected response format from external AI."
            )

        usage = data.get("usage") or {}

        input_tokens = int(
            usage.get("prompt_tokens", 0)
        )

        output_tokens = int(
            usage.get("completion_tokens", 0)
        )

        total_tokens = int(
            usage.get(
                "total_tokens",
                input_tokens + output_tokens,
            )
        )

        return ProviderResponse(
            provider="external",
            text=text,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
        )
