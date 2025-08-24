import sys

data = sys.stdin.read().removesuffix("\n").split("\n")
D, T = map(int, data.pop(0).split())
dancer_hula_hoops = {dancer + 1: 0 for dancer in range(D)}
min_hula_hoops = 0
for throw in range(len(data)):
    thrower, receiver = map(int, data[throw].split())
    if dancer_hula_hoops[thrower] == 0:
        min_hula_hoops += 1
    else:
        dancer_hula_hoops[thrower] -= 1
    dancer_hula_hoops[receiver] += 1
print(min_hula_hoops)