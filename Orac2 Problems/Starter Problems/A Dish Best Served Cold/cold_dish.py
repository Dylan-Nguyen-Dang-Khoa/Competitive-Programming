n = int(input())
list_of_n = []
for i in range(n):
    list_of_n.append(int(input()))
print(min(list_of_n), max(list_of_n), sum(list_of_n)//n)