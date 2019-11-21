from tkinter import *
from tkinter import messagebox
class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Passport Checker")
        self.configure(bg="white")

        self.__add_frame()
        self.__add_heading_label()

        self.__add_first_question()
        self.__add_yes_checkbutton_1()
        self.__add_no_checkbutton_1()

        self.__add_second_question()
        self.__add_yes_checkbutton_2()
        self.__add_no_checkbutton_2()

        self.__add_third_question()
        self.__add_yes_checkbutton_3()
        self.__add_no_checkbutton_3()

        self.__add_check_button()

    def __add_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.configure(highlightthickness=4,highlightbackground="black",bg="white")
    
    def __add_heading_label(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=0,column=0,pady=10)
        self.heading_label.configure(text="Passport Checker", font="Arial 24",bg="white")
    
    def __add_first_question(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=1,column=0,sticky=W,padx=2)
        self.heading_label.configure(text="1. Photo matches face?", font="Arial 16",bg="white")

    def __add_yes_checkbutton_1(self):
        global CheckVar1
        CheckVar1 = IntVar()
        self.yes_checkbutton_1 = Checkbutton(self.frame)
        self.yes_checkbutton_1.grid(row=2,column=0,padx=100,sticky=E)
        self.yes_checkbutton_1.configure(text="Yes",bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black",variable=CheckVar1)

    def __add_no_checkbutton_1(self):
        self.yes_checkbutton_1 = Checkbutton(self.frame)
        self.yes_checkbutton_1.grid(row=2,column=0,padx=10,sticky=E)
        self.yes_checkbutton_1.configure(text="No",bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black")    

       
    def __add_second_question(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=3,column=0,sticky=W,padx=10)
        self.heading_label.configure(text="2. Passport has at least 6 months validlity", font="Arial 16",bg="white")

    def __add_yes_checkbutton_2(self):
        global CheckVar2
        CheckVar2 = IntVar()
        self.yes_checkbutton_2 = Checkbutton(self.frame)
        self.yes_checkbutton_2.grid(row=4,padx=100,sticky=E)
        self.yes_checkbutton_2.configure(text="Yes",bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black",variable=CheckVar2)

    def __add_no_checkbutton_2(self):
        self.yes_checkbutton_2 = Checkbutton(self.frame)
        self.yes_checkbutton_2.grid(row=4,column=0,padx=10,sticky=E)
        self.yes_checkbutton_2.configure(text="No",bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black")  
    
       
    def __add_third_question(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=5,column=0,sticky=W,padx=10)
        self.heading_label.configure(text="3. Visa, if required, is valid?", font="Arial 16",bg="white")

    def __add_yes_checkbutton_3(self):
        global CheckVar3
        CheckVar3 = IntVar()
        self.yes_checkbutton_3 = Checkbutton(self.frame)
        self.yes_checkbutton_3.grid(row=6,column=0,padx=100,sticky=E)
        self.yes_checkbutton_3.configure(text="Yes",bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black",variable=CheckVar3)

    def __add_no_checkbutton_3(self):
        self.yes_checkbutton_3 = Checkbutton(self.frame)
        self.yes_checkbutton_3.grid(row=6,column=0,padx=10,sticky=E)
        self.yes_checkbutton_3.configure(text="No",bg="white",relief=SOLID,highlightthickness=4,highlightbackground="black")  

    def __add_check_button(self):
        self.check_button = Button(self.frame)
        self.check_button.grid(row=7,column=0,pady=10)
        self.check_button.configure(borderwidth=4,relief=SOLID,highlightcolor="black",background="white",width=10,height=2,text="Check")
        self.check_button.bind("<ButtonRelease-1>", self.Checking_Passport)


    def Checking_Passport(self,Event):
        
        if CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 1:
            messagebox.showinfo("Successful","Your passport is valid!")
        
        else:
            messagebox.showinfo("Failed", "The passport is invalid!")