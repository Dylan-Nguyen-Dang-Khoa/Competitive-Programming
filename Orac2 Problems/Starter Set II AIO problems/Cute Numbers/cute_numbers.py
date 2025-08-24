len_number = int(input())
cuteness = 0
for i in range(len_number):
    digits = int(input())
    if digits == 0:
        cuteness += 1
    else:
        cuteness = 0
 
print(cuteness)