import pytest
import asyncio
from main import analyse_sentiment, AnalyseSentimentInput

pytest_plugins = ('pytest_asyncio',)

input = AnalyseSentimentInput(text = "Hello")

@pytest.mark.asyncio
async def test_the_prediction_endpoint_returns_raw_data():
    result = await analyse_sentiment(input)
    assert isinstance(result, dict)
    assert isinstance(result["raw"], dict)
    assert isinstance(result["raw"]["neg"], float)
    assert isinstance(result["raw"]["neu"], float)
    assert isinstance(result["raw"]["pos"], float)
    assert isinstance(result["raw"]["compound"], float)

@pytest.mark.asyncio
async def test_the_prediction_endpoint_returns_interpreted_data():
    result = await analyse_sentiment(input)
    assert isinstance(result, dict)
    assert isinstance(result["interpretation"], dict)
    assert isinstance(result["interpretation"]["label"], str)
    assert isinstance(result["interpretation"]["emoji"], str)