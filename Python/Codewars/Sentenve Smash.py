array = ['hello', 'world', 'this', 'is', 'great']
def smash(words):
    sentence = ""
    for word in words:
        sentence = sentence + " " + word
    s = s.strip()
    return sentence

print(smash(array))