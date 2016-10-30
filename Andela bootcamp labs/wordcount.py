def words(sentence):
    d = {}
    for word in sentence.split():
        word = int(word) if word.isdigit() else word
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d