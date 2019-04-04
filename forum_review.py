# import linecache
#
# i = 1
# while i <= 200:
#     x = linecache.getline('hasla.txt', i)
#     y = x.strip()
#     if y == y[::-1]:
#         print(y)
#     i = i + 1


with open('hasla.txt' ,'r') as file:
    lines = file.readlines()
    for l in lines:
        l = l.strip()
        if l == l[::-1]:
            print(l)
