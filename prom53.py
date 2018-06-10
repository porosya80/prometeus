def super_fibonacci(n, m):
    # if n < m:
    #     return 1

    fibo = [1 for i in range(m)]

    for i in range(0, n):
        fibo.append(sum(fibo[i:i+m]))






    # print (fibo[n-1])



    # a = 1
    # b = 0
    # while n >= 0:
    #     n -= 1
    #     tmp = b
    #     b += a
    #     a = tmp
    #     print (a, end = " ")
    # print()
    return fibo[n-1]

print(super_fibonacci(2,1))