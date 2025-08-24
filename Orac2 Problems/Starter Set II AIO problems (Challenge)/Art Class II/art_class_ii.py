N = int(input())
x_iths = set()
y_iths = set()
for i in range(N):
    x_ith, y_ith = map(int, input().split())
    x_iths.add(x_ith)
    y_iths.add(y_ith)

area = (max(x_iths) - min(x_iths)) * (max(y_iths) - min(y_iths))
print(area)