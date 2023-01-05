import string

most_use_alphabet = input().upper()
word_list = list(set(most_use_alphabet))

cnt = []

for i in word_list:
    count = most_use_alphabet.count
    cnt.append(count(i))
    print(count)
    print('cnt', cnt)

if cnt.count(max(cnt)) > 1:
    print('?')

else:
    print(word_list[(cnt.index(max(cnt)))])
    print(max(cnt))
    print(word_list)