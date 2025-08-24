f = int(input())
friend_amts = {}
for i in range(f):
    a, b = map(int, input().split())
    if a in friend_amts:
        friend_amts[a] += 1
    else:
        friend_amts[a] = 1
    if b in friend_amts:
        friend_amts[b] += 1
    else:
        friend_amts[b] = 1
max_amt = max(friend_amts.values())
ender = True
winners = []
while ender:
    if friend_amts[max(friend_amts, key=friend_amts.get)] == max_amt:
        winners.append(max(friend_amts, key=friend_amts.get))
        friend_amts[max(friend_amts, key=friend_amts.get)] = 0
    else:
        ender = False
winners.sort()
for i in winners:
    print(i)

