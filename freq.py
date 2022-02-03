import os
import pprint

dictionary = {}
def count(elements):

    # if there exists a key as "elements" then simply
    # increase its value.
    if elements in dictionary:
        dictionary[elements] += 1

    # if the dictionary does not have the key as "elements"
    # then create a key "elements" and assign its value to 1.
    else:
        dictionary.update({elements: 1})


   
# Declare a dictionary

def remove_unw2anted(str):
    str = ''.join([c for c in str if c in 'ABCDEFGHIJKLNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\''])
    return str
def clean(word):
    word = remove_unw2anted(word)
    return word.lower()


   



# iterate over files in
# that directory
for filename in os.listdir('pages'):
    f = os.path.join('pages', filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f, "r") as file:
            str = file.read()
            str = str.split()
            for item in str:
                item = clean(item)
                count(item)

file = open('word_freq.txt', 'w')
for w in sorted(dictionary, key=dictionary.get, reverse=True):
    file.write(f'{w}, {dictionary[w]}\n')