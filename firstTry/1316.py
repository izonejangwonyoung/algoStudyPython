# import re
#
# value_number = int(input())
# a = []
# arrayman = []
# count = 0
# realcount=0
# for i in range(0, value_number):
#     temp = input()
#     a.append(temp)
# print(a)
# print(a[0])
# for i in range(0,len(a)):  #리스트의 몇 번쨰 단어를 픽할건지
#     templist=sorted(set(a[i]))
#     print(templist)
#     for j in range(len(templist)):            #templist에는 픽한 단어의 구성 알파벳이 중복이 제거된채로 들어가있음. 픽한 단어의 각 알파벳마다 돌아가면서감
#         print(templist[j])    # a  h   p   y 식으로 줄력
#         for c in re.finditer(templist[j],a[i]):
#             arrayman.append(c.start())
#
#         print(arrayman)
#         print(len(arrayman))
#         if len(arrayman)%2==0:  #어레이맨 속 개수가 짝수개일떄
#
#         else:
#
#
#
#
#         arrayman.clear()
#
#
#
#
#
# print(arrayman)
#

#
# for i in range(0, len(a)):
#     for k in range(0, len(a[i])):
#         for c in re.finditer(a[i][k], a[i]):
#             arrayman.append(c.start())
#             print(arrayman, a[i], a[i][k])
#         for j in range(0, len(arrayman)):
#             for l in range(0, len(arrayman)):
#                 if abs(arrayman[j] - arrayman[l]) != 1:
#                     count += 1
#
#         if count != 0:
#             realcount += 1
#             count = 0
#             print('realcount가 하나 증가했음')
#
#         arrayman.clear()
#     #         if abs(k - arrayman[0]) > 1:
#     #             arrayman.clear()
#     #             break
#     #     break
#     # count+=1
#     # print('현재 카운트는',count)
#
# print(arrayman)
# print(count)
# print(realcount)





#####최종 답안#####
# result = 0
# for i in range(int(input())):
#     word = input()
#     print(sorted(word,key=word.find))
#     print(list(word))
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)




N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+2:]:           ###a in b  => b에 a가 포함되어있니??
            cnt -= 1
            print(word[j],'에서',word[j+2])
            break

print(cnt)