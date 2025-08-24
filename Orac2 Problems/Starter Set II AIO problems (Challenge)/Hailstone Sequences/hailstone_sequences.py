import sys
def main():   
    num = int(input())
    print()
    print(hailstone_sequence_len(num))
    while num != 0:
        num = int(input())
        if num != 0:
            print(hailstone_sequence_len(num))

def hailstone_sequence_len(n):
    sequence_length = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
            sequence_length += 1
        else:
            n = n * 3 + 1
            sequence_length += 1
    return sequence_length


main()
    
        


