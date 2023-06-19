from tkinter import *


def Clear():
    pytext.delete(0,'end')
    OStext.delete(0,"end")
    Matext.delete(0,"end")
    hinext.delete(0,"end")
    engtext.delete(0,"end")
    oectext.delete(0,"end")

def Result():
    root2=Tk()

    root2.title('MARK SHEET')
    root2.geometry("400x300")
    root2.configure(bg="")
    root2.resizable(False, False) 

    if pytext.get()=="" or OStext.get()=="" or Matext.get()=="" or hinext.get()=="" or engtext.get()=="" or OStext.get()=="":
        Label(root2,text="Please Enter the Marks",font="Chiller 20").place(x=80,y=100)
    elif int(pytext.get())>100 or int(OStext.get())>100 or int(Matext.get())>100 or int(hinext.get())>100 or int(engtext.get())>100 or int(OStext.get())>100:  
        Label(root2,text="Opps Smothing Went Wrong ",font="Chiller 20").place(x=80,y=100)
    else:
        sum= int(pytext.get())+int(OStext.get())+int(Matext.get())+int(hinext.get())+int(engtext.get())+int(OStext.get())
        per=((sum/600)*100)
        Label(root2,text=sum,font=20,bg="white").place(x=200,y=100)
        Label(root2,text=per,font=20,bg="white").place(x=200,y=150)
        Label(root2,text="Total marks =",font=20,bg="white").place(x=70,y=100)
        Label(root2,text="Percentage =",font=20,bg="white").place(x=70,y=150)
    
    root2.mainloop()
        
    

    
root=Tk()
root.title('MARK SHEET')
root.geometry("800x770")
root.configure(bg="lavender")
root.resizable(False, False)


label1=Label(root, text="Result Submission Form", font="Stencil 20", bg="lavender").place(x=250,y=20)


label2=Label(root,text="Enter the marks of each subjects  :",font="Calibri 17", bg="lavender").place(x=50,y=90)



label3=Label(root,text="1. Python :",font="Calibri 15", bg="lavender",fg="#000000").place(x=150,y=170)

label4=Label(root,text="2. Multimedia Animation :",font=" Calibri 15", bg="lavender",fg="#000000").place(x=150,y=240)

label5=Label(root,text="3. Operation System :",font="Calibri 15", bg="lavender",fg="#000000").place(x=150,y=310)

label6=Label(root,text="4.  English :",font="Calibri 15", bg="lavender",fg="#000000").place(x=150,y=380)

label7=Label(root,text="3. Hindi :",font="Calibri 15", bg="lavender",fg="#000000").place(x=150,y=450)

label5=Label(root,text="3. OEC :",font="Calibri 15", bg="lavender",fg="#000000").place(x=150,y=520)



pytext=Entry(root,text="",font=15,width=20)
pytext.place(x=450,y=170)
Matext=Entry(root,font=15,width=20)
Matext.place(x=450,y=240)

OStext=Entry(root,font=15,width=20)
OStext.place(x=450,y=310)
engtext=Entry(root,font=15,width=20)
engtext.place(x=450,y=380)
hinext=Entry(root,width=20,font=15,)
hinext.place(x=450,y=450)
oectext=Entry(root,width=20,font=15)
oectext.place(x=450,y=520)



Button(text="View Result",font="Calibri",command=Result ,bg="White").place(x=320,y=650)

Button(text="  Clear  ",font="Calibri",bg="White",width=10,command=Clear).place(x=500,y=645)



root.mainloop()

