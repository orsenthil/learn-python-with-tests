# filename: test_hello.py


def get_hello() -> str:
    return "Hello, World!"


def test_hello() -> None:
    expected = "Hello, World!"
    actual = get_hello()
    assert actual == expected, "{actual} != {expected}".format(actual=actual, expected=expected)


if __name__ == '__main__':
    test_hello()