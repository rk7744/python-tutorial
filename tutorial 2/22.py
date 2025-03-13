# 22. Program to read a string and remove the given words from the string.
def remove_words(sentence, words_to_remove):
    for word in words_to_remove:
        sentence = sentence.replace(word, '')
    return sentence.strip()
print(remove_words("Hello world, welcome to Python!", ["world", "Python"]))