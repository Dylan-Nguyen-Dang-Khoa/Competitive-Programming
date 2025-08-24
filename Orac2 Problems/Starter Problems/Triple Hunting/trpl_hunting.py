n = int(input())
integers = []
positions = []
int_count = 0
for values in range(n):
    integers.append(int(input()))
for i in enumerate(integers):
    if i[1] % 3 == 0:
        int_count += 1
        positions.append(i[0] + 1)
if int_count != 0:
    print(int_count)
    for i in positions:
        print(i, end=" ")
else:
    print("Nothing here!")

