import tkinter as tk
import tkinter.messagebox as msg
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Hallo")

description = """Hallo, das ist ein Python gui!
Es ist voll Cool!"""

# Funktion wandelt RGB in Tkinter - freundliche colorcodes um!


def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


def pprint():
    print("Hallo!")
    print(slider.get())


def qquit():
    if(msg.askyesno("Schließen","Wirklich beenden?")):
        quit()


button = tk.Button(root, text="Klick!", command=pprint, font="Helvetica 12 italic")
button.pack(side="bottom")


button = tk.Button(root, text="Quit", command=qquit, fg="red", font="Helvetica 8 bold")
button.pack(side="bottom")

label = tk.Label(root, text=description, fg="red", bg="white", relief=tk.RIDGE)         # padx=10, pady=10, justify=tk.LEFT, height=4, width=20)
label.pack(side="right")

bild = ImageTk.PhotoImage(Image.open("Irgendwas.png"))

label = tk.Label(root, image=bild, cursor="plus")
label.pack(side="right")

slider = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
slider.pack()



root.mainloop()