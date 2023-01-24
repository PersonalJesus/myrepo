word = 'asasa'
def check_word(word):
    for i in range(0, int(len(word)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True