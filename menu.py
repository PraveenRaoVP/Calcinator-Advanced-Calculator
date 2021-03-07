from tkinter import *
from math import *

from sciencalc import *
from simplecalc import *

content=""

root=Tk()
root.geometry("700x700")
simple_button=Button(root,text="Simple Calculator",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:root1.mainloop(),height=3,width=10)
simple_button.place(x=200,y=350)
scien_button=Button(root,text="Scientific Calculator",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:root2.mainloop(),height=3,width=10)
scien_button.place(x=400,y=350)
exit_button=Button(root,text="Exit",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:exit(),height=2,width=6)
exit_button.place(x=600,y=50)

root.mainloop()



     

