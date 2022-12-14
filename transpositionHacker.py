
import detectEnglish
import transpositionDecrypt


def main():

    my_message = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hacked_message = hack_transposition(my_message)

    if hacked_message is None:
        print('Failed to hack encryption.')
    else:
        print(f'Copying hacked message to clipboard: {hacked_message}')


def hack_transposition(message):
    print('Hacking...')
    print('Press Ctrl-C (on Windows) or Ctrl-D (on macOS and Linux) to quit at any time.)')

    for key in range(1, len(message)):
        print(f'Trying key #{key}...')

        decrypted_text = transpositionDecrypt.decrypt_message(key, message)

        if detectEnglish.is_english(decrypted_text):
            print('-----------------------------------------------------------------------')
            print(f'Possible encryption hack: \nKey {key}: {decrypted_text[:100]}')
            print('-----------------------------------------------------------------------')
            print('Enter D if done, anything else to continue hacking:')
            response = input('>>> ')

            if response.strip().upper().startswith('D'):
                return decrypted_text

    return None


if __name__ == '__main__':
    main()
