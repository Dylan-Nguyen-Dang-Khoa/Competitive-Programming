n, c = map(int, input().split())
rainfall_amounts = []
volume_water = 0
days = 0
index = 0
for i in range(n):
    rainfall_amounts.append(int(input()))

while volume_water < c:
    days += 1
    volume_water += rainfall_amounts[index]
    index += 1
print(days)
