import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for A Mindbending Scenario
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

r1_x1 = 0
r1_y1 = 0
r1_x2 = 0
r1_y2 = 0
r2_x1 = 0
r2_y1 = 0
r2_x2 = 0
r2_y2 = 0

# Read the input.
r1_x1, r1_y1, r1_x2, r1_y2 = map(int, input().strip().split())
r2_x1, r2_y1, r2_x2, r2_y2 = map(int, input().strip().split())

# TODO: This is where you should compute the answer and store it into the
# variable answer.

area_1 = abs(r1_x2 - r1_x1) * abs(r1_y2 - r1_y1)
area_2 = abs(r2_x2 - r2_x1) * abs(r2_y2 - r2_y1)
max_left = max(r1_x1, r2_x1)
min_right = min(r1_x2, r2_x2)
max_bot = max(r1_y1, r2_y1)
min_top = min(r1_y2, r2_y2)
if max_left < min_right and max_bot < min_top:
    overlapped_area = abs(min_right - max_left) * abs(min_top - max_bot)
else:
    overlapped_area = 0
answer = area_1 + area_2 - overlapped_area



# Write the answer.
print(answer)