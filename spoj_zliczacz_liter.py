alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
for i in range(65, 91):
    alphabet.append(chr(i))

tests = int(input())
lines = []
for i in range(tests):
    line = input()
    lines.append(line)
print(lines)
set_lines = lines
letter_counter = []
letters = []
for i in set_lines:
    for letter in i:
        letters.append(letter)

for letter in alphabet:
    counter = letters.count(letter)
    if counter > 0: print(letter, counter)