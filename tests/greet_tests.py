from lib.greet import *

def test_standard_greeting():
    assert greet("Alice") == "Hello, Alice!"

def test_formatting_rules():
    assert greet(" bob ") == "Hello, Bob!"
    assert greet("charlie") == "Hello, Charlie"

def test_edgecase():
    assert greet("") == "Hello, !"

    assert greet(" ") == "Hello, !"

    long_name = "A" * 1000
    assert greet(long_name) == f"Hello, {long_name}!"