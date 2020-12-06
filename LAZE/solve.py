key='IE4E4E4I44IIIEI44IEESY4Y4Y4S44SSSYS44SYYX055505X55BXB0B55B5075BBB5B7BB575\
55BB5B5IIIEIIIIEINININEINEISSSRSSSSRSLSLSLRSLRS0BB5BBB05B505B55B55B3Q0X0Q\
03Q0333Q3Q03XQ8YYYYY8YY8Y8Y88YY8YY5555555B55555B55555555BB55B5BBBB55B\
B5BB5BB55BB555555B555B55B'

print(len(key))

#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS
# Author : Wong Tin Kit
# Student ID : 1003331

import present as present
import argparse
import binascii

nokeybits=80
blocksize=64


def ecb(infile,outfile,keyfile,mode):
    infile = open(infile, 'rb')
    outfile = open(outfile, 'wb')
    keyfile = open(keyfile, 'r')
    key = int(keyfile.readline(),16)
    keyfile.close()
    
    while True:
        chunk = infile.read(8)
        if len(chunk) == 0:
            break
        else:
            if mode == 'e':
                chunk = int.from_bytes(chunk, 'big')
                cipher = present.present(chunk,key) 
                outfile.write(cipher.to_bytes(8,'big'))
            elif mode == 'd':
                chunk = int.from_bytes(chunk, 'big')
                plaintext = present.present_inv(chunk,key)
                outfile.write(plaintext.to_bytes(8,'big'))

    infile.close()
    outfile.close()
    keyfile.close()    

    

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode',choices=['e', 'd'])

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode=args.mode
    
    ecb(infile,outfile,keyfile,mode)



