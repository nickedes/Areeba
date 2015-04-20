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
    plaintext_list = []
    for x in range(1, len(message) / 2 + 1):
        plaintext_list.append(message[i:i + 2])
        i = i + 2

    return plaintext_list


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


def encrypt(message, key):
    plaintext_list = message_to_list(message)
    key_set = playfair_key_gen(key)
    # print(key_set)
    cipher_text = []
    for msg in plaintext_list:
        x = [x for x in key_set if msg[0] in x][0]
        i, j = key_set.index(x), x.index(msg[0])
        # print(msg[0])
        y = [y for y in key_set if msg[1] in y][0]
        a, b = key_set.index(y), y.index(msg[1])
        # print(msg[1])
        if i == a:
            # Same Row
            if b == 4:
                b = -1
            if j == 4:
                j = -1
            cipher_text.append(key_set[a][j + 1])
            cipher_text.append(key_set[a][b + 1])
        elif j == b:
            # Same Column
            if i == 4:
                i = -1
            if a == 4:
                a = -1
            cipher_text.append(key_set[i+1][b])
            cipher_text.append(key_set[a+1][b])
        else:
            # Rectangle Case
            cipher_text.append(key_set[i][b])
            cipher_text.append(key_set[a][j])

    return cipher_text


msg = raw_input("enter message:")
# print(message_to_list(msg.upper()))
key = raw_input("enter key:")
# print(playfair_key_gen(key))
print(encrypt(msg.upper(), key))
