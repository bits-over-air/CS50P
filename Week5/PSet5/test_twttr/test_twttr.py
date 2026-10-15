from twttr import shorten

def test_lowercase():
    assert shorten("hello")== "hll"
    assert shorten("world")== "wrld"

def test_uppercase():
    assert shorten("HELLO")== "HLL"
    assert shorten("WORLD")== "WRLD"

def test_numbers_and_punctuation():
    assert shorten("123")== "123"
    assert shorten("hello, world!")== "hll, wrld!"
