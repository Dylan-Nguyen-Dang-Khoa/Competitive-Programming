import sys

R, S = map(int, sys.stdin.readline().split())
rose_cards = [int(sys.stdin.readline()) for _ in range(R)]
scarlet_cards = [int(sys.stdin.readline()) for _ in range(S)]
rose_cards_frequency = {}
num_pairs = 0
for card in rose_cards:
    if card in rose_cards_frequency:
        rose_cards_frequency[card] += 1
    else:
        rose_cards_frequency[card] = 1
for card in scarlet_cards:
    if card in rose_cards_frequency:
        num_pairs += rose_cards_frequency[card]

print(num_pairs)


