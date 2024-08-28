from tkinter import*
from tkinter  import messagebox
from M import Database


root=Tk()
root.title("win")
root.geometry("500x400")
root.configure(bg="#00cccc")
db = Database('D:/contacts Manager.db')

def populate_list():
            lst_.delete(0,END)
            
            for row in db.fetch():
                 lst_.insert(END,F'{row[0]},{row[1]},{row[2],{row[3]}}') 

def insert():
    if ent_1.get()=='' or ent_2.get()=='' or ent_3.get()=='' or ent_4.get() =='':
        messagebox.showerror("error", "please fill all the blanks")
        return
    db.insert(ent_1.get(),ent_2.get(),ent_2.get(),ent_4.get())
    clear()
    populate_list

def select(event):
    try:
      global record
         
      index=lst_.curselection()
      i=lst_.get(index)
      m=i.split("_")
      ent_1.delete(0,END)
      ent_1.insert(END,m[0])
      ent_2.delete(0,END)
      ent_2.insert(END,m[1])
      ent_3.delete(0,END)
      ent_3.insert(END,m[2])
      ent_4.delete(0,END)
      ent_4.insert(END,m[3])
    except  IndentationError:
        pass
def delete():
    db.remove(record[0])
    clear()
    populate_list()



def insert1():
    # clear()
    n=ent_1.get()
    f=ent_2.get()
    a=ent_3.get()
    p=ent_4.get()  
    print(n,f,a,p)  
    lst_.insert(END,f"{n}_{f}_{a}_{p} ")

        
def clear():
  ent_1.delete(0,END)
  ent_2.delete(0,END)
  ent_3.delete(0,END)
  ent_4.delete(0,END)
def delete_():
    index=lst_.curselection()
    result=messagebox.askyesno("error","enpty")
    if result==TRUE:
        lst_.delete(0,END)

def updata():
    n=ent_1.get()
    f=ent_2.get()
    a=ent_3.get()
    p=ent_4.get()
    index_=lst_.curselection()
    lst_.delete(index_)
    lst_.insert(END,F"{n}_{f}_{a}_{p} ")
    clear()
    

def exit():
    root.destroy()
def show():
    pass


lst_=Listbox(width=80,height=10)
lab_1=Label(root,text="name")
lab_2=Label(root,text="Fname")

lab_3=Label(root,text="Addrese")
lab_4=Label(root,text="Phone")

lab_1.place(x=15,y=10)
ent_1=Entry(root,width=15)
ent_1.place(x=70,y=10)

lab_2.place(x=170,y=10)
ent_2=Entry(root,width=15)
ent_2.place(x=220,y=10)

lab_3.place(x=15,y=50)
ent_3=Entry(root,width=15)
ent_3.place(x=70,y=50)


lab_4.place(x=170,y=50)
ent_4=Entry(root,width=15)
ent_4.place(x=220,y=50)
list_=Listbox(root,width=50,height=10)
list_.place(x=20,y=100)
list_.insert(0,'**************')

btn_1=Button(root,text="insert",width=10,command=insert)
btn_2=Button(root,text="delete",width=10,command=delete_)
btn_2=Button(root,text="delete",width=10,command=populate_list)
btn_3=Button(root,text="updata",width=10,command=updata)
btn_4=Button(root,text="show",width=10,command=show)
btn_5=Button(root,text="clear",width=10,command=clear)
btn_6=Button(root,text="exit",width=10,command=exit)

btn_1.place(x=5,y=300)
btn_2.place(x=110,y=300)
btn_3.place(x=215,y=300)
btn_4.place(x=5,y=350)
btn_5.place(x=110,y=350)
btn_6.place(x=215,y=350)
s=Scrollbar(root)
s.pack(side=LEFT,fill=Y)
list_=Listbox(root,yscrollcommand=s.set)
s.config(command=list_.yview)
list_.bind("<<listboxSelect>>",select)


root.mainloop()