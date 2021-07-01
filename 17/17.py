from os.path import realpath
from collections import defaultdict


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()
    inp = '''team       date       score
---------------------------
Somaliland 1900.01.01 1
Formosa    1900.01.01 0
Genoa      1900.01.01 1
Genoa      1900.01.02 0
Somaliland 1900.01.03 0
Genoa      1900.01.03 0
Genoa      1900.01.06 0
Genoa      1901.01.21 1
Somaliland 1902.01.01 1'''


if __name__ == '__main__':
    main()