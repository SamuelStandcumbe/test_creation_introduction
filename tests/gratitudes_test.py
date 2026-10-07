from lib.gratitudes import *

def test_if_empty_on_start():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_one_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("my health")
    assert gratitudes.format() == "Be grateful for: my health"

def test_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("my health")
    gratitudes.add("the rain")
    gratitudes.add("dessert")
    assert gratitudes.format() == "Be grateful for: my health, the rain, dessert"

'''
def test_multiple_at_once():
    gratitudes = Gratitudes()
    gratitudes.add("my health", "the rain", "dessert")
    assert gratitudes.format() == "Be grateful for: my health, the rain, dessert"
'''