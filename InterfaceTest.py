#import tkinter as tk
#
#class Application(tk.Frame):
#    def __init__(self, master=None):
#        tk.Frame.__init__(self, master)
#        self.grid()
#
#app = Application()
#app.master.title("Tkinter")
#app.mainloop()



from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI")

        self.Textfeld = Label(master, text="Ein einfaches Python GUI!")
        self.Textfeld.pack()

        self.greet_button = Button(master, text="Funktion ausführen", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="[X]", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Irgendwas")
        #do something






root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()