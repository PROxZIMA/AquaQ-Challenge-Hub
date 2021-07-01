from os.path import realpath
from functools import reduce


def mul(a: int, b: int) -> int:
    return a * b


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    print(reduce(mul, (int(i) for i in inp.split('\n'))))


if __name__ == '__main__':
    main()