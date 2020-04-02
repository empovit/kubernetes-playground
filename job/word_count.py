import string
import sys

word_count = {}
to_remove = string.punctuation + string.whitespace
separators = str.maketrans(dict.fromkeys(to_remove, len(to_remove) * ' '))


def count_words(line):
    for token in line.translate(separators).split():

        token = token.lower()
        if word_count.get(token):
            word_count[token] += 1
        else:
            word_count[token] = 1


with open(sys.argv[1], 'r') as f:
    for file_line in f:
        count_words(file_line)

    print(word_count)
