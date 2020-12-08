# 1. Gather pairs for substitution cipher
substitution = {'A':'8',
                'B':'N',
                'C':'4',
                'D':'I',
                'E':'R',
                'F':'1',
                'G':'A',
                'H':'M',
                'I':'C',
                'J':'6',
                'K':'9',
                'L':'F',
                'M':'U',
                'N':'E',
                'O':'2',
                'P':'L',
                'Q':'G',
                'R':'H',
                'S':'Y',
                'T':'S',
                'U':'D',
                'V':'W',
                'W':'V',
                'X':'J',
                'Y':'T',
                'Z':'O',
                '0':'5',
                '1':'B',
                '2':'0',
                '3':'X',
                '4':'7',
                '5':'Q',
                '6':'3',
                '7':'P',
                '8':'K',
                '9':'Z'}

# 2. Carry out reverse substitution on ciphertext (envelope contents)
reverse_substitution = {}
for key in substitution:
    value = substitution[key]
    reverse_substitution[value] = key
ciphertext = 'IE4E4E4I44IIIEI44IEESY4Y4Y4S44SSSYS44SYYX055505X55BXB0B55B5075BBB5B7BB57555BB5B5IIIEIIIIEINININEINEISSSRSSSSRSLSLSLRSLRS0BB5BBB05B505B55B55B3Q0X0Q03Q0333Q3Q03XQ8YYYYY8YY8Y8Y88YY8YY5555555B55555B55555555BB55B5BBBB55BB5BB5BB55BB555555B555B55B'
midtext = ''
for letter in ciphertext:
    midtext += reverse_substitution[letter]
print(midtext)


# 3. Do transposition. See solution.txt

# 4. Decrypt image using key from previous part to get flag.


