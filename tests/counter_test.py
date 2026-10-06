from lib.counter import *

def test_functionality():
    counter = Counter()
    counter.add(4) 
    assert counter.report() == 'Counted to 4 so far.'

def test_multiples():
    counter = Counter()
    counter.add(4)
    counter.add(5)
    counter.add(1)
    assert counter.report() == 'Counted to 10 so far.'