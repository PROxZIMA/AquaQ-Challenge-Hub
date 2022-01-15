from os.path import realpath
from collections import deque, defaultdict
from typing import Union


def construct_dict(wordList: set) -> defaultdict:
    d = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            s = word[:i] + '*' + word[i+1:]
            d[s].append(word)
    return d


def shortestPath(source: str, dest: str, d: defaultdict) -> Union[int, list]:
    queue, visited = deque([(source, 1, [source])]), set()
    while queue:
        word, step, path = queue.popleft()
        if word not in visited:
            visited.add(word)
            if word == dest:
                return step, path
            for i in range(len(word)):
                s = word[:i] + '*' + word[i+1:]
                for neighbor in d[s]:
                    if neighbor not in visited:
                        queue.append((neighbor, step + 1, path + [neighbor]))
    return 0, []


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()
    word = open(f'{realpath(__file__)[:-5]}word.txt').read()
    wordDict = construct_dict(set(word.split('\n')))

    product = 1

    for k in inp.split('\n'):
        step, path = shortestPath(*k.split(','), wordDict)
        product *= step
        print(step, ', '.join(path))

    print(f'\nAnswer = {product}')


if __name__ == '__main__':
    main()
