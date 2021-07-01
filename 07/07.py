from os.path import realpath


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    Elo = dict()
    Rat = dict()

    for match in inp.split('\n')[1:]:
        a, b, score = match.split(',')
        sa, sb = map(int, score.split('-'))

        Ra, Rb = Rat.get(a, 1200), Rat.get(b, 1200)

        Elo[a] = 1 / (1 + 10 ** ((Rb - Ra) / 400))
        Elo[b] = 1 / (1 + 10 ** ((Ra - Rb) / 400))

        if sa > sb:
            Rat[a] = Ra + 20 * (1 - Elo[a])
            Rat[b] = Rb - 20 * (1 - Elo[a])
        else:
            Rat[a] = Ra - 20 * (1 - Elo[b])
            Rat[b] = Rb + 20 * (1 - Elo[b])

    print(int(max(Rat.values())) - int(min(Rat.values())))


if __name__ == '__main__':
    main()