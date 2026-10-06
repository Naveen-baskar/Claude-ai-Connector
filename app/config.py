import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    anthropic_api_key: str | None
    claude_model: str | None

    external_api_key: str | None
    external_api_url: str | None
    external_model: str | None

    default_provider: str


settings = Settings(
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    claude_model=os.getenv("CLAUDE_MODEL"),
    external_api_key=os.getenv("EXTERNAL_API_KEY"),
    external_api_url=os.getenv("EXTERNAL_API_URL"),
    external_model=os.getenv("EXTERNAL_MODEL"),
    default_provider=os.getenv("DEFAULT_PROVIDER", "claude").lower(),
)


def require_claude_config() -> None:
    if not settings.anthropic_api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is missing. "
            "Add it to your .env file."
        )

    if not settings.claude_model:
        raise RuntimeError(
            "CLAUDE_MODEL is missing. "
            "Add the Claude model name to your .env file."
        )


def require_external_config() -> None:
    missing = []

    if not settings.external_api_key:
        missing.append("EXTERNAL_API_KEY")

    if not settings.external_api_url:
        missing.append("EXTERNAL_API_URL")

    if not settings.external_model:
        missing.append("EXTERNAL_MODEL")

    if missing:
        raise RuntimeError(
            "Missing external provider configuration: "
            + ", ".join(missing)
        )
