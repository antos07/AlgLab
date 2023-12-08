import itertools
import math


def euler_function(n):
    result = 1
    for i in itertools.count(2):
        if i ** 2 > n:
            if n > 1:
                result *= n - 1
            return result

        k = 1
        while n % i == 0:
            n //= i
            k *= i
        if k > 1:
            result *= k // i * (i - 1)


def mobius_function(n):
    k = 0
    for i in itertools.count(2):
        if i * i > n:
            if n > 1:
                k += 1
            return -1 if k % 2 else 1
        if n % i == 0:
            n //= i
            k += 1
            if n % i == 0:
                return 0
            
            
def lcm_of_multiple_numbers(numbers):
    lcm, *numbers = numbers
    for number in numbers:
        lcm = lcm * number // math.gcd(lcm, number)
    return lcm


def run():
    options = [
        'Euler function',
        'Möbius function',
        'LCM of multiple numbers',
    ]
    options = [f'{i}) {option}' for i, option in enumerate(options, start=1)]
    print('Options:', *options, sep='\n')
    chosen_option = input('Enter option index or anything else to exit: ')
    if chosen_option == '1':
        n = int(input('n = '))
        print(f'φ({n}) =', euler_function(n))
    if chosen_option == '2':
        n = int(input('n = '))
        print(f'μ({n}) =', mobius_function(n))
    if chosen_option == '3':
        numbers = [int(n) for n in input('Numbers: ').split()]
        print(f'LCM =', lcm_of_multiple_numbers(numbers))


if __name__ == '__main__':
    run()
