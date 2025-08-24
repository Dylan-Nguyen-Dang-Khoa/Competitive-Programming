t = int(input())
denominations = [100, 20, 5, 1]
notes = 0

for i in denominations:
    notes += t // i
    t = t % i
print(notes)




