def get_width(board):
    board_width = len(board[0])
    return board_width


def create_board(width, height):
    
    if 4 <= width <= 10:
        board_rows = ["".join( '.' * width)]
    elif width < 4:
        board_rows = ["".join( '.' * 4)]
    elif width > 10:
        board_rows = ["".join( '.' * 10)]
    
    if 4 <= height <= 10:
        board = (board_rows * height)
    elif height < 4:
        board = (board_rows * 4)
    elif height > 10:
        board = (board_rows * 10)
        
    return board


def display_board(board):
    
    for board_row in range(len(board), 0, -1): 
        spaced_row = ' '.join(board[board_row - 1])
        print(f"|{spaced_row}|")
    
    board_width = get_width(board)
    
    line_break = list(board_width * "--")
    line_break.pop(-1)
    line_break = "".join(line_break)
    print(f"|{line_break}|")
    
    numbered_columns = []
    for i in range(board_width):
        numbered_columns.append(i)
    
    numbered_columns = ' '.join(map(str, numbered_columns))
    print(f"|{numbered_columns}|")
    

def stage_1(width, height):
    
    board = create_board(width, height)
    
    board = display_board(board)
    
    return board


def is_valid_column(board, column_name):
    
    board_width = get_width(board)
    
    if column_name.isdigit():
        column_index = int(column_name)
        if 0 <= column_index < board_width:
            return True
    
    return False


def next_player(players, current_player):
    
    players = list(players)
    player_index = players.index(current_player)
    player_index = (player_index + 1) % len(players)
    
    current_player = players[player_index]


    return current_player
   
     
def stage_2(width, height):
    
    board = create_board(width, height)
    play_game(board)
    
    
    
def is_valid_move(board, column_name):
    
    column_slice, column_name_int = [], int(column_name)
    
    for row in board:
        if row[column_name_int] == ".":
            column_slice.append(row[column_name_int])
        else:
            column_slice.append("X")
    
    if "." in column_slice:
        return True
    else:
        return False
    
     
def column_contents(board, column_index):
    
    column_slice = []
    
    for row in board:
        column_slice.append(row[column_index])
                 
    return ''.join(column_slice)
    


def get_free_row(board, column_index):
    
    row = column_contents(board, column_index)
    
    if "." in row:
        space_index = row.index(".")
        return space_index
    else:
         return (-1)
       
    
def modify_board(board, column_index, row_index, player):
    
    row = board[row_index]
    
    row = list(row)
    row[column_index] = player
    row = ''.join(row)
    
    board[row_index] = row
    
    return board


def add_piece_to_column(board, player, column_name):

    if column_name == "quit":
        return board
        
    column_name = int(column_name)
    
    row_index = get_free_row(board, column_name)
    
    return modify_board(board, column_name, row_index, player)
    
    

def play_turn(board, player):
    
    counter = 0
    user_input = input(f"Player {player} -- enter the column: ")
        
    while counter != 1:
        if user_input == "quit":
            move = user_input 
            counter += 1
            return move
        
        if user_input.isdigit() == True and is_valid_column(board, user_input) == True:
            if is_valid_move(board, user_input) == True or user_input == "quit":
                counter += 1
                move = user_input      
                return move
                  
        user_input = input(f"Player {player} -- enter the column: ")
        


def stage_3(width, height):
    
    board = create_board(width, height)
    play_game(board)
    
    
def is_full(board):
    
    for i in range(len(board)):
        row = board[i]
        if "." in row:
            return False
    return True

def is_winner(board, player):
    
    for row in board:
        row_length = len(row)
        if ( 4 * player) in row:
            return True
        
    counter, column = 0, []
    
    while counter != row_length:
        
        for row in board:
            row = list(row)
            column.append(row[counter]) 
            
        if (4 * player) in ''.join(column):
            return True
        
        else:
            column.clear()
            counter += 1
        
    return False    



def play_game(board):
        
    user_input, player= "NULL", "X"
    
    while user_input != "quit":
        display_board(board)
        user_input = play_turn(board, player)
        
        if str(user_input).lower().strip() == "quit":
            user_input = "quit" 
            display_board(board)
            return print(f"Result: player {player} quits!")                       
            
        else:
            add_piece_to_column(board, player, user_input)
        
        game_result = is_winner(board, player)
        board_capacity = is_full(board)
        
        if game_result == True:
            display_board(board)
            user_input = "quit"            
            return print(f"Result: player {player} wins!") 
        
        elif board_capacity == True:
            display_board(board)
            user_input = "quit"            
            return print(f"Result: draw")           
        
        else:
            player = next_player("XO", player)
       
        
def main(width=8, height=6):
    
    board = create_board(width, height)
    
    play_game(board)



main()