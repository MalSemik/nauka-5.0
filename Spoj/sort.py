def reverse_sort_without_doubles():
    tests = int(input())
    for i in range(tests):
        line = []
        item = input()
        item = item.split(" ")
        for j in range(len(item)):
            line.append(int(item[j]))
        line.sort(reverse=True)
        newlist = [ii for n, ii in enumerate(line) if ii not in line[:n]]
        for k in range(len(newlist)):
            print(str(newlist[k])+" ", end="")



def rozwiąż_spoj_tablice():
    tests = int(input())
    for i in range(tests):
        items = input()
        items = items.split(" ")
        result = items[-1:0:-1]
        for i in result:
            print(i, end=" ")


rozwiąż_spoj_tablice()
