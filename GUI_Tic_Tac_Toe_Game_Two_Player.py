from tkinter import *
from tkinter import messagebox
import random as r


def button(frame):        
    b=Button(frame,padx=1,bg="tan",width=3,text="   ",font=('roboto',60,'bold'),relief="ridge",bd=10)
    return b

def change_():             
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break


def reset():               
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])


def check():                
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Woohoo!!",a+" is the winner :-)")
                    reset()

    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Woohoo!!",a+" is the winner :-)")
        reset()   

    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Its a tie!!","The match has ended in a draw :-/")
        reset()


def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_()
        label.config(text=a+"'s Chance")


root=Tk()                  
root.title("Tic-Tac-Toe")   
a=r.choice(['O','X'])      
colour={'O':"darkblue",'X':"firebrick"}

b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)


label=Label(text=a+"'s Chance",font=('roboto',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()