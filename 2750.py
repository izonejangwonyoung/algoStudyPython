number = int(input())
number_list = []

for i in range(number):
    a = int(input())
    number_list.append(a)

listlist=sorted(number_list)
for i in range(number):
    print(listlist[i], sep='\n')
