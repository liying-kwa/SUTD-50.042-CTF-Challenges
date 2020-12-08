import hashlib
import string
import math
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.RFC1751 import english_to_key


# 1. Checking that english private key is correct
rsa_priv_eng = "rue jilt rain crew use hog ram lois rate cake arm hit par otis ante deny few hum pry meet goad dawn hank home own meld argo buoy use hose rep meld cub dade fay he os gate reid dawn flow hue pry lair dad chub hand his par name dan come flow hood rue gash golf crew hand hen ply meek rare cake lea ha ram otto reid dade lap hey ply loge cub crew halo has rep gash did cave flub holt pry lake did come lam huff per lois aqua cave flow her rue gash rays cake fat huge rue gate day cave flow i pry gwen ames deny bash him per gwen des cake barn hat rep otis ammo chub pet hat rue nair cut cake hank hut ply loge ammo coat us hove rob gash gist cave halt hose rep nair real deny barn haw ply name dan dawn arm hal rue otis cut crew pew hap per hole del chub hang hub rue otto glad come law horn rue otis cub cake foal ham rob nair rain deny hand hem rep meek goad come are holm pry holm coy come are he per jill argo cake flow hone pry gust reek come ding hugh rue lois rate come per hoe pry lois coy cave law her own gush ammo deny flub hulk ply meet goes cake pep hint os lain glow deny halt huh rep meld argo buoy hang hem rep holm reed cake per hoof os meet gist dade lea honk rob nail coy dawn dine ha os gush real dawn carl hop pry holt dan chub care han rob meek dan dade cant hour own jill dad cave dint hut par loge cut coat dint her os otto reed buoy van hob pry holm dan dade arm hut os ouch arch crew lam howl per hole amos crew base hem ram lois rate deny arm hire own five glum buoy are has own lola ante buoy bask hit ply lake ammo chub care hulk rob gush army crew fay holt pry hole reid dawn dime hem ram nair ammo cave us huff rep gust cup chub flue honk pry otis cub dawn fay howe ply ouch ames coat foam guy ram jilt ante dade lay hug own loge dad come fee ha os meld amos deny law hire os gush amos dade pew hem rob meet reek come flow hill per ouch aqua chub per hen par flak ammo coat foal hiss own flag glow buoy foal hoot per holt army chub flub ha ram gate goad cake flue ho pry five ante dawn fed hull own jill day dawn card hub per jill glad dawn hank he ply meek glum cave pep holt"
rsa_priv_eng = rsa_priv_eng.upper()
#m = hashlib.md5()
#m.update(rsa_priv_eng.encode('utf-8'))
#rsa_priv_eng_md5 = "fbad4a66f5934fa8f4784f15f1bd7925"
#print(m.hexdigest() == rsa_priv_eng_md5)


# 2. Get private key d and modulus n from english private key and decrypt encrypted_message1.bin to get AES key
rsa_priv_d = int(english_to_key(rsa_priv_eng).decode('utf-8'))
#print(type(rsa_priv))
rsa_pub_read = open('public_key.pem','r').read()
rsa_pub = RSA.importKey(rsa_pub_read)
#print(rsa_priv_d)
rsa_priv = RSA.construct((rsa_pub.n, rsa_pub.e, rsa_priv_d))
oaep = PKCS1_OAEP.new(rsa_priv)
ciphertext = open('encrypted_message1.bin', 'rb').read()
aes_key = oaep.decrypt(ciphertext)
#aes_key = int.from_bytes(aes_key_bytes, 'big')
#print(hex(aes_key))



# 3. Brute force for password. ANSWER = kmusic!
# book = "Thou hast made me endless, such is thy pleasure. This frail vessel thou emptiest again and again, and fillest it ever with fresh life. This little flute of a reed thou hast carried over hills and dales, and hast breathed through it melodies eternally new. At the immortal touch of thy hands my little heart loses its limits in joy and gives birth to utterance ineffable. Thy infinite gifts come to me only on these very small hands of mine. Ages pass, and still thou pourest, and still there is room to fill. When thou commandest me to sing it seems that my heart would break with pride; and I look to thy face, and tears come to my eyes. All that is harsh and dissonant in my life melts into one sweet harmony---and my adoration spreads wings like a glad bird on its flight across the sea. I know thou takest pleasure in my singing. I know that only as a singer I come before thy presence. I touch by the edge of the far-spreading wing of my song thy feet which I could never aspire to reach. Drunk with the joy of singing I forget myself and call thee friend who art my lord. I know not how thou singest, my master! I ever listen in silent amazement. The light of thy music illumines the world. The life breath of thy music runs from sky to sky. The holy stream of thy music breaks through all stony obstacles and rushes on. My heart longs to join in thy song, but vainly struggles for a voice. I would speak, but speech breaks not into song, and I cry out baffled. Ah, thou hast made my heart captive in the endless meshes of thy music, my master! Life of my life, I shall ever try to keep my body pure, knowing that thy living touch is upon all my limbs. I shall ever try to keep all untruths out from my thoughts, knowing that thou art that truth which has kindled the light of reason in my mind. I shall ever try to drive all evils away from my heart and keep my love in flower, knowing that thou hast thy seat in the inmost shrine of my heart. And it shall be my endeavour to reveal thee in my actions, knowing it is thy power gives me strength to act. I ask for a moment's indulgence to sit by thy side. The works that I have in hand I will finish afterwards. Away from the sight of thy face my heart knows no rest nor respite, and my work becomes an endless toil in a shoreless sea of toil. Today the summer has come at my window with its sighs and murmurs; and the bees are plying their minstrelsy at the court of the flowering grove. Now it is time to sit quite, face to face with thee, and to sing dedication of live in this silent and overflowing leisure. Pluck this little flower and take it, delay not! I fear lest it droop and drop into the dust. I may not find a place in thy garland, but honour it with a touch of pain from thy hand and pluck it. I fear lest the day end before I am aware, and the time of offering go by. Though its colour be not deep and its smell be faint, use this flower in thy service and pluck it while there is time. My song has put off her adornments. She has no pride of dress and decoration. Ornaments would mar our union; they would come between thee and me; their jingling would drown thy whispers. My poet's vanity dies in shame before thy sight. O master poet, I have sat down at thy feet. Only let me make my life simple and straight, like a flute of reed for thee to fill with music. The child who is decked with prince's robes and who has jewelled chains round his neck loses all pleasure in his play; his dress hampers him at every step. In fear that it may be frayed, or stained with dust he keeps himself from the world, and is afraid even to move. Mother, it is no gain, thy bondage of finery, if it keeps one shut off from the healthful dust of the earth, if it rob one of the right of entrance to the great fair of common human life. The time that my journey takes is long and the way of it long. I came out on the chariot of the first gleam of light, and pursued my voyage through the wildernesses of worlds leaving my track on many a star and planet. It is the most distant course that comes nearest to thyself, and that training is the most intricate which leads to the utter simplicity of a tune. The traveller has to knock at every alien door to come to his own, and one has to wander through all the outer worlds to reach the innermost shrine at the end. My eyes strayed far and wide before I shut them and said `Here art thou!' The question and the cry `Oh, where?' melt into tears of a thousand streams and deluge the world with the flood of the assurance `I am!'"
# words = book.split()
# password_mac = "34bedb439ebe86ac90e60b43f033dcd6"
# for word in words:
#     for i in string.printable:
#         for j in string.printable:
#             m = hashlib.md5()
#             password = i + word + j
#             m.update(password.encode('utf-8'))
#             password_mac_try = m.hexdigest()
#             if password_mac_try == password_mac:
#                 print("YES!")
#                 break
#         if password_mac_try == password_mac:
#             break
#     if password_mac_try == password_mac:
#         break
# print(password)
# print(m.hexdigest())


# 4. Get IV by MD5 hashing the specific word from the book. Word is 'music'
m = hashlib.md5()
m.update('music'.encode('utf-8'))
IV = m.digest()
#print(IV)


# 5. Use AES key and IV to decrypt encrypted_message2.bin to get flag
aes = AES.new(aes_key, AES.MODE_CBC, IV)
ciphertext2 = open('encrypted_message2.bin', 'rb').read()
flag = aes.decrypt(ciphertext2).decode('utf-8')
print(flag)

