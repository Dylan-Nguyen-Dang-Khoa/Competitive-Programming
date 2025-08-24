import sys

def main():
    N = int(sys.stdin.readline().rstrip("\n"))
    comfortability = [int(sys.stdin.readline()) for _ in range(N)]
    comfort_dict = {}
    for comfort in comfortability:
        if comfort in comfort_dict:
            comfort_dict[comfort] += 1
        else:
            comfort_dict[comfort] = 1
    if validity_check(comfort_dict):
        print("YES")
    else:
        print("NO")

def validity_check(dictionary):
    for key in dictionary:
        if dictionary[key] % key:
            return False
    return True

main()

