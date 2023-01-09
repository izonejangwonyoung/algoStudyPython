from collections import Counter

n = int(input())
a = []
for i in range(n):
    k = int(input())
    a.append(k)


def solvechoibin():
    arrayone=(Counter(a)).most_common(2)
    if len(arrayone)==1:
        return arrayone[0][0]
    if arrayone[0][1]==arrayone[1][1]:
        return arrayone[1][0]
    else:
        return arrayone[0][0]

a.sort()
sansul = (sum(a) / n)
sansul = round(sansul)
jungang = a[int((n-1)/2)]
choibin = solvechoibin()
bumwe = max(a) - min(a)
print(sansul)
print(jungang)
print(choibin)
print(bumwe)
