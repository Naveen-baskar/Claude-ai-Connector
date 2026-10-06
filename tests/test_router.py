import pytest

from app.models import ProviderResponse
from app.router import ask


def test_unknown_provider():
    with pytest.raises(ValueError):
        ask("unknown", "hello")


def test_provider_response_total_tokens():
    response = ProviderResponse(
        provider="test",
        text="hello",
        input_tokens=100,
        output_tokens=50,
    )

    assert response.total_tokens == 150


def test_provider_response():
    response = ProviderResponse(
        provider="claude",
        text="hello",
        input_tokens=10,
        output_tokens=20,
        total_tokens=30,
    )

    assert response.provider == "claude"
    assert response.text == "hello"
    assert response.input_tokens == 10
    assert response.output_tokens == 20
    assert response.total_tokens == 30
