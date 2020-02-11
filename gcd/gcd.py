def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def main():
    print(gcd(4, 2))


if __name__ == '__main__':
    main()