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

# def encrypt_or_decrypt(original_text, shift_amount, o_direction):
#     output_list = []
#     if direction == "encode":
#         for item in text:
#             if item != " ":
#                 output_list.append(alphabet[((alphabet.index(item)) + shift) % len(alphabet)])
#             else:
#                 output_list.append(" ")
#         output_list = "".join(output_list)
#         print(f"Here is the encoded result: {output_list}")    
#     elif direction == "decode":
#         for item in text:
#             if item != " ":
#                 output_list.append(alphabet[((alphabet.index(item)) - shift) % len(alphabet)])
#             else:
#                 output_list.append(" ")    
#         output_list = "".join(output_list)
#         print(f"Here is the decoded result: {output_list}") 
#     else:
#         print("You must select encode or decode!")
          




# encrypt_or_decrypt(original_text= text, shift_amount= shift, o_direction= direction)

def caeser(original_text, shift_amount, o_direction):
    output_list = []
    if o_direction == "decode":
        shift_amount *= -1
    for item in original_text:
        if item in alphabet:
            output_list.append(alphabet[((alphabet.index(item)) + shift_amount) % len(alphabet)])
        else:
            output_list.append(item)
    output_list = "".join(output_list)
    print(f"Here is the {o_direction}d result: {output_list}")
     
    
go_again = True
while go_again:
    caeser(original_text= text, shift_amount= shift, o_direction= direction)
    again =  input("Type 'yes if you want to go again. Otherwise type 'no'.")
    if again == "no":
        go_again = False
      