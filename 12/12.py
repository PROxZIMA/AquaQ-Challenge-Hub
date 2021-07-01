from os.path import realpath


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    floors = {}
    for i, data in enumerate(inp.split('\n')):
        floors[i] = tuple(map(int, data.split()))

    visited = 1
    curr = 0
    direction = True

    while True:
        if floors.get(curr, 1) == 1:
            break
        if not floors[curr][0]:
            direction = not direction

        curr += floors[curr][1] if direction else -floors[curr][1]
        visited += 1

    print(visited)


if __name__ == '__main__':
    main()