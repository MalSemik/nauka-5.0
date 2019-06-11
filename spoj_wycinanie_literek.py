import sys

for line in sys.stdin:
    line = line.split()
    letter, word = line
    new_word = word.replace(letter, "")
    print(new_word)
