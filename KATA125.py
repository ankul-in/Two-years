#kata
#https://www.codewars.com/kata/5b5736abf1d553f844000050/train/python
def possible_positions(pos):
    x=ord(pos[0])
    y=int(pos[1])
    moves=[(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if ord('a') <= nx <= ord('h') and 1 <= ny <= 8:
            result.append(chr(nx) + str(ny))

    return sorted(result)
print(possible_positions("d5"))