print(ord("A"))
print(ord("Z"))
print(chr(68))
print(chr(86))
import sys
for line in sys.stdin:
    # new_word = []
    # for char in line:
    #     if char == ' ':
    #         new_word.append(char)
    #     elif char == '\n':
    #         new_word.append(char)
    #     elif char != 'Z':
    #         number_ascii = ord(char)
    #         new_letter = chr(number_ascii+3)
    #     else:
    #         new_letter = 'C'
    #     new_word.append(new_letter)
    # print(new_word)
    new_word = []
    for char in line:
        if char == ' ':
            new_word.append(' ')
        else:
            number_ascii = ord(char)
            if number_ascii > 87:
                number_ascii = number_ascii-26
            new_letter = chr(number_ascii+3)
            new_word.append(new_letter)
    print(''.join(new_word))

