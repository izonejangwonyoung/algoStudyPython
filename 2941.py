# import re
# croa_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# arrayman = []
# value = input().lower()
# count = 0
#
# for i in range(0, len(croa_alphabet)):
#     for a in re.finditer(croa_alphabet[i], value):
#         arrayman.append(croa_alphabet[i])
#
# if arrayman.count('dz=') > 0:
#     result = len(arrayman) - arrayman.count('dz=')
#     realresult = len(value) - (arrayman.count('dz=') * 3 + (arrayman.count('z=') - arrayman.count('dz=')) * 2)
#     print(realresult)
#     answer = realresult + arrayman.count('dz=') + (arrayman.count('z=') - arrayman.count('dz='))
#     print(answer)
# else:
#     result = len(value) - len(arrayman)
#     print(result)
croa_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
arrayman = []
value = input().lower()
count = 0


for i in croa_alphabet:
    value=value.replace(i,'*')

print(len(value))