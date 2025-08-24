d, w = map(int, input().split())
dictionary = {}
translations = []
for i in range(d):
    intland, wholeland = map(int, input().split())
    dictionary[intland] = wholeland
for i in range(w):
    translations.append(int(input()))
print()
for translateword in translations:
    if translateword in dictionary:
        print(dictionary[translateword])
    else:
        print("C?")
    