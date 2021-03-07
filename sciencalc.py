from tkinter import *
from math import *
from menu import *

'''
The operations to be performed:-
     Addition
     Subtraction
     Multiplication 
     Division
     Modulus
     ln
     log
     power a^b
     square root
     +/-
     maximize and minimize font    
     
Calculator SETUP:-

|===========================================================================|  |
|                           Scientific Calculator                           |  |                        |
|===========================================================================|  |
|  |    ==================================================================  |  |       
|  |    ==================================================================  |  |                                                                         
|  |                                                                        |  |
|  |                                     ERASE  CLEAR                       |  |
|  |                      e        log ln  pow  +                           |  |
|  |                      pi       1   2   3    -                           |  |
|  |                      mod      4   5   6    x                           |  |
|  |                      sqrt     7   8   9    /                           |  |
|  |                      ( )      .   0   +/-  =                           |  |
|  |                                                                        |  |
|  |                                                                        |  |
|==============================================================================|
|                                                                              |
|==============================================================================|




     
'''



content=""
π=3.141592653589793238462643
e=2.71828
content=""
def buttonPress(num):
     global content 
     content+=str(num)
     answer.set(content)
def clear():
     global content
     content=""
     answer.set(content)
     
def pressX():
     global content
     content=list(content)
     if content:
          content.pop()
     else:
          content=""
     content=str(content)
     
     content=content.replace('[','')
     content=content.replace(']','')
     content=content.replace("'","")
     content=content.replace('"','')
     content=content.replace(",","")
     content=content.replace(" ","")
     answer.set(content)
     
     
def calcPower(a,b):
     return a**b

def calcLog(a):
     return log(a,10)

def calcLn(a):
     return log(a,e)

def pressEqual():
     try:
          global content
          if('^' in content):
               total=str(eval(content.replace('^','**')))
               answer.set(total)
               content=total
          elif 'mod' in content:
               total=str(eval(content.replace('mod','%')))
               answer.set(total)
               content=total
               
          elif 'log' in content:
               logNumber=int(content.replace('log ',''))
               total=str(calcLog(logNumber))
               answer.set(total)
               content=total
          elif 'ln' in content:
               lnNumber=int(content.replace('ln',''))
               total=str(calcLn(lnNumber))
               answer.set(total)
               content=total
               
               
          elif '%' in content:
               total=str(eval(content))
               answer.set(total)
               content=total
          elif '√' in content:
               rootcontent=content.replace('√','')
               total=str(sqrt(int(rootcontent)))
               answer.set(total)
               content=total
          elif 'x' in content:
               mulcontent=content.replace('x','*')
               total=str(eval(mulcontent))
               answer.set(total)
               content=total
          else:
               total = str(eval(content))
               answer.set(total)
               content=total
          
     except:
          answer.set("ERROR")
          content=""

def pressAbsolute(content):
     content=int(content)
     content=-(content)
     content=str(content)
     answer.set(content)
     
root2=Tk()
root2.geometry("700x700")
frame = Frame(root2,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

title=root2.title("Scientific Calculator!")
answer=StringVar()
exp=Entry(root2,textvariable=answer)
exp.place(x=100,y=100,bordermode=INSIDE,width=500,height=30)

#1
button1= Button(root2,text="1",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("1"),height=2,width=6)
button1.place(x=200,y=350)
#2
button2= Button(root2,text="2",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("2"),height=2,width=6)
button2.place(x=300,y=350)
#3
button3= Button(root2,text="3",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("3"),height=2,width=6)
button3.place(x=400,y=350)
#4
button4= Button(root2,text="4",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("4"),height=2,width=6)
button4.place(x=200,y=430)
#5
button5= Button(root2,text="5",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("5"),height=2,width=6)
button5.place(x=300,y=430)
#6
button6= Button(root2,text="6",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("6"),height=2,width=6)
button6.place(x=400,y=430)
#7
button7= Button(root2,text="7",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("7"),height=2,width=6)
button7.place(x=200,y=510)
#8
button8= Button(root2,text="8",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("8"),height=2,width=6)
button8.place(x=300,y=510)
#9
button9= Button(root2,text="9",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("9"),height=2,width=6)
button9.place(x=400,y=510)
#0
button0= Button(root2,text="0",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("0"),height=2,width=6)
button0.place(x=300,y=590)
#pi
buttonpi= Button(root2,text="π",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("π"),height=2,width=6)
buttonpi.place(x=100,y=350)
#e
button_e= Button(root2,text="e",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("e"),height=2,width=6)
button_e.place(x=100,y=270)
#power(a^b)
buttonpow= Button(root2,text="^",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress('^'),height=2,width=6)
buttonpow.place(x=400,y=270)
#log
buttonlog= Button(root2,text="log",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress('log '),height=2,width=6)
buttonlog.place(x=200,y=270)
#ln
buttonln= Button(root2,text="ln",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress('ln '),height=2,width=6)
buttonln.place(x=300,y=270)
#=
buttoneq= Button(root2,text="=",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:pressEqual(),height=2,width=6)
buttoneq.place(x=500,y=590)
# ERASE
buttonx=Button(root2,text="ERASE",font="Calibri 12",fg="black",bg="white",padx=10, pady=10,command=lambda:pressX(),height=2,width=6)
buttonx.place(x=400,y=190)
#CLEAR
buttoncls= Button(root2,text="CLEAR",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:clear(),height=2,width=6)
buttoncls.place(x=500,y=190)

#+/- absolute value
buttonabs=Button(root2,text="+/-",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:pressAbsolute(content),height=2,width=6)
buttonabs.place(x=400,y=590)

#addition

buttonadd= Button(root2,text="+",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("+"),height=2,width=6)
buttonadd.place(x=500,y=270)

#subtraction

buttonsub= Button(root2,text="-",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("-"),height=2,width=6)
buttonsub.place(x=500,y=350)

#multiplication

buttonmul= Button(root2,text="x",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("x"),height=2,width=6)
buttonmul.place(x=500,y=430)

#division

buttondiv= Button(root2,text="/",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress("/"),height=2,width=6)
buttondiv.place(x=500,y=510)

#decimal point
buttondec=Button(root2,text='.',font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress('.'),height=2,width=6)
buttondec.place(x=200,y=590)

#modulo
buttonmod=Button(root2,text='%',font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress('%'),height=2,width=6)
buttonmod.place(x=100,y=430)
#back button
buttonback=Button(root2,text="Back",font="Calibri 12", fg="black",bg="white",padx=10,pady=10,command=lambda:[menu_in_screen(),exit()],height=2,width=6)
buttonback.place(x=600,y=50)

#square root
buttonsqrt=Button(root2,text="√x",font="Calibri 12",fg="black",bg="white",padx=10,pady=10,command=lambda:buttonPress('√'),height=2,width=6)
buttonsqrt.place(x=100,y=510)

#window display
root2.mainloop()    
'''
Completed Buttons:-
1-0
abs (need to test its function) update-works only once.
log, ln
power
decimal point 
Erase, Clear
add,subtract,multiply,divide
equal to sign =
e, pi completed


Need to complete:-
mod (completed)
sqrt √x (completed)

'''


