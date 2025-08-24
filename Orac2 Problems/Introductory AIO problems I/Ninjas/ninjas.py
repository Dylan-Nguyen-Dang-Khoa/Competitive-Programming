import math
N, K = map(int, input().split())
answer = N - ((N // (K + 1)) + 1) if N % (K + 1) != 0 else N - (N // (K + 1))
print(answer)




