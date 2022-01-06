import itertools

x = 'bark'

p = itertools.permutations(x)
count = 0 # set count to 0

for x in p:
    count += 1 # increment count each time a new permutation is printed
    print(count, ' ... ', ''.join(x))

