from tkinter import *
import tkinter.messagebox


def add():
    input_text=ent1.get(1.0,"end-1c")
    if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
    else:
            list_box1.insert(END,input_text)
            ent1.delete(1.0,"end")
            
def delete():
    selected=list_box1.curselection()
    list_box1.delete(selected[0])
    
def done():
    selected=list_box1.curselection()
    
    temp=selected[0]

    temp_selected=list_box1.get(selected)
    temp_selected= temp_selected+" ✔"
    
    list_box1.delete(temp)
    list_box1.insert(temp, temp_selected)
    


# My Window Cutmization
todo_window = Tk()
todo_window.title("خلص اللي وراك يا علق")
todo_window.geometry("300x500+1000+75")
todo_window.resizable(False,False)
todo_window.iconbitmap(r"C:\Users\PC\Downloads\listing_icon-icons.com_70928.ico")
todo_window.config(background="#1A5276")

#label
lbl1 = Label(todo_window, text=":الحاجات اللي وراك", font=("Arial",20,"bold"), bg="#1A5276", fg="#F7DC6F")
lbl1.pack()

# Frame
frame_1 = Frame(todo_window, width=290, height=300, bg="#F7DC6F")
frame_1.place(x=5, y=40)

#List box
list_box1 = Listbox(frame_1, width=32, height=17, background="#F7DC6F", foreground="Black",font=("Arial",12))
list_box1.pack()

#text
ent1 = Text(todo_window, height=5, width=41, bg="#F7DC6F", font=("Arial",10))
ent1.place(x= 5, y=370)

lbl2= Label(ent1,text="اتنيل اكتب هنا",background="#1A5276",foreground="#F7DC6F")
lbl2.place(x=214,y=1)

#button
btn1 = Button(todo_window, text="Insert",height=1, width=10, bg="#F7DC6F", fg="#1A5276", command=add)
btn1.place(x=5,y=460)

btn2 = Button(todo_window, text="Delete",height=1, width=10, bg="#F7DC6F", fg="#1A5276", command=delete)
btn2.place(x=111,y=460)

btn3 = Button(todo_window, text="Done",height=1, width=10, bg="#F7DC6F", fg="#1A5276", command=done)
btn3.place(x=217,y=460)

todo_window.mainloop()