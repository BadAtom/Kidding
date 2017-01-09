def censor(text, word):
    if len(word) > len(text):
        temp = text
        text = word
        word = temp
    temp = "*" * len(word)
    text = text.replace(word, temp)
    return text

print(censor("hello", "hello, it's me"))