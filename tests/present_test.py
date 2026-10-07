from lib.present import *
import pytest

def test_initial_empty():
    present = Present()
    assert present.contents == None

def test_wrapping_unwrapping():
    present = Present()
    present.wrap("Toy Car")

    assert present.contents == "Toy Car"
    assert present.unwrap() == "Toy Car"

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap("Toy Robot")

    with pytest.raises(Exception) as e:
        present.wrap("Video Game")
    assert str(e.value) == "A contents has already been wrapped."

    
def test_unwrapping_empty_present():
    present = Present()

    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."