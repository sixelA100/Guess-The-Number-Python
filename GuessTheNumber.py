from tkinter import *
from tkinter import ttk
import random
from ttkthemes import ThemedTk
window=ThemedTk(theme="equilux")
window.config(themebg="equilux")
window.geometry("500x500")
window.title("GuessTheNumber")
tries=0
ran=random.randint(0,200)
e=ttk.Entry(text="")
e.place(x=170,y=350)
e.configure(state="disabled")
lbltr=ttk.Label(window,text="Tries: "+ str (tries),font=('bold,40'))
lbltr.place(x=190,y=400)
lblt =ttk.Label(window, text="GuessTheNumber", font=('bold', 40))
lblt.place(x=10, y=10)

lbl1=ttk.Label(window,text="In this Game you will try to find a secret number that is randomly chosen every round")
lbl1.place(x=10,y=200)
lbl2=ttk.Label(window,text="Try to guess it with the least possible tries!")
lbl2.place(x=100,y=220)
lblr=ttk.Label(window,text="")


def exit():
    window.destroy()
btne=ttk.Button(window,text="EXIT",command=exit)
btne.place(x=400,y=300)


def randomd():
    global ran
    global tries
    tries=0
    if rb.get()=="EASY(0-50)":
        ran=random.randint(0,50)
    elif rb.get()=="NORMAL(0-100)":
        ran = random.randint(0,100)
    elif rb.get()=="HARD(0-200)":
        ran= random.randint(0,200)
    e.configure(state="enabled")
    btnr.configure(state="disabled")
    e.delete(0, END)
    tries=0
    lbltr.configure(text="Tries: " + str(tries))



btnr=ttk.Button(window,text="Randomize",command=randomd)
btnr.place(x=400,y=350)

rb= StringVar()
rad1=ttk.Radiobutton(window,text="EASY(0-50)",value="EASY(0-50)",variable=rb)
rad1.place(x=50,y=100)

rad2=ttk.Radiobutton(window,text="NORMAL(0-100)",value="NORMAL(0-100)",variable=rb)
rad2.place(x=170,y=100)

rad3=ttk.Radiobutton(window,text="HARD(0-200)",value="HARD(0-200)",variable=rb)
rad3.place(x=300,y=100)

uparrow=PhotoImage(file="uparrow.png")
downarrow=PhotoImage(file="downarrow.png")
correct=PhotoImage(file="correct.png")
die=PhotoImage(file="die.png")

piclbl=ttk.Label(window,image=die)
piclbl.place(x=10,y=300)
def startgame(event):
    try:
        global ran
        global tries
        tries=tries+1
        lbltr.configure(text="Tries: "+str(tries))


        if int(e.get())>ran:
            piclbl.config(image=downarrow)
        elif int(e.get())<ran:
            piclbl.config(image=uparrow)
        elif int(e.get()) == ran:
            piclbl.config(image=correct)
            e.config(state="disabled")
            btnr.configure(state="enabled")
        e.delete(0, END)
    except:
        print("Try to write something inside the entry")
        tries=0
        lbltr.configure(text="Tries: "+str(tries))



window.bind('<Return>',startgame)
window.mainloop()
