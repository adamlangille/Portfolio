to_morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                 'y': '-.--', 'z': '--..',
                 '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.', ' ': ' / ', '.': '.-.-.-', '?': '..--..', '!': '-.-.--',
                 "'": '.----.', '&': '.-...', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--',
                 '=': '-...-', '-': '-....-', '"': '.-..-.', '/': '-..-.', '+': '.-.-.', '%':'------..-.-----'}


def convert_to_morse_code():
    '''Get user input and return converted text.'''
    # get user input, a text string to convert into morse code
    text_to_convert = (input('What is your message to convert?: ')).lower()
    # empty string to populate with converted text
    new_string = ''
    # cycle through each character in text, refer to dict to convert each character, add to new string and add space
    # using list comprehension
    new_string = ''.join([(to_morse_dict[char] + ' ') for char in text_to_convert])
    return new_string


# function to ask if they want to convert again
def convert_again():
    '''Ask if the user wants to convert another message.'''

    asking = True
    while asking:
        again = input('Convert another message? (Y/N): ')
        if again == 'N':
            return False
        elif again == 'Y':
            return True
        else:
            print('Invalid input.\n')


# run program until user exits with valid 'N'
on = True
while on:
    print(convert_to_morse_code())
    on = convert_again()




