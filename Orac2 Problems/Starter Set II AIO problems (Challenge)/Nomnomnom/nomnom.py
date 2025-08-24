import sys

N = int(sys.stdin.readline())
weight_of_last_hippo = int(sys.stdin.readline())
food_eaten = 0
weight_eaten = 0
satisfied = 1
for i in range(N-1):
    food_eaten += int(sys.stdin.readline())
    if food_eaten >= weight_of_last_hippo:
        weight_of_last_hippo = food_eaten
        food_eaten = 0
        satisfied += 1

print(satisfied)


    

    
