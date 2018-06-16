def find_most_frequent(text):
    if len(text) == 0:
        return []
    punc = [',','.',':',';','!','?','-']
    result = {}
    for sign in punc:
        text = text.replace(sign," ")
    text= text.lower().split()
    words = {}
    for word in text:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1
    for word, count in words.items():
        if count in result.keys():
            result[count].append(word)
        else:
            result[count] = [word]
    return((sorted(result[max(result.keys())])))


#
# print(find_most_frequent('Hello,Hello, my dear!'))
print(find_most_frequent(''))
# print(find_most_frequent('to understand recursion you need first to understand recursion...'))
# print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))
#
# print(find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind")
#       )