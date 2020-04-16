import tkinter as tk
import random

#_________________Global Variables_____________
list = []
labellist = []
ll = 20

colorful = False

#Buttons
hx = 5
wx = 5
bx = 15
rx = tk.RIDGE

#List
ViewA = 0
ViewB = 0
ViewList = []


#________________________________________________

#list = [[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],
#[[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],
#[[0, 2], [1, 2], [2, 2, "green"], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]],
#[[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3, "white"], [6, 3], [7, 3], [8, 3], [9, 3]],
#[[0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]],
#[[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]],
#[[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6], [9, 6]],
#[[0, 7], [1, 7], [2, 7], [3, 7, "blue"], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7]],
#[[0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8]],
#[[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9, "yellow"]]]


colours = [["black"],
           ["cyan"],
           ["magenta"],
           ["red"],
           ["blue"],
           ["gray"],
           ["green"],
           ["white"],
           ["pink"],
           ["lime"],
           ["yellow"]]



for i in range(ll):
    list.append([])
    for k in range(ll):
        list[i].append([k,i,random.choice(colours)])
print(len(list),"x",len(list))
print(len(list)*len(list[0]), "Felder")



#for element in list:
#    print(element)



#for y in range(5):
#    print("")
#    for x in range(5):
#        print(list[x+a][y+b], sep="",end="")
#        c.append(list[x+a][y+b])

#print("\n\n",c)


def ListChange():
    global ViewA
    global ViewB
    global ViewList
    global list

    if(ViewA >= len(list)-4):# or ViewA <= -5):
        ViewA = -4

    if (ViewB >= len(list)-4):# or ViewB <= -5):
        ViewB = -4

    if (ViewA <= -len(list)):
        ViewA = 0

    if (ViewB <= -len(list)):
        ViewB = 0




    ViewList = []
    for y in range(5):
        for x in range(5):
            ViewList.append(list[y + ViewA][x + ViewB])

    for n in range(25):
        coords = "[" + str(ViewList[n][0]) +" , "+ str(ViewList[n][1]) + "]"

        if(not len(ViewList[n])<3 and colorful or ViewList[n][0]==0 and ViewList[n][1]==0):
            color = ViewList[n][2]
        else:
            color = "SystemButtonFace"


        labellist[n].config(text=coords, bg = color)

    print("starting position is now: [{},{}]".format( ViewB, ViewA))



def Mid(event):
    event.widget.configure(bg="red")


def Up():
    global ViewA
    ViewA -= 1
    ListChange()


def Left():
    global ViewB
    ViewB -= 1
    ListChange()


def Right():
    global ViewB
    ViewB += 1
    ListChange()


def Down():
    global ViewA
    ViewA += 1
    ListChange()





root = tk.Tk()
root.config(bg="PaleTurquoise2")
#root.resizable(False, False)


for i in range(5):
    for k in range(5):
        label = tk.Label(root, bd=1, relief=tk.SOLID, font="Helvetica 10 bold", text="")
        label.grid(column=k,row=i, sticky="nesw")

        root.grid_columnconfigure(i, minsize=120)
        root.grid_rowconfigure(k, minsize=120)
        labellist.append(label)
ListChange()

#m = tk.Canvas(root, bg="lime", width=250, height=150)
#m.place(x=350, y=450)
#m.bind("<Button-1>",Mid)


up = tk.Button(text="up",height=hx,width=wx,border=bx, relief=rx, command=Up).grid(column=2, row=6, sticky="nesw")
left = tk.Button(text="left",height=hx,width=wx,border=bx, relief=rx, command=Left).grid(column=1, row=7, sticky="nesw")
middle = tk.Button(text="middle",height=hx,width=wx,border=bx, relief=rx, command=Mid).grid(column=2, row=7, sticky="nesw")
right = tk.Button(text="right",height=hx,width=wx,border=bx, relief=rx, command=Right).grid(column=3, row=7, sticky="nesw")
down = tk.Button(text="down",height=hx,width=wx,border=bx, relief=rx, command=Down).grid(column=2, row=8, sticky="nesw")



root.mainloop()