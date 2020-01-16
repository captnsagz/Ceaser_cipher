import sys
import subprocess

subprocess.call("cls",shell="True")

if len(sys.argv) < 3:
        print("[!]Usage: python <filename.py> <string to convert> <key>")
        sys.exit(1)


message = sys.argv[1]
key = int(sys.argv[2])
new_char = ""
enc_message = ""
print("Message to encrypt: "+message)
for char in message:
        if char.isalpha():
                new_char = ord(char.lower())+key
                if new_char >= 122:
                        new_char = new_char - 26
                        enc_message = enc_message + chr(new_char)
                else:
                        new_char = ord(char) + key
                        enc_message = enc_message + chr(new_char)
        else:
                enc_message = enc_message + char
print("Encrypted message: "+enc_message)
                
