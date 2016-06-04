def egcd(a, b):
    "To find gcd of two numbers."
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


if __name__ == '__main__':
    x = input("Enter a and b - a is whose inverse is to be found and b is mod value")
    a, b = x.split(" ")
    a, b = int(a), int(b)
    g, x, y = egcd(a, b)
    if(g != 1):
        print("No inverse exists")
    else:
        print(x % b)
