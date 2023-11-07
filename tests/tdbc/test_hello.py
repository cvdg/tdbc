from tdbc.hello import hello


def test_hello01():
    assert hello("World") == "Hello, World!"


def test_hello02():
    assert hello("Aap") == "Hello, Aap!"
