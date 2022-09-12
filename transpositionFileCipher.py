
import time
import os
import sys
import transpositionEncrypt
import transpositionDecrypt


def main():
    input_filename = 'frankenstein.encrypted.txt'
    output_filename = 'frankenstein.decrypted.txt'
    my_key = 10
    my_mod = 'decrypt'

    if not os.path.exists(input_filename):
        print(f'The file {input_filename} does not exist. Quitting...')
        sys.exit()

    if os.path.exists(output_filename):
        print(f'This will overwrite the file {output_filename}.\n (C)ontinue or (Q)uit?')
        response = input('>>>  ')
        if not response.lower().startswith('c'):
            sys.exit()

    print(f'{my_mod.title()}ing,,,')

    with open(input_filename, 'r') as ff:
        content = ff.read()

        start_time = time.time()
        if my_mod == 'encrypt':
            translated = transpositionEncrypt.encrypt_message(my_key, content)
        elif my_mod == 'decrypt':
            translated = transpositionDecrypt.decrypt_message(my_key, content)

        total_time = round(time.time() - start_time, 2)
        print(f'{my_mod.title()}ion time: {total_time}')

    with open(output_filename, 'w') as f:
        f.write(translated)

    print(f'Done {my_mod}ing {input_filename} ({len(content)} characters)')
    print(f'{my_mod.title()}ed file is {output_filename}')


if __name__ == '__main__':
    main()
