alphabet = 'abc def ghi jkl mno pqrs tuv wxyz'
splited_alphabet = alphabet.split(' ')
value = list(input().lower())
kword=0
# for i in range(splited_alphabet):
#     for k in range(len(splited_alphabet[i])):
#         if
for i in range(0, len(value)):
    for k in range(0, 8):
        for j in range(0, len(splited_alphabet[k])):
            if value[i] == splited_alphabet[k][j]:
                kword= k+kword+3

print(kword)
