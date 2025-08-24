# Template for Palindrome

# Read in the input
N = int(input().strip())
# "readline" also includes the newline marking the end of the line (if there is one).
# We add a .strip() which gets rid of it for us.
line = input().strip()

# Convert the string to a list so we can modify it
line = list(line)

# The characters of the palindrome are line[0], line[1], ..., line[N-1]
# TODO: Solve the problem

alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(int(len(line)/2)):
    if line[i] != line[N-(i+1)]:
        lower_lttr = alphabet[min(alphabet.find(line[i]), alphabet.find(line[N-(i+1)]))]
        change_character_pos = i if line[i] != lower_lttr else N-(i+1)
        line[change_character_pos] = lower_lttr

# Convert back to a string for printing
line = "".join(line)
print(line)