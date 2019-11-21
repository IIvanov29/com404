from tkinter import *
from tkinter import messagebox
class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Tickets")
        self.configure(width=50,height=300,bg="white")

        self.__add_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()


    def __add_frame(self):
        self.__add_frame = Frame()
        self.__add_frame.pack()
        self.__add_frame.configure(highlightthickness=4,highlightbackground="black",bg="white")
    
    def __add_heading_label(self):
        self.__add_heading_label = Label(self.__add_frame)
        self.__add_heading_label.grid(row=0,column=0,pady=10)
        self.__add_heading_label.configure(text="Entrance Tickets", font="Arial 24",bg="white")
    
    def __add_instruction_label(self):
        self.__add_heading_label = Label(self.__add_frame)
        self.__add_heading_label.grid(row=1,column=0, pady=25,padx=20,sticky="W")
        self.__add_heading_label.configure(text="How many tickets are needed?", font="Arial 16",bg="white")
    def __add_tickets_entry(self):
        self.__add_tickets_entry = Entry(self.__add_frame)
        self.__add_tickets_entry.grid(row=2,column=0, pady=10,padx=20)
        self.__add_tickets_entry.configure(borderwidth=0,highlightthickness=4,highlightbackground="black",width=15,font="Arial 26")

    def __add_buy_button(self):
        self.__add_buy_button = Button(self.__add_frame)
        self.__add_buy_button.grid(row=3,column=0,pady=20)
        self.__add_buy_button.configure(borderwidth=4,relief=SOLID,highlightcolor="black",background="white",width=10,height=2,text="Buy")
        
        self.__add_buy_button.bind("<ButtonRelease-1>",self.__ticket_bought)


    def __ticket_bought(self,event):
        number_of_tickets = self.__add_tickets_entry.get()

        if int(number_of_tickets) == 1:

            messagebox.showinfo("Purchased","Congratulations, you purchased 1 ticket")
        
        elif int(number_of_tickets) > 1:

            messagebox.showinfo("Purchased","Congratulations, you purchased {} tickets".format(number_of_tickets))

        else:

            messagebox.showinfo("Invalid Argument !", "Please enter a valid number of tickets")