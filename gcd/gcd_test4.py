def gcd(A :int, B : int) -> int:
    if A % B == 0:
        return B

    R = A % B

    while R != 0:
        A = B
        B = R
        R = A % B

    return B


def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"


if __name__ == '__main__':
    test_gcd()
