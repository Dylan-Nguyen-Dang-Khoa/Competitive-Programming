L = int(input())
X = int(input())
Y = int(input())


route1 = X + Y
route2 = L * 2 - route1
print(min(route1, route2))