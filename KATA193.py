#kata
#https://www.codewars.com/kata/5592fc599a7f40adac0000a8/train/python

matrix=[
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

def sum_diagonals(matrix):
    n=len(matrix)
    answer=[]
    for i in range(n):
        answer.append(matrix[i][i])
        answer.append(matrix[i][n-1-i])
    return sum(answer)
matrix = [[-2,5,3,2],
          [9,-6,5,1],
          [3,2,7,3],
          [-1,8,-4,8]]


print(sum_diagonals(matrix))

# def sum_diagonals(matrix):
#     n = len(matrix)
#     return sum(matrix[i][i] + matrix[i][n - 1 - i] for i in range(n)) - (matrix[n // 2][n // 2] if n % 2 == 1 else 0)