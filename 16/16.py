from os.path import realpath


def asciiParse(alpha: list, letters: str) -> dict:
    asciiDict = dict()

    for c, l in zip(letters, range(0, len(alpha), 6)):
        info = dict()
        asci = alpha[l : l + 6]                     # Ascii of a letter

        # This is the trick. 'm' is the maximum length of any row like 5 for 'Y', 1 for 'I', 6 for 'A'
        # Now add 1 to it because we should keep a minimum of 1 space between each character
        m = len(max(asci, key=len)) + 1
        arr = [i.ljust(m, ' ') for i in asci]       # Left justify all the row of Ascii upto width 'm'
        info['arr'] = arr
        info['space'] = ''.join(arr).count(' ')     # Count the spaces in the new Ascii
        asciiDict[c] = info                         # Store the information

    return asciiDict


def kemingDistance(letters: str, asciiDict: dict) -> dict:
    keming = dict()

    """First count list of spaces in right of 1st char. Then list of space in left of 2nd char.
    Keming distance between the two chars is the minimum of sum of distance at each row.
    Now subtract the extra 1 space we added above. This will give the original keming distance
    between the two characters.
    Example: 'A' char's Ascii will be 'A '. If we add 'I' it will be 'A I'
              Keming distance between 'A' and 'I' will be 1. Now we substract 1 for it and final
              distance is 0. So when we actually add 'A' and 'I' we'll have that 1 extra spacing
              between them and we don't have to delete anything"""

    for first in letters:
        fr = [len(i.split('#')[-1]) for i in asciiDict[first]['arr']]
        for sec in letters:
            sl = [len(i.split('#')[0]) for i in asciiDict[sec]['arr']]
            keming[first + sec] = min(x + y for x, y in zip(fr, sl)) - 1

    return keming


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()
    alpha = open(f'{realpath(__file__)[:-5]}alpha.txt').read().split('\n')
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    asciiDict = asciiParse(alpha, letters)
    keming = kemingDistance(letters, asciiDict)
    total = 0

    # For every current char add up the its space and removing that extra columns of unnecessary spaces
    # using kemingDistance. The space we are adding are the spaces present in new Asscii(1 extra padding)
    # so no need to worry about the minimum 1 space required between 2 char.
    for i in range(len(inp) - 1):
        total += (asciiDict[inp[i]]['space'] - 6 * keming[inp[i] + inp[i+1]])
        
    total += asciiDict[inp[len(inp) - 1]]['space'] - 6

    print(total)


if __name__ == '__main__':
    main()