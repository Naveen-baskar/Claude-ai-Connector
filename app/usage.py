from .models import ProviderResponse


def format_usage(response: ProviderResponse) -> str:
    return (
        "\n"
        "========================================\n"
        "TOKEN USAGE\n"
        "========================================\n"
        f"Provider: {response.provider}\n"
        f"Input tokens: {response.input_tokens}\n"
        f"Output tokens: {response.output_tokens}\n"
        f"Total tokens: {response.total_tokens}\n"
    )
