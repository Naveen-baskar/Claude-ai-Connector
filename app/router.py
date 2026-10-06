from .claude_client import ClaudeClient
from .external_client import ExternalClient
from .models import ProviderResponse


def ask(
    provider: str,
    prompt: str,
) -> ProviderResponse:

    provider = provider.strip().lower()

    if provider == "claude":
        client = ClaudeClient()
        return client.ask(prompt)

    if provider == "external":
        client = ExternalClient()
        return client.ask(prompt)

    raise ValueError(
        f"Unknown provider '{provider}'. "
        "Available providers: claude, external"
    )
