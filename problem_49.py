from collections import defaultdict, Counter
from itertools import combinations
import math
from typing import List


def erathos(n: int, lower_bound: int = 0) -> List[bool]:
    a = [True for _ in range(n)]
    a[0], a[1] = False, False
    for i, isprime in enumerate(a):
        if isprime:
            if i >= lower_bound:
                yield i
            for n in range(i * i, n, i):
                a[n] = False


foo = [prime for prime in erathos(n=10000, lower_bound=1000)]

# find permutations
primes = defaultdict(list)
for prime in foo:
    p = "".join(sorted(str(prime)))
    primes[p].append(prime)

sequences = [p for p in primes.values() if len(p) > 3]

# here is the example sequence from the description
# [1487, 1847, 4817, 4871, 7481, 7841, 8147, 8741],

# brute force look for all differences
# n choose k for k=2 is ~ O(m*n*2)
# where m are the number of serquences
# and n are the avg number of elements in a sequence
for x in sequences:
    z = defaultdict(set)
    for i, j in combinations(x, 2):
        k = j - i
        z[k].add(i)
        z[k].add(j)
        if len(z[k]) == 3:
            print(f"diff: {k}, nums:{sorted(list(z[k]))}")