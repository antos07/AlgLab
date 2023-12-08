from functools import lru_cache
from itertools import count


@lru_cache
def is_prime(a):
    for i in count(2):
        if i * i > a:
            return True
        if a % i == 0:
            return False


def factorize(n):
    factors = []

    for i in count(2):
        if i * i > n:
            break
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    return factors


def calculate_legendre(a, p):
    assert p > 0
    assert p != 2
    assert is_prime(p)

    if a >= p or a < 0:
        return calculate_legendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p - 1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not is_prime(a):
        factors = factorize(a)
        product = 1
        for pi in factors:
            product *= calculate_legendre(pi, p)
        return product
    else:
        if ((p - 1) // 2) % 2 == 0 or ((a - 1) // 2) % 2 == 0:
            return calculate_legendre(p, a)
        else:
            return (-1) * calculate_legendre(p, a)


def calculate_jacobi(a, n):
    assert n > 0 and n % 2

    a = a % n
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t *= -1

        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t *= -1

        a %= n

    if n == 1:
        return t
    return 0


def run():
    options = [
        'Legendre symbol',
        'Jacobi symbol',
    ]
    options = [f'{i}) {option}' for i, option in enumerate(options, start=1)]
    print('Options:', *options, sep='\n')
    chosen_option = input('Enter option index or anything else to exit: ')
    if chosen_option == '1':
        a = int(input('a = '))
        p = int(input('p = '))
        print(calculate_legendre(a, p))

    if chosen_option == '2':
        a = int(input('a = '))
        n = int(input('n = '))
        print(calculate_jacobi(a, n))


if __name__ == '__main__':
    run()
