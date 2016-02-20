def egcd(a, b):
    "To find gcd of two numbers."
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


if __name__ == '__main__':
    a, b = 84, 13
    g, x, y = egcd(a, b)
    if(g != 1):
        print("No inverse exists")
    else:
        print(x % b)
