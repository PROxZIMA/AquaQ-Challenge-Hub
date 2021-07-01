from os.path import realpath


def add(a: int, b: int) -> int:
    return a + b


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    room = [
        '  ##  ',
        ' #### ',
        '######',
        '######',
        ' #### ',
        '  ##  '
    ]

    nav = {
        'U': [-1, 0],
        'D': [1, 0],
        'L': [0, -1],
        'R': [0, 1],
    }

    r, c, total = 0, 2, 0



    for i in inp:
        tr, tc = map(add, [r, c], nav[i])
        if -1 < tr < 6 and -1 < tc < 6 and room[tr][tc] == '#':
            r, c = tr, tc
        total += (r + c)

    print(total)


if __name__ == '__main__':
    main()