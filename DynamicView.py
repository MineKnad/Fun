import tkinter as tk


def addweight(row,column):
    c.grid_rowconfigure(row, weight=1,minsize=30)
    c.grid_columnconfigure(column, weight=1,minsize=28)


class Feld:
    def __init__(self, coords, farbe):
        self.coords = coords
        self.farbe = farbe


##############################################################

screenX = 12
screenY = 8


listx = 16
listy = 16

xmove = 0
ymove = 0

div=1

showcoords = False
labellist = []
list = []

chooser = 0

viewlist = []

##############################################################

if(screenY > 18 or screenX > 38):
    div = 3
elif(screenY > 9 or screenX > 19):
    div = 2





# ##################### Funktion ScreenView ############################################################################

def ScreenView():
    viewlist = []
    global xmove
    global ymove

    #constrict the variables
    if (xmove <= -len(list[0])):
        xmove = 0

    if (ymove <= -len(list)):
        ymove = 0


    if (xmove >= len(list[0]) - (screenX-1)):
        xmove = -(screenX-1)

    if (ymove >= len(list) - (screenY-1)):  # or ViewB <= -5):
        ymove = -(screenY-1)


    try:
        for i in range(screenY):
            for j in range(screenX):
                viewlist.append(list[i + ymove][j + xmove])
    except:
        print("ERROR: Liste zu klein für Screen!")
        quit()


    #print("\n", labellist, "\n")

    #for instance in viewlist:
    #    print(instance.coords, end=" ")


    for i in range(len(labellist)):
        if(showcoords):
            labellist[i].config(text=viewlist[i].coords, bg=viewlist[i].farbe)
        else:
            labellist[i].config(text="", bg=viewlist[i].farbe)

    return(viewlist)

#Every command (event)----------------------------------------------------------------------

def up():
    global ymove
    ymove -= 1
    ScreenView()

def down():
    global ymove
    ymove += 1
    ScreenView()

def left():
    global xmove
    xmove -= 1
    ScreenView()

def right():
    global xmove
    xmove += 1
    ScreenView()


def ClickEvent(event):
    global chooser
    pos = labellist.index(event.widget)

    #print(pos)
    #print(ScreenView()[pos])

    if(chooser == 3):
        if(event.num == 1):
            ScreenView()[pos].farbe = "SkyBlue1"

        elif (event.num == 3):
            ScreenView()[pos].farbe = "SkyBlue3"

    if (chooser == 0):
        if (event.num == 1):
            ScreenView()[pos].farbe = "green"

        elif (event.num == 3):
            ScreenView()[pos].farbe = "LightGoldenrod2"



    ScreenView()



def Choose(event):
    global chooser
    if(event.widget.cget("relief") == tk.FLAT):
        event.widget.config(relief=tk.SUNKEN)
        chooser = 3
    else:
        event.widget.config(relief=tk.FLAT)
        chooser = 0





# Creating list and viewlist
#Creating the FELD objects
########################################################################################################################

for i in range(listy):
    list.append([])
    for k in range(listx):
        list[i].append(Feld([k,i],"SkyBlue3"))
list[0][0].farbe = "red"



for row in list:
    print("")
    for instance in row:
        print(instance.coords, end=",")

print("\n\n")






root = tk.Tk()

root.geometry("{}x{}".format(int(screenX * 100//div), screenY * 100//div + 100))
if(screenX > 1):
    root.resizable(0,0)




#Create Labels
########################################################################################################################
for i in range(screenY):
    for j in range(screenX):

        label = tk.Label(relief=tk.SOLID, bd= 1)

        labellist.append(label)
        label.config(text=label)

        # bind label to ClickEvent
        label.bind("<Button-1>", ClickEvent)
        label.bind("<Button-3>", ClickEvent)


        #bind to grid
        label.grid(column=j, row=i, sticky="nsew")

        root.grid_rowconfigure(i, weight=1)# minsize=40)
        root.grid_columnconfigure(j, weight=1)#minsize=40)








#Buttons
#========================================================================

tk.Label().grid(column=0, row=screenY + 1)
root.grid_rowconfigure(screenY + 1, weight=1)

c = tk.Canvas(root,bg="gray88",height=80,width=80)
c.place(x=(screenX * 50//div) - 40, y=(screenY * 100//div) + 10)

up = tk.Button(c,text="↑", command=up ).grid(row=0, column=1, sticky="nsew")
left = tk.Button(c,text="←", command=left ).grid(row=1, column=0, sticky="nsew")
middle = tk.Button(c).grid(row=1, column=1, sticky="nsew")
right = tk.Button(c,text="→", command=right ).grid(row=1, column=2, sticky="nsew")
down = tk.Button(c,text="↓", command=down ).grid(row=2, column=1, sticky="nsew")

addweight(0,1)
addweight(1,0)
addweight(1,1)
addweight(1,2)
addweight(2,1)


#Editor - buttons
choser3 = tk.Canvas(root,bg="light sky blue",height=20,width=20, bd=5)
choser3.place(x=(screenX * 50//div) - 100, y=(screenY * 100//div) + 40)
choser3.bind("<Button-1>", Choose)



ScreenView()
print("View started")


root.mainloop()
