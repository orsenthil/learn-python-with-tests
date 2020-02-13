def gcd(A :int, B : int) -> int:
    while A != 0:
        R = A % B
        B = A
        A = R

    return B


def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"


if __name__ == '__main__':
    test_gcd()
