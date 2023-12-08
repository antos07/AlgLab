import random
import math
import sys

sys.setrecursionlimit(10**7)


# method to return prime divisor for n
def factorize_rho_pollard(n):
    if n == 1:
        return None

    if n % 2 == 0:
        return 2

    x = random.randint(2, n - 2)
    y = x

    c = random.randint(1, n - 1)

    d = 1
    while d == 1:
        x = (x ** 2 + c) % n

        y = (y ** 2 + c) % n
        y = (y ** 2 + c) % n

        d = math.gcd(abs(x - y), n)

        if d == n:
            return factorize_rho_pollard(n)

    return d


def run():
    n = int(input('n = '))
    print(factorize_rho_pollard(n))


if __name__ == '__main__':
    run()
