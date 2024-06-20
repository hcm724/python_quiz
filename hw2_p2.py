num = 1
while num <= 10000:
    factor_sum = 0
    i = 1
    while i < num:
        if num % i == 0:
            factor_sum += i
        i += 1
    if factor_sum == num:
        print(num)
    num += 1