from dataclasses import dataclass


@dataclass
class ProviderResponse:
    provider: str
    text: str
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0

    def __post_init__(self):
        if self.total_tokens == 0:
            self.total_tokens = (
                self.input_tokens + self.output_tokens
            )
