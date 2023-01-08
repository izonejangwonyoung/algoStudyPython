# n, m = map(int, input().split())
#
# list1 = [[0 for _ in range(n)] for _ in range(m)]
# for i in range(n):
#     list1[i] = (list(map(int, input().split())))
# list2 = [[0 for _ in range(n)] for _ in range(m)]
# for i in range(n):
#     list2[i] = (list(map(int, input().split())))
# # print('list1=',list1)
# # print('list2=',list2)
# # print('total=',total)
# for i in range(0, n):
#     for j in range(0, m):
#         list1[i][j] += list2[i][j]
#         print(list1[i][j], end=" ")
#     print()
n, m = map(int, input().split())

# list1 = [[0 for i in range(n)] for j in range(m)]
# list2 = [[0 for i in range(n)] for j in range(m)]
list1 = []
list2 = []
for i in range(n):
    list1.append(list(map(int, input().split())))
for i in range(n):
    list2.append(list(map(int, input().split())))
for i in range(0, n):
    for j in range(0, m):
        list1[i][j] += list2[i][j]
        print(list1[i][j], end=" ")
    print()
