with open('test.txt', 'r') as f:
    grid = [[c for c in l.rstrip()] for l in f]

print("\n".join([''.join(row) for row in grid]))

def count(move_x, move_y, search, grid):
    found = 0
    for i in range(len(grid)):
        current_x = 0 + (move_x*i)
        current_x %= len(grid[i])
        current_y = 0 + (move_y*i)
        if current_y <= len(grid) and grid[current_y][current_x] == search:
            found += 1
    return found

def count_by_sequences(sequences, search, grid):
    total = 0
    for sequence in sequences:
        result = max(1, count(*sequence, search, grid))
        if total == 0:
            total = result
        else:
            total *= result
    return total

assert(count_by_sequences([(3, 1)], '#', grid) == 7)

with open('data.txt', 'r') as f:
    grid = [[c for c in l.rstrip()] for l in f]

print('part 1', count_by_sequences([(3, 1)], '#', grid))
print('part 2', count_by_sequences([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)], '#', grid))