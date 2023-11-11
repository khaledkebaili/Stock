import tkinter
from cProfile import  label
from subprocess import call
from tkinter import ttk,Tk
from tkinter import *
from  tkinter import messagebox
import mysql.connector

def Retour():
    xd.destroy()
    call(["python","main1.py"])

def Ajouter():
    code = txtcode.get()
    client = txtclient.get()
    produit = comprauduit.get()
    telephoun = txttelephoun.get()
    prix = txtprix.get()
    quantiter = txtquantiter.get()

    maBase = mysql.connector.connect(host="localhost",user="root",password="",database="vents")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO tb_vents (code, client, produit, telephoun, prix, quantiter) VALUES (%s, %s, %s, %s, %s,%s)"
        val = (code, client, produit, telephoun, prix, quantiter)
        meConnect.execute(sql,val)
        maBase.commit()
        derniercode = meConnect.lastrowid
        messagebox.showinfo("information","vent ajouter")
        xd.destroy()
        call(["python", "vents.py"])

    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close

def Modifer():
    code = txtcode.get()
    client = txtclient.get()
    produit = comprauduit.get()
    telephoun = txttelephoun.get()
    prix = txtprix.get()
    quantiter = txtquantiter.get()

    maBase = mysql.connector.connect(host="localhost",user="root",password="",database="vents")
    meConnect = maBase.cursor()

    try:
        sql = "update tb_vents set client=%s, produit=%s, telephoun=%s, prix=%s, quantiter=%s where code=%s"
        val = ( client, produit, telephoun, prix, quantiter,code)
        meConnect.execute(sql, val)
        maBase.commit()
        derniercode = meConnect.lastrowid
        messagebox.showinfo("information", "vent modifer")
        xd.destroy()
        call(["python", "vents.py"])

    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close
def Supprimer():
    code = txtcode.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="vents")
    meConnect = maBase.cursor()
    try:
        sql = "delete from tb_vents  where code= %s "
        val = (code,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniercode = meConnect.lastrowid
        messagebox.showinfo("information", "vent supprimer")
        xd.destroy()
        call(["python", "vents.py"])
    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close
xd = Tk()

xd.title("MENUE VENTS")
xd.geometry("1350x700+0+0")
xd.resizable(False, False)
c=Canvas(xd,bg="gray16",height="200",width="200")
f=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\a.png")
back=Label(xd,image=f)
back.place(x=300,y=45,relheight=1,relwidth=1)
c.pack()
lbltitre = Label(xd,borderwidth=3,relief=SUNKEN,text="GESTION DES VENTS",font=("sans Serif",25))
lbltitre.place(x=0,y=0,width=1350,height=100)


lblproduit = Label(xd,text="PRODUIT",font=("Arial",18), bg="white",fg="black")
lblproduit.place(x=50,y=200,width=250)
comprauduit = ttk.Combobox(xd,font=("Arial",18))
comprauduit['values']=['scanaire','respirateur','ecg']
comprauduit.place(x=350,y=200,width=250)

lblclient = Label(xd,text="CLIENT",font=("Arial",18), bg="white",fg="black")
lblclient.place(x=50,y=250,width=250)
txtclient = Entry(xd,bd=4,font=("Arial",18))
txtclient.place(x=350,y=250,width=250)

lblcode = Label(xd,text="CODE",font=("Arial",18), bg="white",fg="black")
lblcode.place(x=50,y=150,width=250)
txtcode = Entry(xd,bd=4,font=("Arial",18))
txtcode.place(x=350,y=150,width=250)

lbltelephoun = Label(xd,text="TELEPHONE",font=("Arial",18), bg="white",fg="black")
lbltelephoun.place(x=50,y=300,width=250)
txttelephoun = Entry(xd,bd=4,font=("Arial",18))
txttelephoun.place(x=350,y=300,width=250)

lblquantiter = Label(xd,text="QUANTITE",font=("Arial",18), bg="white",fg="black")
lblquantiter.place(x=50,y=350,width=250)
txtquantiter = Entry(xd,bd=4,font=("Arial",18))
txtquantiter.place(x=350,y=350,width=250)

lblprix = Label(xd,text="PRIX",font=("Arial",18), bg="white",fg="black")
lblprix.place(x=50,y=400,width=250)
txtprix = Entry(xd,bd=4,font=("Arial",18))
txtprix.place(x=350,y=400,width=250)

benreg = Button(xd,text="Enregistrer",font=("Arial",16),bg="white",fg="black",command=Ajouter)
benreg.place(x=700,y=175,width=200)

bmod = Button(xd,text="Modifer",font=("Arial",16),bg="white",fg="black",command=Modifer)
bmod.place(x=700,y=225,width=200)

bsup = Button(xd,text="Supprimer",font=("Arial",16),bg="white",fg="black",command=Supprimer)
bsup.place(x=700,y=275,width=200)

bretour = Button(xd,text="Retour",font=("Arial",16),bg="white",fg="black",command=Retour)
bretour.place(x=700,y=325,width=200)

table = ttk.Treeview(xd,columns=(1,2,3,4,5,6,),height= 10,show="headings")
table.place(x=0,y=550,width=1350,height=700)

table.heading(1,text = "code")
table.heading(2,text ="client")
table.heading(3,text ="produit")
table.heading(4,text ="telephoun")
table.heading(5,text ="prix")
table.heading(6,text ="quantiter")

table.column(1,width =150)
table.column(2,width =150)
table.column(3,width =150)
table.column(4,width =150)
table.column(5,width =150)
table.column(6,width =150)

maBase = mysql.connector.connect(host="localhost", user="root", password="", database="vents")
meConnect = maBase.cursor()
meConnect.execute("select * from tb_vents")
for row in meConnect:
    table.insert("",END,value=row)

maBase.close()

xd.mainloop()