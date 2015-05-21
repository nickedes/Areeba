from random import randrange


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def egcd(a, b):
    "To find gcd of two numbers."
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def invmod(e, m):
    g, x, y = egcd(e, m)
    if g != 1:
        return None
    else:
        return x % m


def public_private_key(p, q):
    """
    Generates public and private for encryption and decryption
    Public key : (e,n)
    Private key : (d,n)
    """
    n = p * q
    m = (p - 1) * (q - 1)
    gcd = 0
    while gcd != 1:
        e = randrange(1, m)
        gcd, _, _ = egcd(e, m)

    d = invmod(e, m)

    return ((e, n), (d, n))


def encrypt(key, msg):
    k, n = key
    cipher = []

    for c in msg:
        cipher.append(pow(ord(c), k, n))

    return cipher


def decrypt(key, msg):
    k, n = key
    plain = []

    for c in msg:
        plain.append(chr(pow(c, k, n)))

    return ''.join(plain)


if __name__ == '__main__':
    p = int(raw_input('Enter 1st Prime no. '))
    q = int(raw_input('Enter 2nd Prime no. '))

    if is_prime(p) and is_prime(q):
        public, private = public_private_key(p, q)
        print "Public key: ", public
        print "Private key: ", private

        message = raw_input("Enter message: ")

        ciphertext = encrypt(public, message)

        print("Encrypted:", ciphertext)
        print("decrypted:", decrypt(private, ciphertext))
    elif p == q:
        print("primes no.s should be distinct")
    else:
        print("Entered No.s are not prime")
