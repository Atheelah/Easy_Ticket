from tkinter import *
root = Tk()
root.title("Easy Ticket")
root.geometry("300x100")
root.config(bg="red")
root.resizable(height=False, width=False)


def nextscreen():
    root.destroy()
    import Easy_Ticket


button1 = Button(root, text="Choose Your Ticket", fg='white', border=4, bg="blue", command=nextscreen)
button1.place(x=60, y=35)


root.mainloop()
