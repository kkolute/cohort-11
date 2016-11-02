'''
author : Kennedy kolute
class  : Andela bootcamp 11
'''
def words(sentence):
# initialize an empty dictionary
    d = {}
	# loop through the elements in the sentence separated by white space
    for word in sentence.split():
	# separate word and digits while looping and store them in variable word
        word = int(word) if word.isdigit() else word
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
#return elements in the dictionary
    return d