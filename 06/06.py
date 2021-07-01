from os.path import realpath


def main():
    inp = int(open(f'{realpath(__file__)[:-2]}txt').read())

    total = 0
    for i in range(inp + 1):
        for j in range(inp - i + 1):
            total += f'{i}{j}{inp - i - j}'.count('1')

    print(total)


if __name__ == '__main__':
    main()