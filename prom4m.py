import sys

encode = str((sys.argv[1]))
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
str5 = []
stra = []
encode =(''.join(encode.split()))
result = ""

length = len(encode) - len(encode)% 5

for i in range(0,length,5):
    str5.append(encode[i:i+5])

for i in str5:
    word = ""
    for j in i:

        if j.islower():
            word  += "a"
        if j.isupper():
            word += "b"
    stra.append(word)

for i in stra:
    letter_pos = key.find(i)
    result += alphabet[letter_pos]

print(result)

