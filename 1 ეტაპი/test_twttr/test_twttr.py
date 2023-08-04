from twttr import shorten

def test_letters():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'

def test_num():
    assert shorten('123') == '123'

def test_punctuation():
    assert shorten('!!') == '!!'