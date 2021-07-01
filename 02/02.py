from os.path import realpath


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()
    inp = list(map(int, inp.split()))

    ans = 0
    while True:
        if not inp:
            break
        val = inp.pop(0)
        ans += val
        if val in inp:
            i = len(inp) - inp[::-1].index(val)
            inp = inp[i:]

    print(ans)


if __name__ == '__main__':
    main()