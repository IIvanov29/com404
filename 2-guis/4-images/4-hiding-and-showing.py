from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Hotel Check In")
        self.configure(bg="white")
    
        self.successimg = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\success.png")
        self.failedimg = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\failed.png")

        self.__add_frame()
        self.__add_heading_label()

        self.__add_first_entry_label()
        self.__add_first_entry()
        self.__add_checkbox()
        
        self.__add_second_entry_label()
        self.__add_second_entry()
        self.__add_second_checkbox()
       
        self.__add_third_entry_label()
        self.__add_third_entry()
        self.__add_third_checkbox()

        self.__add_check_button()
       
       
     

    def __add_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.configure(highlightthickness=4,highlightbackground="black",bg="white")
    
    def __add_heading_label(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=0,column=0,columnspan=3)
        self.heading_label.configure(text="Hotel Check In", font="Arial 24",bg="white")
    
    def __add_first_entry_label(self):
        self.first_entry_label= Label(self.frame)
        self.first_entry_label.grid(row=1,column=0,pady=7,sticky=W)
        self.first_entry_label.configure(text="Name:", font="Arial 16",bg="white")

    def __add_first_entry(self):
        self.first_entry = Entry(self.frame)
        self.first_entry.grid(row=1,column=1,pady=7)
        self.first_entry.configure(borderwidth=0,highlightthickness=4,highlightbackground="black",width=12,font="Arial 14")
        self.first_entry.bind("<FocusOut>", self.name_check)

    def __add_checkbox(self):
        self.checkbox = Label(self.frame)
        self.checkbox.grid(row=1,column=3,pady=7,padx=4)
        self.checkbox.configure(image=self.failedimg,bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black",height=22,width=25)
       
    def __add_second_entry_label(self):
        self.second_entry_label = Label(self.frame)
        self.second_entry_label.grid(row=2,column=0,pady=7,sticky=W)
        self.second_entry_label.configure(text="Passport Number", font="Arial 16",bg="white")

    def __add_second_entry(self):
        self.second_entry = Entry(self.frame)
        self.second_entry.grid(row=2,column=1,pady=7)
        self.second_entry.configure(borderwidth=0,highlightthickness=4,highlightbackground="black",width=12,font="Arial 14")
        self.second_entry.bind("<FocusOut>", self.passport_num_check)

    def __add_second_checkbox(self):
        self.checkbox1 = Label(self.frame)
        self.checkbox1.grid(row=2,column=3,pady=7,padx=4)
        self.checkbox1.configure(image=self.failedimg,bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black",height=25,width=25)

    def __add_third_entry_label(self):
        self.third_entry_label = Label(self.frame)
        self.third_entry_label.grid(row=3,column=0,pady=7,sticky=W)
        self.third_entry_label.configure(text="No. of nights", font="Arial 16",bg="white")

    def __add_third_entry(self):
        self.third_entry = Entry(self.frame)
        self.third_entry.grid(row=3,column=1,pady=7)
        self.third_entry.configure(borderwidth=0,highlightthickness=4,highlightbackground="black",width=12,font="Arial 14")
        self.third_entry.bind("<FocusOut>", self.num_of_nights_check)

    def __add_third_checkbox(self):
        self.checkbox2 = Label(self.frame)
        self.checkbox2.grid(row=3,column=3,pady=7,padx=4)
        self.checkbox2.configure(image=self.failedimg,bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black",height=25,width=25)

    def __add_check_button(self):
        self.check_button = Button(self.frame)
        self.check_button.grid(row=4,column=0,columnspan=2,pady=7,sticky=E,padx=20)
        self.check_button.configure(borderwidth=4,relief=SOLID,highlightcolor="black",background="white",width=10,height=2,text="Check In")

    def name_check(self,Event):
        if len(self.first_entry.get()) < 1:
            messagebox.showerror("Invalid Information","Name field needs to be filled in.")
        else:
            self.checkbox.configure(image=self.successimg)

    def passport_num_check(self, Event):
        if len(self.second_entry.get()) < 1:
            messagebox.showerror("Invalid Information","Passport number field needs to be filled in.")
        else:
            self.checkbox1.configure(image=self.successimg)
    def num_of_nights_check(self, Event):
        if len(self.third_entry.get()) < 1:
            messagebox.showerror("Invalid Information","Number of Nights needs to be filled in.")
        elif int(self.third_entry.get()) > 365:
            messagebox.showerror("Invalid Information", "Number of nights cannot be more than 365.") 
        else:
            self.checkbox2.configure(image=self.successimg)



if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()