from subprocess import call
from tkinter import ttk,Tk
from tkinter import *
from  tkinter import messagebox
import mysql.connector

def Retour():
    xd.destroy()
    call(["python","main1.py"])

def Ajouter():

    NOME = txtNOME.get()
    PASS = txtPASS.get()
    GMAIL = txtGMAIL.get()


    maBase = mysql.connector.connect(host="localhost",user="root",password="",database="login")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO usuario (email,username,password) VALUES (%s, %s, %s)"
        val = (GMAIL,NOME,PASS)
        meConnect.execute(sql,val)
        maBase.commit()
        derniercode = meConnect.lastrowid
        messagebox.showinfo("information","admin ajouter")
        xd.destroy()
        call(["python", "new_admin.py"])

    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close

def Supprimer():
    PASS = txtPASS.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="login")
    meConnect = maBase.cursor()
    try:
        sql = "delete from usuario where password= %s "
        val = (PASS,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniercode = meConnect.lastrowid
        messagebox.showinfo("information", "admin supprimer")
        xd.destroy()
        call(["python", "new_admin.py"])
    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close

xd = Tk()

xd.title("AJOUTER ADMIN")
xd.geometry("900x250+300+150")
xd.resizable(False, False)


lblNOME = Label(xd,text="NAME",font=("Arial",18),bg="white",fg="black")
lblNOME.place(x=50,y=50,width=250)
txtNOME = Entry(xd,bd=4,font=("Arial",18),bg="white",fg="black")
txtNOME.place(x=350,y=50,width=250)

lblPASS = Label(xd,text="MOT DE PASS ",font=("Arial",18),bg="white",fg="black")
lblPASS.place(x=50,y=105,width=250)
txtPASS = Entry(xd,bd=4,font=("Arial",18),bg="white",fg="black")
txtPASS.place(x=350,y=105,width=250)

lblGMAIL = Label(xd,text="email",font=("Arial",18),bg="white",fg="black")
lblGMAIL.place(x=50,y=160,width=250)
txtGMAIL = Entry(xd,bd=4,font=("Arial",18),bg="white",fg="black")
txtGMAIL.place(x=350,y=160,width=250)

benreg = Button(xd,text="Enregistrer",font=("Arial",16),bg="white",fg="black",command=Ajouter)
benreg.place(x=650,y=55,width=200)

bretour = Button(xd,text="Retour",font=("Arial",16),bg="white",fg="black",command=Retour)
bretour.place(x=650,y=105,width=200)

bsupprimer = Button(xd,text="SUPPRIMER",font=("Arial",16),bg="white",fg="black",command=Supprimer)
bsupprimer.place(x=650,y=155,width=200)

xd.mainloop()