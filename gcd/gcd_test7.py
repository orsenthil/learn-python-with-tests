
def gcd(A :int, B : int) -> int:
    while (A % B) != 0:
        R = A % B
        A = B
        B = R

    return B


def test_gcd():
    assert gcd(16, 12) == 4, "GCD was incorrect"
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"
    assert gcd(2, 4) == 2, "GCD was incorrect"


if __name__ == '__main__':
    test_gcd()
