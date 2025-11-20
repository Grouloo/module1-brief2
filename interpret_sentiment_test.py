import pytest
from interpret_sentiment import interpret_sentiment

def test_a_compound_above_0_05_is_a_positive_sentiment():
    assert interpret_sentiment(0.6) == ("Positif", "😊")

def test_a_compound_below_0_05_is_a_negative_sentiment():
    assert interpret_sentiment(-0.6) == ("Négatif", "😢")

def test_a_compound_between_0_05_and_0_05_is_a_neutral_sentiment():
    assert interpret_sentiment(0.0) == ("Neutre", "😐")