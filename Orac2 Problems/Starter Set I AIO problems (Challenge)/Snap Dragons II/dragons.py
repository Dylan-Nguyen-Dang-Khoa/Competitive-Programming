R, C, rose_row, rose_column, scarlet_row, scarlet_column = map(int, input().split())

distance_between = abs(rose_row - scarlet_row) + abs(rose_column - scarlet_column)


if distance_between % 2 == 0:
    print("SCARLET")
else:
    print("ROSE")
