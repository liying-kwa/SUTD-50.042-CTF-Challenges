import hashlib
import base64
from PIL import Image
'''
1. Prove that something has been changed in the zip folder
checksum = '55261c371ddfba51a1d62b0d4d05a485'
content = open('CyberSecurityAct.zip', 'rb').read()
md5_hash = hashlib.md5()
md5_hash.update(content)
digest = md5_hash.hexdigest()
print(digest)
'''

comment_dict = {}
pageNumber = ['108', '087', '052', '012']
for i in pageNumber:
	filename = 'CyberSecurityAct/cybersecurityact{}.png'.format(i)
	im = Image.open(filename)
	im.load()  # Needed only for .png EXIF data (see citation above)
	comment_dict[i] = im.info['Comment']


#print(comment_dict)
# decode from b64
decoded_list= [base64.b64decode(comment_dict[i].encode()).decode() for i in comment_dict]
print(decoded_list)

# XOR all values inside the list.
print(int(decoded_list[0]) ^ int(decoded_list[1]) ^ int(decoded_list[2]) ^ int(decoded_list[3])) 
ans = 22436606392191067862898321914890413051122050164579179671470593407422318126928784369913201892485362980447337866925160673792266994734727263444211771782683935345403776108564933419714282179314422611440217349895686121874130849570576601776436596049297766908062669265409425079601403159208485382330716718928322025781
hex_ans = 0x1ff366d8cb37f1983f4422326fc528d285f0ce7147681f4e3a0b2b7a9efed070cb4432d649c1513f20622592adda606466721a388a9afc6c91491e3507b4e672eec0ad9c0e53b42f0ae429ba9dc810035aeb3ca94b0f470060e109534204d2f04f0880a28e40f8f7eddc2e50cf1e529b3fb1482fbacf645b3cafe3e3a516d935
ciphertext = 0xa39dc7da5332d6eda9fbc3b6e5793ff002ca8b36aea033a5fc8bf392d7fc7243471b309e632451cbd744c55a84365a74d94c8954e545e767fddf57a824532ed2fd705d77e3e0cc98bc3c7cc26ab8d7e2f123f2965272988039d571c0c42609e31ebb2e59a16171c92de804a4a3e6b50d0d24597b2746c01c3c1e961be1e71598
s = ciphertext ^ hex_ans

print(ciphertext)
XOR_stuff = 0x9f82b703118d6401fac6c99986ce8ed76d37b263ef223b32a539ae4a9cb882b41dcb270fd7eb187f6255558cc097a9f48bec6071a77d797ec4b225a8c4d9838822c6117f5be99611e4c4383fee83a6b28f34f93170cf5c3a7d4ee4f6fd14af22bc44e63a64651e25c0d95ef8f3e3cb8c5edf15fd666ad711d9237ff09cda1398
print(hex(s))

b64 = base64.b64encode(bytes.fromhex(hex(s)[2:])).decode()
print(b64)

