#kata
#https://www.codewars.com/kata/691ca4c58c5f7e662d508d31/train/python

def find_saddle_points(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    col_max = [max(matrix[r][c] for r in range(rows)) for c in range(cols)]
    for r in range(rows):
        row_min = min(matrix[r])
        for c in range(cols):
            if matrix[r][c] == row_min and matrix[r][c] == col_max[c]:
                result.append((r, c))
    return result

