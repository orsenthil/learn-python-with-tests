def is_a_palindrome(term) -> bool:
    reversed_term = term[::-1]
    if reversed_term == term:
        return True
    return False


def test_palindrome():
    assert is_a_palindrome("ABBA") == True
    assert is_a_palindrome("BOB")  == True
    assert is_a_palindrome("B") == True
    assert is_a_palindrome("NOT") == False