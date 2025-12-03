def sum_nat(n):
    sum = 0
    if n==0:
        print('The sum is zero')
    else:
        for i in range(1,n+1):
            sum+=i
        print(sum)
sum_nat(10)
