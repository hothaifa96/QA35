# pip install pytest

def test1():
    actual = 2 + 3  # התשובה בפועל
    expected = 5  # התוצאה הצפויה
    assert actual == expected


def test2_n():
    actual = 3 / 1.0
    expected = 2
    assert actual != expected
