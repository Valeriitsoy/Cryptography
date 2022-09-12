

def main():
    my_message = 'Common sense is not so common.'
    my_key = 8
    ciphertext = encrypt_message(my_key, my_message)

    print(ciphertext + '|')


def encrypt_message(key, message):
    ciphertext = [''] * key

    for column in range(key):
        current_index = column

        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    main()

