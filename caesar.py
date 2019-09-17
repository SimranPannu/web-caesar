import string
import unicodedata
# alphabet_position(letter) function that  receives a letter (that is, a string with only one alphabetic character)
#  and returns the 0-based numerical position of that letter within the alphabet.
def alphabet_position(letter):
    alphabet_pos = 'abcdefghijklmnopqrstuvwxyz' 
    if (letter.isupper()):
        letter=letter.lower()
    position = alphabet_pos.index(letter)
    return position 

# rotate_character(char, rot) function that receives a character char (that is, a string of length 1), and 
# an integer rot. Your function should return a new string of length 1, the result of rotating char by rot number 
# of places to the right.
def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upperAlphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if char.isupper():
        char_pos= alphabet_position(char)
        return (upperAlphabet[(char_pos+rot)%26])
    elif char.islower():
        char_pos= alphabet_position(char)
        return (alphabet[(char_pos+rot)%26]) 
    else:
        return char 
        
def encrypt(text, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upperAlphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        elif char.isalpha():
            encrypted+=rotate_character(char,rot)
        else:
            encrypted=encrypted+char
    return encrypted

#main function
def main():
    user_letter = input("Please enter the letter:")
    letter_postion=alphabet_position(user_letter)  #invoke the function
    print(letter_postion)
    my_char=rotate_character("!",37)
    print(my_char)
    mytext=encrypt("Hello, World!",5)
    print(mytext)
if __name__ == "__main__":
    main()