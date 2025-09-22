#kata
#https://www.codewars.com/kata/5af304892c5061951e0000ce/train/python
card = [
          ['B', 'I', 'N', 'G', 'O'],
          [1, 16, 31, 46, 61],
          [3, 18, 33, 48, 63],
          [5, 20, 'FREE SPACE', 50, 65],
          [7, 22, 37, 52, 67],
          [9, 24, 39, 54, 69]
        ]
# print(card[1:])
a = ['B1', 'I16', 'N31', 'G46', 'O61']
b = ['B1', 'I16', 'N31', 'G46', 'O63']
c = ['B1', 'I16', 'N31', 'G46']
d = ['B1', 'I16', 'N31', 'G46', 'O63', 'O61']

# def bingo(card, numbers):
#     output=0
#     num=list(map(lambda x: int(x[1:]), numbers))
#     print(num)
#     for card1 in card[1:]:
#         print(card1)
#         count=sum(1 for i,j in zip(card1,num) if i==j )
#         output+=count
#     if len(numbers)==4:
#         return output>3
#     return output>4

def bingo(card, numbers):
    # Create a lookup set for fast access
    called = set(numbers)

    # Build a 5x5 boolean grid indicating marked positions
    marked = [[False]*5 for _ in range(5)]
    headers = card[0]

    for r in range(5):
        for c in range(5):
            val = card[r+1][c]
            if val == 'FREE SPACE':
                marked[r][c] = True
            else:
                tile = f"{headers[c]}{val}"
                if tile in called:
                    marked[r][c] = True

    # Check rows
    for row in marked:
        if all(row):
            return True

    # Check columns
    for c in range(5):
        if all(marked[r][c] for r in range(5)):
            return True

    # Check diagonals
    if all(marked[i][i] for i in range(5)):
        return True
    if all(marked[i][4-i] for i in range(5)):
        return True

    return False

print(bingo(card, a))
