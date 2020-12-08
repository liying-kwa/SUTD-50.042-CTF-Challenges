from present import *
import string

def square_multiply(a,x,n):
    y = 1
    x_bits = []
    # Convert x to binary in list format, starting with MSB
    x_bits = bin(x)[2:]
    for i in x_bits:
        y = (y * y) % n
        if int(i) == 1:
            y = (y * a) % n
    return y


# 1. Find b where 100 <= b <= 150
g = 2222
p = 1208925819614629174706189
A = 505817375660548445575646
B = 33828968133470676004315
a = 68946

for i in range(100, 151):
    temp = square_multiply(g, i, p)
    if temp == B:
        b = i
#print(b)


# 2. Use b to figure out 80 bit key for present
key = square_multiply(A, b, p)
#print(key.bit_length())


# 3. Decrypt encrypted conversation
ciphertext = open('encryptedConvo', 'rb').read()
cipher = int.from_bytes(ciphertext, 'big')
plaintext = present_inv(cipher, key)
msg = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big').decode('utf-8')
print(msg)
