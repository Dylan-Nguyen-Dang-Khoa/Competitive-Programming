
fruit_no = int(input())
full_moon_count = 0

while fruit_no % 11 != 1:
    full_moon_count +=1
    fruit_no *= 2
print(full_moon_count, fruit_no)