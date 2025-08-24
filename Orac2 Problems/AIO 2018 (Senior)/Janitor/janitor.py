# Actual AIO problem solution

def tile_check(tiles, tile_row, tile_column):
    number_of_tiles_higher = 0
    if tile_column + 1 < C:
        if tiles[tile_row][tile_column] < tiles[tile_row][tile_column + 1]:
            number_of_tiles_higher += 1 
    if tile_column != 0:
        if tiles[tile_row][tile_column] < tiles[tile_row][tile_column - 1]:
            number_of_tiles_higher += 1
    if tile_row + 1 < R:
        if tiles[tile_row][tile_column] < tiles[tile_row + 1][tile_column]:
            number_of_tiles_higher += 1
    if tile_row != 0:
        if tiles[tile_row][tile_column] < tiles[tile_row - 1][tile_column]:
            number_of_tiles_higher += 1
    return number_of_tiles_higher
    
answer = 0
tiles = []
tile_changes = []
tiles_higher_count = []
R, C, Q = list(map(int, input().split()))
for _ in range(R):
    tiles.append(list(map(int, input().split())))
for _ in range(Q):
    tile_changes.append(list(map(int, input().split())))
for tile_row in range(R):
    temp_row = []
    for tile_column in range(C):
        if (tiles_higher := tile_check(tiles, tile_row, tile_column)) == 0:
            answer += 1
        temp_row.append(tiles_higher)
    tiles_higher_count.append(temp_row)

        
            
print(answer)
for changes in tile_changes:
    tile_row = changes[0] - 1
    tile_column = changes[1] - 1
    tiles[tile_row][tile_column] = changes[2]
    old_tiles_higher = tiles_higher_count[tile_row][tile_column]
    tiles_higher_count[tile_row][tile_column] = tile_check(tiles, tile_row, tile_column)
    if old_tiles_higher == 0 and tiles_higher_count[tile_row][tile_column] > 0:
        answer -= 1
    elif old_tiles_higher > 0 and tiles_higher_count[tile_row][tile_column] == 0 :
        answer += 1
    if tile_column + 1 < C:
        old_tiles_higher = tiles_higher_count[tile_row][tile_column + 1]
        tiles_higher_count[tile_row][tile_column + 1] = tile_check(tiles, tile_row, tile_column + 1)
        if old_tiles_higher == 0 and tiles_higher_count[tile_row][tile_column + 1] > 0:
            answer -= 1
        elif old_tiles_higher > 0 and tiles_higher_count[tile_row][tile_column + 1] == 0 :
            answer += 1
    if tile_column != 0:
        old_tiles_higher = tiles_higher_count[tile_row][tile_column - 1]
        tiles_higher_count[tile_row][tile_column - 1] = tile_check(tiles, tile_row, tile_column - 1)
        if old_tiles_higher == 0 and tiles_higher_count[tile_row][tile_column - 1] > 0:
            answer -= 1
        elif old_tiles_higher > 0 and tiles_higher_count[tile_row][tile_column - 1] == 0 :
            answer += 1
    if tile_row + 1 < R:
        old_tiles_higher = tiles_higher_count[tile_row + 1][tile_column]
        tiles_higher_count[tile_row + 1][tile_column] = tile_check(tiles, tile_row + 1, tile_column)
        if old_tiles_higher == 0 and tiles_higher_count[tile_row + 1][tile_column] > 0:
            answer -= 1
        elif old_tiles_higher > 0 and tiles_higher_count[tile_row + 1][tile_column] == 0 :
            answer += 1
    if tile_row != 0:
        old_tiles_higher = tiles_higher_count[tile_row - 1][tile_column]
        tiles_higher_count[tile_row - 1][tile_column] = tile_check(tiles, tile_row - 1, tile_column)
        if old_tiles_higher == 0 and tiles_higher_count[tile_row - 1][tile_column] > 0:
            answer -= 1
        elif old_tiles_higher > 0 and tiles_higher_count[tile_row - 1][tile_column] == 0 :
            answer += 1
    print(answer)

    
        
        


    
                    
"""
5 3 2 0 
4 8 4 3
5 7 6 1
"""