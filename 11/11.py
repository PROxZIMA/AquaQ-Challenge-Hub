from os.path import realpath


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    areas = []

    for area in inp.split('\n')[1:]:
        lx, ly, ux, uy = map(int, area.split(','))
        # List of tiles in a given area
        areas.append(tuple((x,y) for x in range(lx, ux) for y in range(ly, uy)))

    l = len(areas)

    tiles = set()

    for i in range(l):
        for j in range(i + 1, l):
            # If a common tiles in 2 area then add to set
            if any(x in areas[j] for x in areas[i]):
                tiles = tiles.union(areas[i]).union(areas[j])

    print(len(tiles))


if __name__ == '__main__':
    main()