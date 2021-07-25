#EXTREME Tic Tac Toe
#By: Rachel Sousa & Mike Engle

import tkinter as tk #import the tkinter library
from collections import defaultdict
pO_col = "purple"
pX_col = "black"

player = 'O'
highlighted = []
for i in range(11):
    for j in range(11):
        highlighted.append((i,j))

win_matrix = [[0 for col in range(3)] for row in range(3)]

big_grid_dict= defaultdict(list)
big_grid_dict[(0,0)] = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
big_grid_dict[(0,1)] = [(0,4), (0,5), (0,6), (1,4), (1,5), (1,6), (2,4), (2,5), (2,6)]
big_grid_dict[(0,2)] = [(0,8), (0,9), (0,10), (1,8), (1,9), (1,10), (2,8), (2,9), (2,10)]
big_grid_dict[(1,0)] = [(4,0), (4,1), (4,2), (5,0), (5,1), (5,2), (6,0), (6,1), (6,2)]
big_grid_dict[(1,1)] = [(4,4), (4,5), (4,6), (5,4), (5,5), (5,6), (6,4), (6,5), (6,6)]
big_grid_dict[(1,2)] = [(4,8), (4,9), (4,10), (5,8), (5,9), (5,10), (6,8), (6,9), (6,10)]
big_grid_dict[(2,0)] = [(8,0), (8,1), (8,2), (9,0), (9,1), (9,2), (10,0), (10,1), (10,2)]
big_grid_dict[(2,1)] = [(8,4), (8,5), (8,6), (9,4), (9,5), (9,6), (10,4), (10,5), (10,6)]
big_grid_dict[(2,2)] = [(8,8), (8,9), (8,10), (9,8), (9,9), (9,10), (10,8), (10,9), (10,10)]


#create window
window = tk.Tk()

#layout the gameboard as a matrix
button = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def add_text(r,c):
    global player
    #if spot is empty add text
    #if button[r][c]['text'] == '':
    button[r][c]['text'] = player
        #change to other player
    if player == 'O':
        button[r][c].config(fg=pO_col,)
        label_1.config(text= "X's turn")
        player = 'X'
    else:
        button[r][c].config(fg=pX_col, )
        label_1.config(text="O's turn")
        player = 'O'

def check_lilwin(m,n):
    global win_matrix
    i, j = big_grid_dict[(m, n)][0]
    for num in range(3):
        if button[i+num][0]['text'] == button[i+num][1]['text'] == button[i+num][2]['text'] != '':
            if player == 'O':
                win_matrix[m][n] = 1
            else:
                win_matrix[m][n] = 2
    for num in range(3):
        if button[0][j+num]['text'] == button[1][j+num]['text'] == button[2][j+num]['text'] != '':
            if player == 'O':
                win_matrix[m][n] = 1
            else:
                win_matrix[m][n] = 2
    if button[i][j]['text'] == button[i+1][j+1]['text'] == button[i+2][j+2]['text'] != '':
        if player == 'O':
            win_matrix[m][n] = 1
        else:
            win_matrix[m][n] = 2
    elif button[i][j+2]['text'] == button[i][j]['text'] == button[i+2][j]['text'] != '':
        if player == 'O':
            win_matrix[m][n] = 1
        else:
            win_matrix[m][n] = 2

def check_bigwin():
    global win_matrix
    for i in range(3):
        if win_matrix[i][0] == win_matrix[i][1] == win_matrix[i][2] != 0:
            return True
    for j in range(3):
        if win_matrix[0][j] == win_matrix[1][j] == win_matrix[2][j] != 0:
            return True
    if win_matrix[0][0] == win_matrix[1][1] == win_matrix[2][2] != 0:
        return True
    elif win_matrix[0][2] == win_matrix[1][1]== win_matrix[2][0] != 0:
        return True
    return False

#######attempt to highlight a whole 3x3 matrix######
def highlight_grid(r, c):
    global highlighted
    m = r
    n = c

    if check_bigwin() == False:
        if (r > 3 and r < 7):
            m = (r - 4)
        elif (r > 7):
            m = (r - 8)

        if (c > 3 and c < 7):
            n = (c - 4)
        elif (c > 7):
            n = (c - 8)

        if (r, c) in highlighted and button[r][c]['text'] == '':
            print("hi")
            add_text(r, c)

            check_lilwin(m,n)
            print(win_matrix)

            #clear the board
            for e in range(11):
                w = 0
                for w in range (11):
                    if (e!=3 and e!=7):
                        if (w!=3 and w!=7):
                            button[e][w].config(bg="white",)

            for i in range(len(big_grid_dict[(m,n)])):
                #get index of grid space
                row, col = big_grid_dict[(m,n)][i][0], big_grid_dict[(m,n)][i][1]
                #set grid space to color
                button[row][col].config(bg="green", )
            highlighted = big_grid_dict[(m,n)]

    else:
        if player == 'O':
            label_1.config(text="O Won!!")
        else:
            label_1.config(text="X Won!!")


#Should this be it's own function?
for i in range(11):
    for j in range(11):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        # frame.grid(row=i, column=j, padx=5, pady=5)
        if j == 3 or j == 7 or i == 3 or i == 7:
            frame.grid(row=i, column=j, padx=5, pady=5)
        else:
            button[i][j] = tk.Button(text='',
                width=5,
                height=3,
                bg="white",
                command=lambda r=i, c=j: highlight_grid(r, c),
                fg="blue",
                borderwidth=1
            )
            button[i][j].grid(row=i, column=j, padx=1, pady=1)

label_1 = tk.Label(text="O's turn", font=('normal', 22, 'bold'))
label_1.grid(row=11, column=0, columnspan=11)



window.mainloop()
