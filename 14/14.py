from os.path import realpath
from collections import defaultdict


def calcLocation(matrix: list) -> defaultdict:
    location = defaultdict(list)

    for i in range(5):
        for j in range(5):
            arr = [i, j + 5]
            if i == j:
                arr.append(10)
            if i + j == 4:
                arr.append(11)
            location[matrix[i][j]] = arr

    return location


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    #           0    1   2   3   4      # 11 (2nd Diagonal)
    matrix  = [[6 , 17, 34, 50, 68],    # 5
               [10, 21, 45, 53, 66],    # 6
               [5 , 25, 36, 52, 69],    # 7
               [14, 30, 33, 54, 63],    # 8
               [15, 23, 41, 51, 62]]    # 9
                                        # 10 (1st Diagonal)

    location = calcLocation(matrix)     # Calculate location according to the numbers above

    winPosition = {0 : 5, 1 : 5, 2 : 5, 3 : 5, 4 : 5, 5 : 5, 6 : 5, 7 : 5, 8 : 5, 9 : 5, 10 : 5, 11 : 5}
    answer = 0

    for seq in inp.split('\n'):
        bingo, seqCount = winPosition.copy(), 0
        for num in map(int, seq.split()):
            seqCount += 1
            for i in location[num]:     # Subtract 1 from all the winning row to which 'num' belongs
                bingo[i] -= 1
            if 0 in bingo.values():
                break
        answer += seqCount

    print(answer)


if __name__ == '__main__':
    main()