from lib.check_codeword import *

def test_functionality():
    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("house") == "Close, but nope."
    assert check_codeword("pizza") == "WRONG!"

def test_edge_cases():
    pass