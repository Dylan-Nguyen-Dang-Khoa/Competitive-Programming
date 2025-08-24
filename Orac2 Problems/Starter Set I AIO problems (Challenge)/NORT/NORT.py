W, H = map(int, input().split())

if H % 2 == 0 or W % 2 == 0:
    print(W * H)
else:
    print(W * H - 1)