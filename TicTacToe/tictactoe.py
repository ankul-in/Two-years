def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
def check_win(board):
    win_condition=[(0,1,2),(0,3,6),(0,4,8),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(2,4,6)]
    for condition in win_condition:
        if board[condition[0]]==board[condition[1]]==board[condition[2]]!="":
            return board[condition[0]]
    if "" not in board:
        return "Tie"
    return False
def play_game():
    board=[""]*9
    current_player="X"
    while True:
        print_board(board)
        move=input(f"Player{current_player},enter your move(1-9):")
        if board[int(move)-1]!="":
            print("invalidMove,Try again")
            continue
        board[int(move)-1]=current_player
        result=check_win(board)
        if  result:
            print_board(board)
            if result=="Tie":
                print("Its a Tie")
            else:
                print(f"Player {result} wins!!")
            break
        current_player="O" if current_player=="X" else "X"
play_game()