from lib.report_length import *

def test_functionality():
    result = report_length("Banana")
    assert result == "This string was 6 characters long."