from math import gcd


def rsa_example(p, q, message):
    n = p * q

    t = (p - 1) * (q - 1)

    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break

    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

    # encryption
    ct = (message ** e) % n
    print(f"Encrypted message is {ct}")

    # decryption
    mes = (ct ** d) % n
    print(f"Decrypted message is {mes}")


def run():
    p = int(int(input("p = ")))
    q = int(input("q = "))
    message = int(input("message = "))

    rsa_example(p, q, message)


# p=61, q=53, message=65


if __name__ == '__main__':
    run()
