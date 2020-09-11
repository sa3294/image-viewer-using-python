from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("hell")
root.iconbitmap(r'C:\Users\soumy\Desktop\python\image_viewer\coff.ico')

mimg = ImageTk.PhotoImage(Image.open(r'C:\Users\soumy\Desktop\python\image_viewer\1.jpg'))
mlabel = Label(image=mimg)
mlabel.pack()
root.mainloop()