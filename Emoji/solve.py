emoji_string = '😄😁 😃😀 😒😀 😹😀 😁😀 😇😀 😅😂 😶😃 😷😁 😃😀 🙀😀'
decoded_string = ''
istd_course_string = ''
for emoji in emoji_string:
	if emoji != " ": 
		#print(type((emoji.encode('unicode-escape'))))
		decoded_string += emoji.encode('unicode-escape').decode('ASCII')
		istd_course_string += emoji.encode('unicode-escape').decode('ASCII')[-3:] 
	else: 
		decoded_string += " "
		istd_course_string += " "

print(decoded_string)
print()
# \U0001f604\U0001f601 \U0001f603\U0001f600 \U0001f612\U0001f600 \U0001f639\U0001f600 \U0001f601\U0001f600 \U0001f607\U0001f600 \U0001f605\U0001f602 \U0001f636\U0001f603 \U0001f637\U0001f601 \U0001f603\U0001f600 \U0001f640\U0001f600

print("Look at EmojiHint3")
print(istd_course_string)
	

