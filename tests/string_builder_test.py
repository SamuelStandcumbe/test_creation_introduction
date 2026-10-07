from lib.string_builder import *

def test_functionality():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_new_input():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"

def test_length():
    string_builder = StringBuilder()
    string_builder.add("python")
    assert string_builder.size() == 6

def test_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add