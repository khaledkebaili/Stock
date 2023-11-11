from subprocess import call
from tkinter import ttk,Tk
from tkinter import *
from  tkinter import messagebox

def ACHATS ():
    xd.destroy()
    call(["python","ACHATS.py"])
def AJOUTER_AD ():
    xd.destroy()
    call(["python", "new_admin.py"])
def VENTS():
    xd.destroy()
    call(["python","vents.py"])

xd = Tk()

xd.title("GESTION DU STOCK")
xd.geometry("600x400+400+180")
xd.resizable(False, False)
c=Canvas(xd,bg="#ffffff",height="200",width="200")
f=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\k.png")
back=Label(xd,image=f)
back.place(x=50,y=30,relheight=1,relwidth=1)
c.pack()

lbltitre = Label(xd,borderwidth=3,relief=SUNKEN,text="GESTION DU STOCK",font=("sans Serif",25),)
lbltitre.place(x=0,y=0,width=600)

ba = Button(xd,text="ACHATS",font=("Arial",24),command=ACHATS)
ba.place(x=10,y=80,width=150)

bv = Button(xd,text="VENTES",font=("Arial",24),command=VENTS)
bv.place(x=160,y=80,width=150)

bm = Button(xd,text="AJOUTER ADMIN",font=("Arial",24),command=AJOUTER_AD)
bm.place(x=310,y=80,width=280)
xd.mainloop()
