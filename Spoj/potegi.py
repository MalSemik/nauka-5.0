tests = int(input())
for i in range(tests):
    line = input()
    line = line.split(" ")
    a = int(line[0])
    b = int(line[1])
    result = a ** b
    result = str(result)
    int_result = int(result[-1])
    print(int_result)