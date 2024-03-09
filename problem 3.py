"""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 09, 2024                                                    
************************************************************************
"""
# Write a program that asks the user for the plaintext (all uppercase letters, no  spaces)  
# and  the  keyword  (all  uppercase  letters)  and  produce  the ciphertext using the Vigenère cipher. 
# Give the output of your program for the following message and key:
# Message: THISISTHELASTTASKHOORDAY
# Key: KNIGHTS

def encrypt(string):
    # Encrypts the given string
    ciphered = []
    for i in string:
        if i == "A":
            ciphered.append(0)
        elif i == "B":
            ciphered.append(1)
        elif i == "C":
            ciphered.append(2)
        elif i == "D":
            ciphered.append(3)
        elif i == "E":
            ciphered.append(4)
        elif i == "F":
            ciphered.append(5)
        elif i == "G":
            ciphered.append(6)
        elif i == "H":
            ciphered.append(7)
        elif i == "I":
            ciphered.append(8)
        elif i == "J":
            ciphered.append(9)
        elif i == "K":
            ciphered.append(10)
        elif i == "L":
            ciphered.append(11)
        elif i == "M":
            ciphered.append(12)
        elif i == "N":
            ciphered.append(13)
        elif i == "O":
            ciphered.append(14)
        elif i == "P":
            ciphered.append(15)
        elif i == "Q":
            ciphered.append(16)
        elif i == "R":
            ciphered.append(17)
        elif i == "S":
            ciphered.append(18)
        elif i == "T":
            ciphered.append(19)
        elif i == "U":
            ciphered.append(20)
        elif i == "V":
            ciphered.append(21)
        elif i == "W":
            ciphered.append(22)
        elif i == "X":
            ciphered.append(23)
        elif i == "Y":
            ciphered.append(24)
        elif i == "Z":
            ciphered.append(25)
    return ciphered

def decyrpt(mod_list):
    # Converts a list of integers back to letters.
    result = ""
    for i in mod_list:
        if i == 0:
            result += "A"
        elif i == 1:
            result += "B"
        elif i == 2:
            result += "C"
        elif i == 3:
            result += "D"
        elif i == 4:
            result += "E"
        elif i == 5:
            result += "F"
        elif i == 6:
            result += "G"
        elif i == 7:
            result += "H"
        elif i == 8:
            result += "I"
        elif i == 9:
            result += "J"
        elif i == 10:
            result += "K"
        elif i == 11:
            result += "L"
        elif i == 12:
            result += "M"
        elif i == 13:
            result += "N"
        elif i == 14:
            result += "O"
        elif i == 15:
            result += "P"
        elif i == 16:
            result += "Q"
        elif i == 17:
            result += "R"
        elif i == 18:
            result += "S"
        elif i == 19:
            result += "T"
        elif i == 20:
            result += "U"
        elif i == 21:
            result += "V"
        elif i == 22:
            result += "W"
        elif i == 23:
            result += "X"
        elif i == 24:
            result += "Y"
        elif i == 25:
            result += "Z"
    return result

# Inputs
message = str(input("Enter a message: ").upper().replace(" ", ""))
key = str(input("Enter a key: ").upper())

# Encrypt the message and key
message_cipher = encrypt(message)

# Ensure the key length matches the message length
if not len(message_cipher) == len(key):
    key_fill = key * (len(message_cipher) // len(key)) + key[:len(message_cipher) % len(key)]

key_cipher= encrypt(key_fill)

# Add corresponding elements from the message and key cipher lists
add_list = [sum(i) for i in zip(message_cipher, key_cipher)]

# Take modulo 26 of each element in the add_list
mod_list = [i % 26 for i in add_list]

# Convert the mod_list back to letters
result = decyrpt(mod_list)

# Print the results

print("Message:", message)
print("Key:", key)
print("Cipher Text:", result)
