from math import sqrt
from os.path import realpath


def factors(n: int) -> list:
    factor = []

    if n % 2 == 0:
        factor.append(2)

    while n % 2 == 0:
        n //= 2

    for num in range(3, int(sqrt(n)) + 1, 2):
        if n % num == 0:
            factor.append(num)

        while n % num == 0:
            n //= num

        if n == 1:
            break

    if n > 1:
        factor.append(n)

    return factor


def main():
    inp = int(open(f'{realpath(__file__)[:-2]}txt').read())

    factor = factors(inp)
    total = 0

    for num in range(1, inp):
        if not any(num % f == 0 for f in factor):
            total += num

    print(total)


if __name__ == '__main__':
    main()