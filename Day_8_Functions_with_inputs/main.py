# Caesar Cipher
# Functions with inputs
# Arguments and Parameters

# Type 'encode' to encrypt, type 'decode to decrypt:
# encode
# Type your message:
# Hello World!
# Type the shift number:
# 9
# Here's the encoded result: .....!
# Type 'yes if you want to go again. Otherwise type 'no'.
# Type 'encode' to encrypt, type 'decode to decrypt:
# decode
# Type your message:
# adsf asdf sadf
# Type the shift number:
# 9
# Here's the encoded result: .....!
import string

alphabet = list(string.ascii_lowercase)
print(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount, o_direction):
    shifted_list = []
    if direction == "encode":
        for item in text:
            if item != " ":
                shifted_list.append(alphabet[((alphabet.index(item)) + shift) % len(alphabet)])
            else:
                shifted_list.append(" ")
        shifted_list = "".join(shifted_list)
        print(f"Here is the encoded result: {shifted_list}")    
    elif direction == "decode":
        for item in text:
            if item != " ":
                shifted_list.append(alphabet[((alphabet.index(item)) - shift) % len(alphabet)])
            else:
                shifted_list.append(" ")    
        shifted_list = "".join(shifted_list)
        print(f"Here is the decoded result: {shifted_list}") 
    else:
        print("You must select encode or decode!")
          




encrypt(original_text= text, shift_amount= shift, o_direction= direction)