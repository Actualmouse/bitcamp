from um import count

def test_space():
    assert count('um ') == 1

def test_words():
    assert count('mum') == 0

def test_case():
    assert count('UM') == 1
    assert count('uM') == 1