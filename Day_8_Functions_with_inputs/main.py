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

text_list = list(text)
shifted_list = []
for item in text_list:
    if item != " ":
        shifted_list.append(alphabet[(alphabet.index(item))+shift])
    else:
        shifted_list.append(" ")
        

print(shifted_list)