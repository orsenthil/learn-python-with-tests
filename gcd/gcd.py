def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def main():
    print(gcd(2, 4))
    print(gcd(4, 2))
    print(gcd(12, 16))
    print(gcd(16, 12))

if __name__ == '__main__':
    main()