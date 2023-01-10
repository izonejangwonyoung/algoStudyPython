# def quick_sort(array):
#     # 리스트가 하나 이하의 원소를 가지면 종료
#     if len(array) <= 1: return array
#
#     pivot, tail = len(array[0]), len(array[1:])
#
#     left_side = [x for x in tail if x <= pivot]
#
#     right_side = [x for x in tail if x > pivot]
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
#
# n = int(input())
#
# a = []
# for i in range(n):
#     a.append(input())
#
# print(a)
# print(len(a[0]))
# length = []
# b=quick_sort(a)
# print(b)

# not my code
import sys

# N: 데이터 개수
N = int(sys.stdin.readline().rstrip())

array = []
for i in range(N):
    array.append(sys.stdin.readline().rstrip())

array = list(set(array))
array = sorted(array, key=lambda x: (len(x), x))

for i in range(len(array)):
    print(array[i])
