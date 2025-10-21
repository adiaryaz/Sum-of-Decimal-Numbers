n = input()
if "." in n:
    print("NotProceed")
else:
    n = int(n)
    if n <= 0:
        print("NotProceed")
    else:
        decimal_sum = 0
        for _ in range(n):
            num = input()
            if "." in num:
                decimal_sum += float(num)
        print(decimal_sum)