"""The task is to write function that calculates cube root from any
number with precision 0.0001 without using any standard functions"""


def precise(x, y, z):
    y1 = x ** 3
    while y1 < y:
        x += z
        y1 = x ** 3
    x -= z

    return x


def cube_root():
    y = float(input("Input any number: "))
    x = 0
    z = 1
    negative = False

    if y < 0:
        negative = True
        y = -y

    for i in range(6):
        x = precise(x, y, z)
        z *= 0.1

    if negative:
        return round(-x, 4)
    return round(x, 4)


print(cube_root())
