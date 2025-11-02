#kata
#https://www.codewars.com/kata/56242b89689c35449b000059/train/python

def chess_board(rows, columns):
    board = []
    for r in range(rows):
        row = []
        for c in range(columns):
            cell = 'O' if (r + c) % 2 == 0 else 'X'
            row.append(cell)
        board.append(row)
    return board

