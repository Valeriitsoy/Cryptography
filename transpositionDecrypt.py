import math


def main():
    my_message = 'Cenoonommstmme oo snnio. s s c'
    my_key = 8

    plaintext = decrypt_message(my_key, my_message)

    print(plaintext + '|')


def decrypt_message(key, message):
    num_of_columns = int(math.ceil(len(message) / float(key)))

    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    plaintext = [''] * num_of_columns
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1
    return ''.join(plaintext)


if __name__ == '__main__':
    main()

