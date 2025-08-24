N = int(input())
rightest = 0
leftest = float("inf")
for i in range(N):
    resting_spot = int(input())
    if resting_spot > rightest:
        rightest = resting_spot
    if resting_spot < leftest:
        leftest = resting_spot

print(rightest - leftest + 1)



                         
    