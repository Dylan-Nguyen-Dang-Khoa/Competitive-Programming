n = int(input())

d = 0
while not n % 2:
    d += 1
    n /= 2
b = int(n)
print(b, d)

