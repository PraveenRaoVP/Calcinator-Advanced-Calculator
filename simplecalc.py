import math
from tkinter import *
from menu import *
from sciencalc import *
from simplecalc import *
from menu import *



     

def buttonPress(num):
     global content
     content+=str(num)
     answer.set(content)

def pressEqual():
     try:
          global content
          total = str(eval(content))
          answer.set(total)
          content=total
     except:
          answer.set("ERROR")
          content=""

def clear():
     global content
     content=""
     answer.set("")


root1=Tk()
root1.geometry("700x700")
answer = StringVar()


frame = Frame(root1,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

title = root1.title("Simple Calculator!")
welcomeStatement=""
welcomeStatement= Label(root1,text="Perform Simple Calculations!!")
welcomeStatement.place(x=275,y=30)
expression_in_calc=""
expression_in_calc=Entry(root1,font="Calibri 20",textvariable=answer)
expression_in_calc.place(x=100,y=100,bordermode=INSIDE,width=500,height=30)


button1= Button(root1,text="1",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("1"),height=3,width=15)
button1.place(x=100,y=250)

button2= Button(root1,text="2",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("2"),height=3,width=15)
button2.place(x=275,y=250)

button3= Button(root1,text="3",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("3"),height=3,width=15)
button3.place(x=450,y=250)

button4= Button(root1,text="4",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("4"),height=3,width=15)
button4.place(x=100,y=350)

button5= Button(root1,text="5",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("5"),height=3,width=15)
button5.place(x=275,y=350)

button6= Button(root1,text="6",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("6"),height=3,width=15)
button6.place(x=450,y=350)

button7= Button(root1,text="7",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("7"),height=3,width=15)
button7.place(x=100,y=450)

button8= Button(root1,text="8",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("8"),height=3,width=15)
button8.place(x=275,y=450)

button9= Button(root1,text="9",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("9"),height=3,width=15)
button9.place(x=450,y=450)

button0= Button(root1,text="0",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("0"),height=3,width=15)
button0.place(x=275,y=550)

buttondec= Button(root1,text=".",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("."),height=3,width=15)
buttondec.place(x=100,y=550)

buttoneq = Button(root1,text="=",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:pressEqual(),height=3,width=15)
buttoneq.place(x=450,y=550)

buttonplus= Button(root1,text="+",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("+"),height=3,width=8)
buttonplus.place(x=100,y=150)

buttonminus= Button(root1,text="-",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("-"),height=3,width=8)
buttonminus.place(x=200,y=150)

buttonmul= Button(root1,text="x",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("*"),height=3,width=8)
buttonmul.place(x=300,y=150)

buttondiv= Button(root1,text="/",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("/"),height=3,width=8)
buttondiv.place(x=400,y=150)

buttonclear= Button(root1,text="Clear",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:clear(),height=3,width=8)
buttonclear.place(x=500,y=150)

buttonback=Button(root1,text="Back to Menu",font="Calibri 12", fg="black",bg="white",padx=10,pady=10,command=lambda:[f() for f in [root1.mainloop(),exit()]],height=2,width=6)
buttonback.place(x=600,y=50)

root1.mainloop()

