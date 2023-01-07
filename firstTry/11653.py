n = int(input())
array = []
i=2
if n==1:
    pass
else:
    while n != 1:
        if n % i == 0:   #i의 값이 인수인 경우
            # print('hello')
            array.append(i)
            n = n / i
            # print(n)
        else:            #인수가 아닌 경우
            # print('here')
            # print(i)
            i = 1 + i

    for i in range(len(array)):
        print(array[i])
