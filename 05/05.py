from os.path import realpath


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    d1 = {
        'F': 1,
        'B': 6,
        'L': 2,
        'R': 5,
        'U': 3,
        'D': 4,
    }

    d2 = {
        'F': 1,
        'B': 6,
        'L': 3,
        'R': 4,
        'U': 2,
        'D': 5,
    }

    total = 0

    for i in range(len(inp)):
        m = inp[i]
        if m == 'U':
            d1['F'], d1['U'], d1['B'], d1['D'] = d1['D'], d1['F'], d1['U'], d1['B']
            d2['F'], d2['U'], d2['B'], d2['D'] = d2['D'], d2['F'], d2['U'], d2['B']
        if m == 'D':
            d1['F'], d1['U'], d1['B'], d1['D'] = d1['U'], d1['B'], d1['D'], d1['F']
            d2['F'], d2['U'], d2['B'], d2['D'] = d2['U'], d2['B'], d2['D'], d2['F']
        if m == 'L':
            d1['F'], d1['R'], d1['B'], d1['L'] = d1['R'], d1['B'], d1['L'], d1['F']
            d2['F'], d2['R'], d2['B'], d2['L'] = d2['R'], d2['B'], d2['L'], d2['F']
        if m == 'R':
            d1['F'], d1['R'], d1['B'], d1['L'] = d1['L'], d1['F'], d1['R'], d1['B']
            d2['F'], d2['R'], d2['B'], d2['L'] = d2['L'], d2['F'], d2['R'], d2['B']

        if d1['F'] == d2['F']:
            total += i

    print(total)


if __name__ == '__main__':
    main()