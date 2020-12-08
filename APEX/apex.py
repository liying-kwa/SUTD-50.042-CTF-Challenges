# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:51:25 2020

@author: Jo-Shen
"""

import string

if __name__ == "__main__":
    ciphertext = ":OW+iW-b&VQ6$(HUcqhepd8fficffcrgeof8jfio88pp8ok6gd4"
    key = "WHOSYOURMOMMY"
    numbers = []
    a = string.printable
    b =[]
    for letter in ciphertext:
        numbers.append(a.find(letter))
    print(numbers)
    for x in range(4):
        for letter in key:
            b.append(a.find(letter))
    print(b)
    shifted = []
    for i in range(len(numbers)):
        shift = (numbers[i]-b[i])%len(a) + string.printable.find("a")
        shifted.append(shift)
    print(shifted)
    final = ""
    c = ""
    for i in shifted:
        #print(i)
        #print(string.printable[i])
        final += string.printable[i]
        #print(final)
        c += str(i)
    print(final)
    #print(c)
    
    numbers = [76, 77, 68, 82, 75, 68, 77, 77, 68, 64, 82, 75, 68, 77, 76, 68, 81, 77, 68, 81, 77, 68, 76, 75, 68, 81, 75, 68, 78, 77, 68, 76, 75, 66]
    mod = 74
    #numbers = [str(x%mod) if x&mod>=0 and x%mod<=10 else str(x) for x in numbers]
    numbers = [str(x%mod) if x&mod>=0 and x%mod<=10 else " " for x in numbers]
    print(numbers)
    print("".join(numbers))