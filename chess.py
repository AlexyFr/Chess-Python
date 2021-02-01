#!/usr/bin/env python3

# Update method
def update(cb):
    print( "                                          ")
    print( "                                          ")
    print( "     +-------------------------------+    ")
    print(f"   H | {cb[0][0]} | {cb[0][1]} | {cb[0][2]} | {cb[0][3]} | {cb[0][4]} | {cb[0][5]} | {cb[0][6]} | {cb[0][7]} |    ")
    print( "     |-------------------------------|    ")
    print(f"   G | {cb[1][0]} | {cb[1][1]} | {cb[1][2]} | {cb[1][3]} | {cb[1][4]} | {cb[1][5]} | {cb[1][6]} | {cb[1][7]} |    ")
    print( "     |-------------------------------|    ")
    print(f"   F | {cb[2][0]} | {cb[2][1]} | {cb[2][2]} | {cb[2][3]} | {cb[2][4]} | {cb[2][5]} | {cb[2][6]} | {cb[2][7]} |    ")
    print( "     |-------------------------------|    ")
    print(f"   E | {cb[3][0]} | {cb[3][1]} | {cb[3][2]} | {cb[3][3]} | {cb[3][4]} | {cb[3][5]} | {cb[3][6]} | {cb[3][7]} |    ")
    print( "     |-------------------------------|    ")
    print(f"   D | {cb[4][0]} | {cb[4][1]} | {cb[4][2]} | {cb[4][3]} | {cb[4][4]} | {cb[4][5]} | {cb[4][6]} | {cb[4][7]} |    ")
    print( "     |-------------------------------|    ")
    print(f"   C | {cb[5][0]} | {cb[5][1]} | {cb[5][2]} | {cb[5][3]} | {cb[5][4]} | {cb[5][5]} | {cb[5][6]} | {cb[5][7]} |    ")
    print( "     |-------------------------------|    ")
    print(f"   B | {cb[6][0]} | {cb[6][1]} | {cb[6][2]} | {cb[6][3]} | {cb[6][4]} | {cb[6][5]} | {cb[6][6]} | {cb[6][7]} |    ")
    print( "     |-------------------------------|    ")
    print(f"   A | {cb[7][0]} | {cb[7][1]} | {cb[7][2]} | {cb[7][3]} | {cb[7][4]} | {cb[7][5]} | {cb[7][6]} | {cb[7][7]} |    ")
    print( "     +-------------------------------+    ")
    print( "       1   2   3   4   5   6   7   8      ")
    print( "                                          ")
    print( "                                          ")

# Pawn method
def pawn(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb):
    print("Pawn selected.")
    cb[y_dest_cb][x_dest_cb] = cb[y_start_cb][x_start_cb]
    cb[y_start_cb][x_start_cb] = cb_empty[y_start_cb][x_start_cb]

    return cb

# Rook method
def rook(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb):
    print("Rook selected.")
    cb[y_dest_cb][x_dest_cb] = cb[y_start_cb][x_start_cb]
    cb[y_start_cb][x_start_cb] = cb_empty[y_start_cb][x_start_cb]

    return cb

# Knight method
def knight(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb):
    print("Knight selected.")
    cb[y_dest_cb][x_dest_cb] = cb[y_start_cb][x_start_cb]
    cb[y_start_cb][x_start_cb] = cb_empty[y_start_cb][x_start_cb]

    return cb

# Bishop method
def bishop(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb):
    print("Bishop selected.")
    cb[y_dest_cb][x_dest_cb] = cb[y_start_cb][x_start_cb]
    cb[y_start_cb][x_start_cb] = cb_empty[y_start_cb][x_start_cb]

    return cb

# Queen method
def queen(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb):
    print("Queen selected.")
    cb[y_dest_cb][x_dest_cb] = cb[y_start_cb][x_start_cb]
    cb[y_start_cb][x_start_cb] = cb_empty[y_start_cb][x_start_cb]

    return cb

# King method
def king(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb):
    print("King selected.")
    cb[y_dest_cb][x_dest_cb] = cb[y_start_cb][x_start_cb]
    cb[y_start_cb][x_start_cb] = cb_empty[y_start_cb][x_start_cb]

    return cb

# Empty chessboard
cb_empty = [[],[],[],[],[],[],[],[]]
cb_empty[0] = ["#"," ","#"," ","#"," ","#"," "]
cb_empty[1] = [" ","#"," ","#"," ","#"," ","#"]
cb_empty[2] = ["#"," ","#"," ","#"," ","#"," "]
cb_empty[3] = [" ","#"," ","#"," ","#"," ","#"]
cb_empty[4] = ["#"," ","#"," ","#"," ","#"," "]
cb_empty[5] = [" ","#"," ","#"," ","#"," ","#"]
cb_empty[6] = ["#"," ","#"," ","#"," ","#"," "]
cb_empty[7] = [" ","#"," ","#"," ","#"," ","#"]

# Initialising chessboard
cb = [[],[],[],[],[],[],[],[]]
cb[0] = ["r","n","b","q","k","b","n","r"]
cb[1] = ["p","p","p","p","p","p","p","p"]
cb[2] = ["#"," ","#"," ","#"," ","#"," "]
cb[3] = [" ","#"," ","#"," ","#"," ","#"]
cb[4] = ["#"," ","#"," ","#"," ","#"," "]
cb[5] = [" ","#"," ","#"," ","#"," ","#"]
cb[6] = ["P","P","P","P","P","P","P","P"]
cb[7] = ["R","N","B","Q","K","B","N","R"]

pchar = "PRNBQKprnbqk"
xchar = "12345678"
ychar = "ABCDEFGHabcdefgh"

is_selected = False
white_turn = True
black_turn = False

# First display of the chessboard
update(cb_empty)
update(cb)

# Gameloop
while(True):
    # New turn... No piece selected
    is_selected = False

    cb.reverse()
    cb_empty.reverse()

    while is_selected == False:
        # Waiting piece selecetion and coordinates input
        start_input = input("Select a piece of the board to move it (syntax : (piece)(Y)(X) (ex: PB3)) : ")
        
        while ( len(start_input) != 3 ) or ( start_input[0] not in pchar ) or ( start_input[1] not in ychar ) or ( start_input[2] not in xchar ):
            print("")
            start_input = input("Incorrect input...\nSelect a piece of the board to move it (syntax : (piece)(Y)(X) (ex: PB3)) : ")

        selected_piece = start_input[0]
        y_start = start_input[1]
        x_start = start_input[2]

        # Index of the lists of the chessboard
        y_start_cb = ychar.index(y_start.upper())
        x_start_cb = xchar.index(x_start)

        print(f"Coordinates entered : (X:{x_start_cb};Y:{y_start_cb})")
        print(f"Piece at these coordinates : {cb[y_start_cb][x_start_cb]}")

        if selected_piece == cb[y_start_cb][x_start_cb]:
            is_selected = True

        else:
            print(f"No {selected_piece} found at {y_start}{x_start}")
            is_selected = False

    # Waiting piece destination input
    dest_input = input("Enter the destination of the selected piece (syntax : (Y)(X) (ex : A3)) : ")

    while ( len(dest_input) != 2 ) or ( dest_input[0] not in ychar ) or ( dest_input[1] not in xchar ):
        print("")
        start_input = input("Incorrect input...\nEnter the destination of the selected piece (syntax : (Y)(X) (ex: A3)) : ")

    y_dest = dest_input[0]
    x_dest = dest_input[1]

    # Index for the lists of the chessboard
    y_dest_cb = ychar.index(y_dest.upper())
    x_dest_cb = xchar.index(x_dest)

    print(f"Coordinates entered : (X:{x_dest_cb};Y:{y_dest_cb})")

    # Searching method to use for the piece
    if selected_piece == "P" or selected_piece == "p":
        cb = pawn(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb)

    elif selected_piece == "R" or selected_piece == "r":
        rook(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb)

    elif selected_piece == "N" or selected_piece == "n":
        knight(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb)

    elif selected_piece == "B" or selected_piece == "b":
        bishop(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb)

    elif selected_piece == "Q" or selected_piece == "q":
        queen(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb)

    elif selected_piece == "K" or selected_piece == "k":
        king(cb_empty,cb,y_start_cb,x_start_cb,y_dest_cb,x_dest_cb)

    cb.reverse()
    cb_empty.reverse()
    
    # Updating
    update(cb)


