with open('test.txt', 'r') as f:
    lines = [l.rstrip() for l in f]

def calc_seat(line):
    row = line[0:7]
    row_start = 0
    row_end = 127
    for c in row:
        half = (row_start+row_end)/2
        if c == 'F':
            row_end = int(half-0.5)
        if c == 'B':
            row_start = int(half+0.5)

    col = line[7:10]
    col_start = 0
    col_end = 7
    for c in col:
        half = (col_start+col_end)/2
        if c == 'L':
            col_end = int(half-0.5)
        if c == 'R':
            col_start = int(half+0.5)
    
    seat = (row_start * 8) + col_start

    return line, row_start, col_start, seat


def highest_seat_id(seats):
    return max([seat[-1] for seat in seats])

test_seats = [calc_seat(line) for line in lines]
assert(
    test_seats == [
        ('FBFBBFFRLR', 44, 5, 357),
        ('BFFFBBFRRR', 70, 7, 567),
        ('FFFBBBFRRR', 14, 7, 119),
        ('BBFFBBFRLL', 102, 4, 820)
    ]
)
assert(highest_seat_id(test_seats) == 820)