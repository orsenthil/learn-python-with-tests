def is_a_palindrome(term) -> bool:
    return False


def test_palindrome():
    assert is_a_palindrome("ABBA") == True
    assert is_a_palindrome("BOB")  == True
    assert is_a_palindrome("B") == True