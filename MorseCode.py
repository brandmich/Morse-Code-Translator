#Write a program that asks the user to enter a string and converts it into morse code.

#Define Main function.
def main():
    
    #Ask for user input.
    user_input = input('Enter something to be converted to Morse code. Valid characters are A-Z, 0-9, ' \
                       'spaces, commas, periods, and question marks: ')

    #Print the morse code by iterating over the string user_input and convert it to upper case then morse code.
    for i in user_input:
        print(morse[i.upper()], end = '')


    input()

#Make a translation into morse code.
morse = {',' : '--..--',    '.' : '.-.-.-', '?' : '..--..',
         ' ' : ' / ',

         '0' : '-----',     '1' : '.----',  '2' : '..---',
         '3' : '...--',     '4' : '....-',  '5' : '.....',
         '6' : '-....',     '7' : '--...',  '8' : '---..',
         '9' : '----.',

         'A' : '.-',        'B' : '-...',   'C' : '-.-.',
         'D' : '-..',       'E' : '.',      'F' : '..-.',
         'G' : '--.',       'H' : '....',   'I' : '..',
         'J' : '.---',      'K' : '-.-',    'L' : '.-..',
         'M' : '--',        'N' : '-.',     'O' : '---',
         'P' : '.--.',      'Q' : '--.-',   'R' : '.-.',
         'S' : '...',       'T' : '-',      'U' : '..-',
         'V' : '...-',      'W' : '.--',    'X' : '-..-',
         'Y' : '-.-',       'Z' : '--..',
        }

    
#Call the main function.    
main()
