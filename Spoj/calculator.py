import sys

for line in sys.stdin:
    inserted_line = line.split()
    sign = inserted_line[0]
    a = int(inserted_line[1])
    b = int(inserted_line[2])
    if sign == "+":
        print(a + b)
    elif sign == "-":
        print(a - b)
    elif sign == "*":
        print(a * b)
    elif sign == "/":
        print(a // b)
    elif sign == "%":
        print(a % b)
    elif sign == "//":
        print(a // b)
    elif sign == "**":
        print(a ** b)
