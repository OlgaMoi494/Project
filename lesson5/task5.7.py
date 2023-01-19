a = 0
b = 1
lst_fib = [a,b]
for _ in range(15):
    temp = a
    a = b
    b = temp + a
    lst_fib.append(b)

print(lst_fib)