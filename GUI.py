from tkinter import *
import Code_v as q

root=Tk()
root.title("Virtual Assistant")
root.geometry("2000x2000")
root.maxsize(600,600)
root.minsize(600,600)

def query():
    return q.virtual_assistant()


room=PhotoImage(file=r'C:\\Users\\Lenovo\\Documents\\Virtual Assistant\\assistant.png')
room1=Label(image=room)
room1.pack(fill="x")
Label(root,text="Hey!!How can I help you?",fg="white",bg="pink",font="arial 30 bold").place(x=0,y=5)

Button(text = "Ask Something",fg="black",width=20,bg="white",font="bold",command=query).place(x=200,y=550)





root.mainloop()