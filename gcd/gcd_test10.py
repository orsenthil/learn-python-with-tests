def gcd(A :int, B : int) -> int:

    while A != 0:
        temp = A
        A = A % B
        B = temp

    print(B)
    return B


def test_gcd():
    assert gcd(16, 12) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"


if __name__ == '__main__':
    test_gcd()
