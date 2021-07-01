from os.path import realpath
from collections import defaultdict
from re import findall
import time


def shortestPath(source: str, dest: str, word: str) -> str:
    l = len(source)
    check = defaultdict(lambda: False)                  # True if visited a word
    chains = [source]                                   # List of all possible chains of 2-2 or 3-3 from source at a time

    while True:
        newChains = []                                  # New chains with 1 extra word
        for chain in chains:
            curr = chain[-l:]                           # Pick up last word of the chain
            if not check[curr]:
                check[curr] = True                      # Find all valid words that can be made from 'curr' by changing 1 character
                for end in (x for i in range(l) for x in findall(fr'\b{curr[:i]}\w{curr[i+1:]}\b', word) if x != curr):
                    if end == dest:
                        return f'{chain} {end}'
                    newChains.append(f'{chain} {end}')  # Append to the new collection of chains

        chains = newChains                              # Store your new collection
        if not len(chain):
            break


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()
    word = open(f'{realpath(__file__)[:-5]}word.txt').read()

    print('Product = 97920000.\nCan\'t come up with anything good. Sit back and enjoy. This took 12 min with pypy3.\n')
    product = 1
    t = time.time()

    for k in inp.split('\n'):
        t1 = time.time()
        x = shortestPath(*k.split(','), word)
        l = len(x.split())
        product *= l
        print(x, l)
        print(f'\tTime took = {round(time.time() - t1, 2)} s')

    print(f'\nAnswer = {product}')
    print(f'Total time = {round((time.time() - t)/60, 2)} min')


if __name__ == '__main__':
    main()


# dog wog wag war 4
# bow pow paw pay ply 5
# tree free flee fled 4
# fire fare pare park 4
# forge gorge gorse horse house 5
# stall still shill chill chili 5
# start scart scant scent shent sheet sleet gleet greet great 10
# inner inter enter eater oater outer 6
# asking tsking toking coking coning conins conies conges longes lunges lungee bungee burgee burgle burble bubble bobble 17
# coffee coffer confer conker cooker cooter coater crater craver braver brawer drawer 12