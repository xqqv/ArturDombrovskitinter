from tkinter import *
f=False
def tehtudvalik():
    global f
    if f:
        texbox.configure(show="*")
        f=False
    else:
        texbox.configure(show="")
        f=True
def textpealkirjesse():
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0,END)
aken=Tk()
aken.geometry("400x500")
aken.title("akna pealkiri")
aken.configure(bg="#13e0eb")
aken.iconbitmap("icon.ico")
pealkiri=Label (aken,text="põhielemendid", bg="#9edb8f",fg="#18420d", cursor="star", font="Britannic_Bold 16", justify=CENTER,height=3,width=26) 
raam=Frame(aken)
texbox=Entry(raam, bg="#9edb8f",fg="#18420d",font="Britannic_Bold 16",width=20)

pilt=PhotoImage(file="eye.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,image=pilt, variable=var, onvalue=True, offvalue=False, command=tehtudvalik)
valik.deselect()
nupp=Button(raam, text="Vajuta mind", bg="#d5f0e0", fg="#18420d", font="Britannic_Bold 16", width=16)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0)
valik.grid(row=0,column=1)
nupp.grid(row=0,column=2)
aken.mainloop()
