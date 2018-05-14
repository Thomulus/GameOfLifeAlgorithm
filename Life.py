from tkinter import *

currentgen  = 0
grid        = []
M           = 0 #M is number of rows

def update():
    global grid, currentgen;
    if currentgen <= generations:
        root.label.configure(text=currentgen)
        graph.delete(ALL)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                graph.create_rectangle(8*col,8*row,8*col+8,8*row+8,
                    fill="red" if grid[row][col] == 1 else "black")

        temp = [[0 for x in range(N)] for y in range(M)];

        for i in range(M):
            for j in range(N):
                count = checkNeighbours(i, j);
                temp[i][j] = 1 if count == 3 or (count == 2 and grid[i][j] == 1) else 0

        grid = temp
        currentgen += 1
    graph.after(50,update)

def checkNeighbours(i, j):
    count = 0
    for x in range(3):
        for y in range(3):
            xcoord = (x-1+i) % (len(grid))
            ycoord = (y-1+j) % (len(grid[0]))
            if (x != 1 or y !=1) and grid[xcoord][ycoord] == 1: count += 1;

    return count

with open("inLife.txt", "r") as f:
    generations = int(f.readline())
    global N #N is number of columns
    for line in f:
        M += 1;       #M is number of rows
        grid.append([int(i) for i in list(line.replace("\n", ""))]);

    N = len(line)
    WIDTH = 8*N
    HEIGHT = 8*(M+4) #+4 added to account for some UI elements.
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT,
        (root.winfo_screenwidth() - WIDTH) / 2,
        (root.winfo_screenheight() - HEIGHT) / 2))
    root.bind_all('<Escape>', lambda event: event.widget.quit())
    root.label = Label(root, text="")
    root.label.pack()
    graph = Canvas(root, width=WIDTH, height=HEIGHT, background='white')
    graph.after(1000, update)
    graph.pack()
    mainloop()


