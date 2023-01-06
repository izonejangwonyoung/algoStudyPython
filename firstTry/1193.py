a = int(input())
temp_answer = 0
for i in range(0, 10000000):
    if (i - 1) * i < 2 * a <= i * (i + 1):
        temp_answer = i
        break

if i % 2 == 0:
    aa = round(a - (i * (i - 1) / 2))
    bb = round(i + 1 - aa)
    print(str(aa)+'/'+str(bb))
else:
    aa = round(a - (i * (i - 1) / 2))
    bb = round(i + 1 - aa)
    print(str(bb)+'/'+str(aa))
