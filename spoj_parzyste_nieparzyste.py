# tests = int(input())
# for i in range(tests):
#     line = input()
#     splitted = line.split(" ")
#     even = splitted[2::2]
#     odd = splitted[1::2]
#     print(" ".join(even+odd))

import sys
my_sum = 0
for line in sys.stdin:
    line = int(line)
    my_sum = my_sum + line
    print(my_sum)