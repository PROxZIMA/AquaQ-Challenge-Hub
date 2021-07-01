from os.path import realpath
import re


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    print('Regex answer:', sum(len(re.findall(r'(.+?)(?=\1)', pat)) + 1 for pat in inp.split('\n')))
    print("Counts all non-overlapping sub groups that repeat itself like 'akmakm' " +
        "but gives 1 extra for 'akkmakkm' cuz 'kk' repeats itself in the last part.")

    total = 0

    for string in inp.split('\n'):
        lens = len(string)
        maxOccur = 0

        for size in range(1, lens // 2 + 1):
            # divides string in parts of length 'size'

            for skip in range(size):
                # skip 0, 1, 2, ..., size - 1 characters from start

                if size * 2 + skip > lens:
                    # If no more than 2 strings can be formed break the loop
                    break

                repeat = 0
                max_repeat = 0
                val = string[skip : skip + size]

                for i in range(skip, lens - (lens % size), size):
                    # starting from skip and with jump of size
                    # find cosecutive identical strings

                    temp = string[i : i + size]
                    if temp == val:
                        repeat += 1
                    else:
                        repeat = 1
                        val = temp

                    max_repeat = max(max_repeat, repeat)

                maxOccur = max(maxOccur, max_repeat)

        total += maxOccur

    print('\nOriginal answer', total)


if __name__ == '__main__':
    main()