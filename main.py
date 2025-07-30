import morse_talk as mtalk

def main():

    user_choose = input('Type E for encoding the text, \nType D for decoding the text. \nType EXIT to shut down\n')

    if user_choose.upper() == 'E':
        encode()
    elif user_choose.upper() == 'D':
        decode()
    elif user_choose.upper() == 'EXIT':
        print("Bye, see you next time!")
    else:
        print("ERROR, TRY AGAIN")
        main()

def encode():
    coder = True
    while coder:
        text = input('Type your text to convert to Morse Code: ')
        converted_text = mtalk.encode(text)
        print(f"Your Text In Morse Code: {converted_text}")
        answer = input('Would you like to continue? type Y for yes, or N for no\n')
        if answer.upper() == 'Y':
            pass
        elif answer.upper() == 'N':
            coder = False
            main()
        else:
            print("ERROR, try again")

def decode():
    coder = True
    while coder:
        text = input('Type your Morse code to convert to text: ')
        converted_text = mtalk.decode(text)
        print(f"Your Morse Code In Text: {converted_text}")
        answer = input('Would you like to continue? type Y for yes, or N for no\n')
        if answer.upper() == 'Y':
            pass
        elif answer.upper() == 'N':
            coder = False
            main()
        else:
            print("ERROR, try again")

print("WELCOME TO THE MORSE CODE GENERATOR")
main()