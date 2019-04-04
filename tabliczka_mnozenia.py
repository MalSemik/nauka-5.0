list1 = [[i*j for i in range(1,11)]for j in range(1,11)]
for line in list1:
    print(line)

print(f'{50.1:10}','hbhb')

for line in list1:
    for item in line:
        print(f"{item:<4}", end="")
    print("")