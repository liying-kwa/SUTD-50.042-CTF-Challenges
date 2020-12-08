import hashlib


# 1. Prove that something has been changed in the zip folder
checksum = '55261c371ddfba51a1d62b0d4d05a485'
content = open('CyberSecurityAct.zip', 'rb').read()
md5_hash = hashlib.md5()
md5_hash.update(content)
digest = md5_hash.hexdigest()
print(digest)