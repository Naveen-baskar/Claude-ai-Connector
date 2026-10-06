from pathlib import Path

from .config import settings
from .router import ask
from .usage import format_usage


BASE_DIR = Path(__file__).resolve().parent.parent

MASTER_PROMPT_PATH = (
    BASE_DIR
    / "prompts"
    / "master_prompt.txt"
)


def load_master_prompt() -> str:
    if not MASTER_PROMPT_PATH.exists():
        raise FileNotFoundError(
            f"Master prompt not found: {MASTER_PROMPT_PATH}"
        )

    return MASTER_PROMPT_PATH.read_text(
        encoding="utf-8"
    )


def build_prompt(user_prompt: str) -> str:
    master_prompt = load_master_prompt()

    return (
        f"{master_prompt}\n\n"
        "========================================\n"
        "USER REQUEST\n"
        "========================================\n\n"
        f"{user_prompt}"
    )


def main():

    print("\n========================================")
    print("       AI MODEL BRIDGE")
    print("========================================\n")

    provider = input(
        f"Provider [claude/external] "
        f"(default: {settings.default_provider}): "
    ).strip().lower()

    if not provider:
        provider = settings.default_provider

    prompt = input("\nEnter your prompt: ").strip()

    if not prompt:
        print("Prompt cannot be empty.")
        return

    try:
        final_prompt = build_prompt(prompt)

        response = ask(
            provider,
            final_prompt,
        )

        print("\n========================================")
        print("AI MODEL RESPONSE")
        print("========================================\n")

        print(response.text)

        print(format_usage(response))

    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")

    except Exception as exc:
        print("\nERROR:")
        print(exc)


if __name__ == "__main__":
    main()
