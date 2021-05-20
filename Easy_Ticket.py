from tkinter import *
from tkinter import messagebox
# Creating the GUI frame
root = Tk()
root.title("Easy Ticket")
root.geometry("550x550")
root.config(bg="blue")
root.resizable(height=False, width=False)

# Creating a class
class TicketSales:
    def __init__(self, window):
# Cell--> Label And Entry
        self.label1 = Label(window, text="Enter Your Cell Number :")
        self.label1.place(x=5, y=5)
        self.entry1 = Entry(window, bg='red', fg='white')
        self.entry1.place(x=200, y=5)

# Ticket Catergory--> Label And Entry
        self.label2 = Label(window, text="Select Ticket Catergory:")
        self.label2.place(x=5, y=60)
        self.variable = StringVar()
        self.variable.set("Select Ticket")
        self.entry2 = OptionMenu(window, self.variable, 'Soccer', 'Movie', 'Theater')
        self.entry2.place(x=200, y=60)

# Number of Tickets --> Label And Entry
        self.label3 = Label(window, text="Number Of Tickets Bought :")
        self.label3.place(x=5, y=130)
        self.entry3_spinbox = Spinbox(window, from_=0, to_=10, width=10)
        self.entry3_spinbox.place(x=200, y=130)

# Calculate Button --> Label And Entry
        self.calbut = Button(window, text="Calculate Ticket", bg="red", borderwidth=4, command=self.calculate)
        self.calbut.place(x=100, y=200)

# Clear Button --> Label And Entry
        self.clearbut = Button(window, text="Clear Entries", bg="red", borderwidth=4, command=self.clear)
        self.clearbut.place(x=280, y=200)

# Top And Bottom Border --> Label And Entry
        self.border1 = Label(window, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="white")
        self.border2 = Label(window, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="white")
        self.border1.place(y=260)
        self.border2.place(y=450)

# Amount --> Label And Place
        self.amount = Label(window, text="", bg="red", fg='white')
        self.amount.place(x=50, y=300)

        self.reserve = Label(window, text="", bg="red", fg='white')
        self.reserve.place(x=50, y=350)

# Cell --> Label And Place
        self.cell = Label(window, text='', bg='red', fg='white')
        self.cell.place(x=50, y=400)
# Defining A Calculation for Soccer, Movie and Theater Tickets
    def calculate(self):
        ticket_no = int(self.entry3_spinbox.get())
        vat = 0.14
        try:
            int(self.entry1.get())
            if len(self.entry1.get()) < 10 or len(self.entry1.get()) > 10:
                raise ValueError

            elif self.variable.get() == "Select Ticket":
                raise ValueError

            elif int(self.entry3_spinbox.get()) == 0:
                raise ValueError

# For Soccer
            elif self.variable.get() == "Soccer":
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount.config(text=text)

# For Movie
            elif self.variable.get() == "Movie":
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount.config(text=text)

# For Theater
            elif self.variable.get() == "Theater":
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount.config(text=text)

# Reservation appears after first details are put in.
            reserve_text = "Reservation for {} for : {} ".format(self.variable.get(), ticket_no)
            cell_text = "Reservation Made By: {}".format(self.entry1.get())
            self.reserve.config(text=reserve_text)
            self.cell.config(text=cell_text)
# Pops up when incorrect values are inserted
        except ValueError:  # Error Message
            messagebox.showerror(message="INVALID - Please Try Again")

    def clear(self):
        self.entry1.delete(0, END)
        self.entry1.focus()
        self.variable.set("Select Ticket")
        self.entry3_spinbox.delete(0, END)
        self.entry3_spinbox.insert(0, 0)
        self.amount.config(text="")
        self.reserve.config(text="")
        self.entry1.config(text="")


TicketSales(root)
root.mainloop()
