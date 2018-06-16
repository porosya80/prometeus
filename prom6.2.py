morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."

}
radio_code = {
    ".": "^",
    "-": "^^^",
    " ": "_______"
}

def encode_radio(chr):
    result = []
    for _ in morse_code[chr]:
        result.append(radio_code[_])
    return "_".join(result)


def encode_morze(text):
    result = []
    word = []
    text = text.upper().split()
    for word in text:

        wordres =[]
        for chr in word:
            if chr not in morse_code.keys():
                continue
            wordres.append(encode_radio(chr))
        result.append('___'.join(wordres))
    return '_______'.join(result)


print(encode_morze("6"))
# print(encode_radio('S'))
