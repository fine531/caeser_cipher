alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#This encrypt function encode the user_text 
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
    #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.    
def decrypt(cipher_text, shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        new_letter=alphabet[new_position]
        plain_text += new_letter
    print(f'The decoded text is {plain_text}')
#check whether user want to encode or decode    
if direction== "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text, shift_amount=shift)    
else:
    print("You have entered wrong input")

   
   
