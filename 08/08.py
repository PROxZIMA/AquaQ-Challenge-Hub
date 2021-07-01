from os.path import realpath


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    currMilk, currCereal, last5Milk = 0, 0, [0, 0, 0, 0, 0]

    for data in inp.split('\n')[1:]:
        _, milk, cereal = (int(x) if x.isdigit() else x for x in data.split(','))
        currCereal += cereal

        for day, val in enumerate(last5Milk):
            if currCereal and val:
                currCereal -= 100
                last5Milk[day] -= 100
                break

        last5Milk.pop(0)
        last5Milk.append(milk)
        currMilk = sum(last5Milk)

    print(currMilk + currCereal)


if __name__ == '__main__':
    main()