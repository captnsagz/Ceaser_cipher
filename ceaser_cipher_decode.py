

alpha = {

        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26
}

key = 3
message = "KHOOR PB QDPH LV LEUDKLP"
enc_message = ""
enc = ""
key_list = list(alpha.keys()) 
val_list = list(alpha.values()) 
for i in message:
        if i.isalpha():
                x = i.upper()
                y = alpha[x] - key
                if y < 0:
                        y = y + 26
                        enc = list(alpha.keys())[list(alpha.values()).index(y)]
                        enc_message = enc_message + enc
                else:
                        enc = list(alpha.keys())[list(alpha.values()).index(y)]
                        enc_message = enc_message + enc
        elif i.isspace():
                enc_message = enc_message + " "
print(enc_message)
