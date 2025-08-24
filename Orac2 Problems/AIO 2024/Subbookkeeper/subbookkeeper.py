import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Subbookkeeper
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of letters in the word.
N = 0

# word is the word with one missing letter
word = ""

# Read the value of N and the word.
N = int(input().strip())
word = input().strip()

# TODO: This is where you should compute your solution. Store the largest score
# that Rebecca can achieve into the variable answer.

answer = 0
question_position = word.index("?")
word1 = word[:question_position] + word[question_position-1] + word[question_position+1:]
word2 = word[:question_position] + word[(question_position+1) % N] + word[question_position+1:]
adjacent1 = 0
adjacent2 = 0
letter1 = ""
letter2 = ""
for i in range(N):
    if word1[i] == letter1:
        adjacent1 += 1
    else:
        letter1 = word1[i]
    if word2[i] == letter2:
        adjacent2 += 1
    else:
        letter2 = word2[i]
answer = max(adjacent1, adjacent2)

# Write the answer.
print(answer)