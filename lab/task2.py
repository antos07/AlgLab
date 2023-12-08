import sys
from functools import reduce


def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if m == 1:
        return 0

    # Apply extended Euclid Algorithm
    while a > 1:
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t

    # Make x1 positive
    if x1 < 0:
        x1 = x1 + m0

    return x1


def find_min_x(a, n):
    prod = reduce(lambda acc, n_i: acc * n_i, n, 1)

    # Initialize result
    result = 0
    # Apply above formula
    for a_i, n_i in zip(a, n):
        pp = prod // n_i
        result = result + a_i * inv(pp, n_i) * pp

    return result % prod


def run():
    print('Format: a_i n_i')
    a = []
    n = []
    for line in sys.stdin:
        a_i, n_i = map(int, line.split())
        a.append(a_i)
        n.append(n_i)
    
    print(find_min_x(a, n))


if __name__ == '__main__':
    run()
