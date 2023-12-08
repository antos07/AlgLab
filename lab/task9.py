import random


def add_points(point1, point2, p, a):
    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 == y2:
        beta = (3 * x1 * x2 + a) * pow(2 * y1, -1, p)
    else:
        beta = (y2 - y1) * pow(x2 - x1, -1, p)

    x3 = (beta * beta - x1 - x2) % p
    y3 = (beta * (x1 - x3) - y1) % p
    return x3, y3


def double_and_add_method(point_g, k, p, a):
    k_binary = bin(k)[2:]
    point1 = point_g
    point2 = point_g

    for i in range(1, len(k_binary)):
        current_bit = k_binary[i: i + 1]
        if current_bit == '1':
            point1 = add_points(point1, point2, p, a)
        else:
            point2 = add_points(point2, point2, p, a)
    return point1


def el_gamal_example(a, p, n, message, point):
    k = random.randint(1, n - 1)
    r = random.randint(1, n - 1)

    point_y = double_and_add_method(point, k, p, a)
    alice_point = double_and_add_method(point, message, p, a)
    print("Alice point: ", alice_point)

    g = double_and_add_method(point, r, p, a)
    h = add_points(alice_point, double_and_add_method(point_y, r, p, a), p, a)

    s = double_and_add_method(g, k, p, a)
    x, y = s
    y = -y
    s = (x, y)

    bob_point = add_points(s, h, p, a)
    print("Bob point: ", bob_point)


if __name__ == '__main__':
    el_gamal_example(
        a=6564647656756756567564,
        p=1564557676556756555423764748464879078528375647687567345687676545638475435434737,
        n=115792089237316195423570985008687907852837564279074904382605163141518161494337,
        message=987877,
        point=(
            55066263022277343669578718895168534326250603453777594175500187360389116729240,
            32670510020758816978083085130507043184471273380659243275938904335757337482424,
        ),
    )
