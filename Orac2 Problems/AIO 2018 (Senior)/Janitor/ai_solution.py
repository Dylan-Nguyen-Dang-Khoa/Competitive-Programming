import sys
input = sys.stdin.readline

def main():
    R, C, Q = map(int, input().split())
    H = [list(map(int, input().split())) for _ in range(R)]
    
    # Directions: north, south, west, east
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # Check if (r,c) is a peak (no neighbour higher than it)
    def is_peak(r, c):
        h = H[r][c]
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and H[nr][nc] > h:
                return False
        return True

    # Build initial is_peak array and count
    is_pk = [[False]*C for _ in range(R)]
    peak_count = 0
    for i in range(R):
        for j in range(C):
            if is_peak(i,j):
                is_pk[i][j] = True
                peak_count += 1

    # Output helper
    out = []
    out.append(str(peak_count))

    # Process each replacement
    for _ in range(Q):
        r, c, new_h = map(int, input().split())
        r -= 1
        c -= 1
        
        # Collect this tile and its neighbours
        cells = [(r,c)]
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                cells.append((nr,nc))
        
        # Remove their old contributions
        for i,j in cells:
            if is_pk[i][j]:
                peak_count -= 1
            is_pk[i][j] = False
        
        # Apply the height change
        H[r][c] = new_h
        
        # Recompute peaks among affected cells
        for i,j in cells:
            if is_peak(i,j):
                is_pk[i][j] = True
                peak_count += 1
        
        out.append(str(peak_count))

    # Print all answers
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
