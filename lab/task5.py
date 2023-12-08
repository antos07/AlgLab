import math
from contextlib import suppress


def mod_pow(a, n, mod):
    result = 1
    while n > 0:
        if n % 2:
            result *= a
            result %= mod

        n //= 2
        a **= 2
        a %= mod

    return result


def baby_step_giant_step(g, y, p):
    k = int(math.ceil(math.sqrt(p - 1)))
    x = [mod_pow(g, i, p) for i in range(k)]
    inv = mod_pow(g, k * (p - 2), p)

    for j in range(k):
        tmp = (y * mod_pow(inv, j, p)) % p
        with suppress(ValueError):
            return x.index(tmp) + j * k


def run():
    g = int(input('g = '))
    y = int(input('y = '))
    p = int(input('p = '))
    print(baby_step_giant_step(g, y, p))


if __name__ == '__main__':
    run()
