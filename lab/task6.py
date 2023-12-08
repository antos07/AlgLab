import random

from lab.task3 import calculate_legendre


def mod_p(a, p):
    return (a % p + p) % p


def pick_a(p, n):
    while True:
        a = random.randint(1, max(n, 100))
        if calculate_legendre(mod_p(a ** 2 - n, p), p) == -1:
            return a


def mult(a, b, w, p):
    return (mod_p(a[0] * b[0] + a[1] * b[1] * w, p),
            mod_p(a[0] * b[1] + a[1] * b[0], p))


def mod_pow(a, n, w, p):
    result = (1, 0)
    while n > 0:
        if n % 2:
            result = mult(result, a, w, p)

        n //= 2
        a = mult(a, a, w, p)

    return result


def cipolla_algorithm(p, n):
    a = pick_a(p, n)
    w = ((a ** 2 - n) % p + p) % p

    return mod_pow((a, 1), (p + 1) // 2, w, p)[0]


def run():
    p = int(input('p = '))
    n = int(input('n = '))

    print(cipolla_algorithm(p, n))


if __name__ == '__main__':
    run()
