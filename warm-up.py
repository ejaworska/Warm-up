import os

def getch():
    #Returns a single character from standard input

    import sys, tty, termios # import modules
    fd = sys.stdin.fileno()# assign to fd variable a file descriptor - (stdin) an integer standard input (0, 1, 2)
    old_settings = termios.tcgetattr(fd)# assign to old_settings variable a list containing the tty attributes for file descriptor fd
    try:
        tty.setraw(sys.stdin.fileno())# change the mode of the file descriptor fd to raw
        ch = sys.stdin.read(1)# assign to ch variable a single character returned from stdin
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)# call a function that returns list containing the tty attributes for file descriptor fd
    return ch # return ch variable


x_ = 5
y_ = 5

while True:
    x = getch()
    os.system('clear')

    if x == "a":
        y_ -= 1
    if x == "s":
        x_ += 1
    if x == "d":
        y_ += 1
    if x == "w":
        x_ -= 1
    board = [[".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."]]
    board[x_][y_] = "@"

    for i in board:
        print("".join(i))
