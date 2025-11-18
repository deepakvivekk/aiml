def print_board(board): 
    for row in board: 
        print(" | ".join(row)) 
        print("-" * 9) 
def check_winner(board, player): 
# Check rows and columns 
    for i in range(3): 
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)): 
            return True 
        # Check diagonals 
        if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player: 
            return True 
    return False 
def is_board_full(board): 
    return all(board[i][j] != ' ' for i in range(3) for j in range(3)) 
def tic_tac_toe(): 
    board = [[' ' for _ in range(3)] for _ in range(3)] 
    current_player = 'X' 
    while True: 
        print_board(board) 
        print(f"Player {current_player}'s turn.")         
        # Get valid move 
        while True: 
            try: 
                row = int(input("Enter row (0, 1, 2): ")) 
                col = int(input("Enter column (0, 1, 2): ")) 
                if row in range(3) and col in range(3) and board[row][col] == ' ': 
                    break 
                else: 
                    print("Invalid move. Try again.") 
            except ValueError: 
                print("Please enter valid integers.") 
        board[row][col] = current_player 
        if check_winner(board, current_player): 
            print_board(board) 
            print(f"Player {current_player} wins!") 
            break 
        elif is_board_full(board): 
            print_board(board) 
            print("It's a draw!") 
            break        
        # Switch player 
        current_player = 'O' if current_player == 'X' else 'X' 
if __name__ == "__main__": 
    tic_tac_toe() 