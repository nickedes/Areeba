import string


def message_to_list(plaintext):

    message = []
    for char in plaintext:
        message.append(char)

    for x in message:
        if x == " ":
            message.remove(" ")

    i = 0
    for e in range(len(message) / 2):
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'X')
        i = i + 2

    if len(message) % 2 == 1:
        message.append("X")

    i = 0
    new = []
    for x in xrange(1, len(message) / 2 + 1):
        new.append(message[i:i + 2])
        i = i + 2

    return new


def playfair_key_gen(key):
    playfair_key = []
    for e in key.upper():
        if e not in playfair_key:
            playfair_key.append(e)

    if 'i' in key:
        alphabet = string.ascii_uppercase.replace('J', '')
    else:
        alphabet = string.ascii_uppercase.replace('I', '')

    for alpha in alphabet:
        if alpha not in playfair_key:
            playfair_key.append(alpha)

    for x in playfair_key:
        if x == " ":
            playfair_key.remove(" ")

    playfair_key_group = []
    for x in range(5):
        playfair_key_group.append('')
    for i in range(len(playfair_key) / 5):
        playfair_key_group[i] = playfair_key[i * 5:i * 5 + 5]
    return playfair_key_group


msg = raw_input("enter message:")
print(message_to_list(msg))
key = raw_input("enter key:")
print(playfair_key_gen(key))
