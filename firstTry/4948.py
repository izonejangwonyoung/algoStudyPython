import math
import sys
import time

# array=[]
while True:
    count = 0
    n = int(input())
    # start=time.time()
    if n == 0:
        sys.exit(1)
    m = 2 * n
    number = int(math.sqrt(m))
    for i in range(n + 1, m + 1):
        if i == 1:
            continue
        for k in range(2, number + 1):
            # if i in array:
            #     break
            if i % k == 0:  # 소수가 아니라면
                # array.append(i)
                break

        else:
            count += 1

    print(count)
    # print('time:',time.time()-start)
# array = [True for _ in range(0,123456)]
# array[0] = False
# array[1] = False
# for i in range(2, 123456):
#     for j in range(2, 352):
#         if i % j == 0:  ## 소수가 아니라면
#             array[i]=False
#             break
# print(array)
