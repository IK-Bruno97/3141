
def Fibo(count):
    if count == 0:
        return 0

    elif count == 1:
        return 1

    else:
        return Fibo(count - 1) + Fibo(count - 2)

n = 10
print([ Fibo(i) for i in range(0, n+1)])

sum = 0
tenp = n
while tenp > 0:
    digit = tenp % 10
    sum += digit ** 3
    tenp //= 10

if n == sum:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")