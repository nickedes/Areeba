import string
from itertools import imap, cycle

alpha = string.ascii_lowercase


def caesar(c, k):
    return alpha[(alpha.index(c) + int(k)) % 26]


def vigenere(c, k):
    return alpha[(alpha.index(c) + alpha.index(k)) % 26]


def encrypt(cipher, plain, key):
    return "".join(imap(cipher, plain, cycle(key)))

if __name__ == '__main__':

    inp = raw_input("Enter string: ")
    inp = inp.lower()

    print "Caeser'd Text: ", encrypt(caesar, inp, [13])
    print "Vigenere'd Text: ", encrypt(vigenere, inp, "chaitu")
