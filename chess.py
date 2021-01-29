# Update method
def update(cb):
    print("                                          ")
    print("                                          ")
    print("       A   B   C   D   E   F   G   H      ")
    print("     +-------------------------------+    ")
    print("   1 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[0][0],cb[0][1],cb[0][2],cb[0][3],cb[0][4],cb[0][5],cb[0][6],cb[0][7]))
    print("     |-------------------------------|    ")
    print("   2 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[1][0],cb[1][1],cb[1][2],cb[1][3],cb[1][4],cb[1][5],cb[1][6],cb[1][7]))
    print("     |-------------------------------|    ")
    print("   3 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[2][0],cb[2][1],cb[2][2],cb[2][3],cb[2][4],cb[2][5],cb[2][6],cb[2][7]))
    print("     |-------------------------------|    ")
    print("   4 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[3][0],cb[3][1],cb[3][2],cb[3][3],cb[3][4],cb[3][5],cb[3][6],cb[3][7]))
    print("     |-------------------------------|    ")
    print("   5 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[4][0],cb[4][1],cb[4][2],cb[4][3],cb[4][4],cb[4][5],cb[4][6],cb[4][7]))
    print("     |-------------------------------|    ")
    print("   6 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[5][0],cb[5][1],cb[5][2],cb[5][3],cb[5][4],cb[5][5],cb[5][6],cb[5][7]))
    print("     |-------------------------------|    ")
    print("   7 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[6][0],cb[6][1],cb[6][2],cb[6][3],cb[6][4],cb[6][5],cb[6][6],cb[6][7]))
    print("     |-------------------------------|    ")
    print("   8 | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |    ".format(cb[7][0],cb[7][1],cb[7][2],cb[7][3],cb[7][4],cb[7][5],cb[7][6],cb[7][7]))
    print("     +-------------------------------+    ")
    print("                                          ")
    print("                                          ")

# Pawn method
def pawn():
    """ One square movement forward (except for the first turn where two squares movement is allowed) """
    print("Pawn selected.")

# Rook method
def rook():
    """ Entire straight line movements if no piece on its way """
    print("Rook selected.")

# Knight method
def knight():
    """ L frame movements (three squares long and two squares large) """
    print("Knight selected.")

# Bishop method
def bishop():
    """ Entire horizontal line movements if no piece on its way """
    print("Bishop selected.")

# Queen method
def queen():
    """ All pieces movements allowed (except the knight) """
    print("Queen selected.")

# King method
def king():
    """ One square movement in every direction (except if castling movement used with rook) """
    print("King selected.")

# Initialising chessboard
cb = [ [], [], [], [], [], [], [], [] ]
cb[0] = ["r","n","b","q","k","b","n","r"]
cb[1] = ["p","p","p","p","p","p","p","p"]
cb[2] = ["#"," ","#"," ","#"," ","#"," "]
cb[3] = [" ","#"," ","#"," ","#"," ","#"]
cb[4] = ["#"," ","#"," ","#"," ","#"," "]
cb[5] = [" ","#"," ","#"," ","#"," ","#"]
cb[6] = ["P","P","P","P","P","P","P","P"]
cb[7] = ["R","N","B","Q","K","B","N","R"]

ychar_Maj = "ABCDEFGH"
ychar_min = "abcdefgh"

# Gameloop
while(True):
    # Waiting user input
    piece = input("Select a piece of the board to move it (syntax : xy (ex: B3)) : ")

    x = piece[0] # Char
    y = piece[1] # Int

    # X coordinates
    if x in ychar_Maj:
        xeq = ychar_Maj.index(x, 0)

    elif x in ychar_min:
        xeq = ychar_min.index(x, 0)

    # Y coordinates
    yeq = int(y)-1

    # Display selected piece
    if cb[yeq][xeq] == "P" or cb[yeq][xeq] == "p":
        pawn()

    elif cb[yeq][xeq] == "R" or cb[yeq][xeq] == "r":
        rook()
    
    elif cb[yeq][xeq] == "B" or cb[yeq][xeq] == "b":
        bishop()

    elif cb[yeq][xeq] == "Q" or cb[yeq][xeq] == "q":
        queen()

    elif cb[yeq][xeq] == "K" or cb[yeq][xeq] == "k":
        king()

    else:
        if cb[yeq][xeq] == "#":
            print("Empty white square")

        else:
            print("Empty black square")
    # Updating
    update(cb)

    print("xeq={0} / yeq={1}".format(xeq,yeq))                               
    print("Found : {0}\n".format(cb[yeq][xeq]))

    cb.reverse()

    update(cb)
