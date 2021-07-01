from os.path import realpath


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    key_pad = {
        2 : ' abc' ,
        3 : ' def' ,
        4 : ' ghi' ,
        5 : ' jkl' ,
        6 : ' mno' ,
        7 : ' pqrs',
        8 : ' tuv' ,
        9 : ' wxyz',
        0 : '  '
    }

    for i in inp.split('\n'):
        n, v = map(int, i.split())
        print(key_pad[n][v], end='')


if __name__ == '__main__':
    main()