# program to display all possible permutations of a given string

import itertools

x = '1234'

def allPossiblePermutations(string1):
    permutations = itertools.permutations(string1)

    count = 1

    for x in permutations:
        print(count, '...' ,''.join(string1))
        count += 1

allPossiblePermutations(x)
