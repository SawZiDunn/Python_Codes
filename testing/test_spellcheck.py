import pytest
import spellcheck

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input

def test_length(input_value):
    
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) < 50

def test_struc(input_value):
 
    assert spellcheck.first_char(input_value).istitle()
    assert spellcheck.last_char(input_value).endswith(".")

# Run these tests with `python3 -m pytest test_spellcheck.py`