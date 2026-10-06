import anthropic

from .config import require_claude_config, settings
from .models import ProviderResponse


class ClaudeClient:
    def __init__(self):
        require_claude_config()

        self.client = anthropic.Anthropic(
            api_key=settings.anthropic_api_key
        )

    def ask(self, prompt: str) -> ProviderResponse:
        try:
            response = self.client.messages.create(
                model=settings.claude_model,
                max_tokens=2000,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            text_parts = []

            for block in response.content:
                if hasattr(block, "text"):
                    text_parts.append(block.text)

            text = "\n".join(text_parts)

            input_tokens = getattr(
                response.usage,
                "input_tokens",
                0,
            )

            output_tokens = getattr(
                response.usage,
                "output_tokens",
                0,
            )

            return ProviderResponse(
                provider="claude",
                text=text,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                total_tokens=input_tokens + output_tokens,
            )

        except anthropic.AuthenticationError:
            raise RuntimeError(
                "Claude authentication failed. "
                "Check your ANTHROPIC_API_KEY."
            )

        except anthropic.RateLimitError:
            raise RuntimeError(
                "Claude rate limit reached. Try again later."
            )

        except anthropic.APIError as exc:
            raise RuntimeError(
                f"Claude API error: {exc}"
            )

        except Exception as exc:
            raise RuntimeError(
                f"Claude request failed: {exc}"
            )
