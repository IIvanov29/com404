from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Newsletter")
        self.configure(height = 180, width = 350,bg="gray")

        self.add_frame()
        self.add_frame1()
        self.add_heading_label()
        self.add_info_label()
        self.add_email_label()
        self.add_entry()
        self.add_button()      
        
        

    def add_heading_label(self):
        self.add_heading_label = Label(self.add_frame)
        self.add_heading_label.grid(row=0,column=0,columnspan=2,pady=10,padx=5)
        self.add_heading_label.configure(font = "Arial 17", text = "RECIEVE OUR NEWSLETTER")

    def add_info_label(self):
        self.add_info_label = Label(self.add_frame)
        self.add_info_label.grid(row=1,column=0,columnspan=2,pady=10)
        self.add_info_label.configure(text = "Please enter your email below to recieve our newsletter.")
    
    def add_frame(self):
        self.add_frame = Frame()
        self.add_frame.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
    
    def add_frame1(self):
        self.add_frame1 = Frame(self.add_frame)
        self.add_frame1.grid(row=3,column=0,columnspan=3,pady=15)
        self.add_frame1.configure(bg="black",height=5,width=300)
    
    def add_email_label(self):
        self.add_email_label = Label(self.add_frame1)
        self.add_email_label.pack(side=LEFT,pady=0)
        self.add_email_label.configure(text="Email:")

    def add_entry(self):
        self.add_entry = Entry(self.add_frame1)
        self.add_entry.pack(side=RIGHT)
        self.add_entry.configure(width=30)
    
    def add_button(self):
        self.add_button = Button(self.add_frame)
        self.add_button.grid(row=4,column=0,columnspan=3)
        self.add_button.configure(text = "Subscribe",bg="#ffdef5" ,height = 1, width = 48)    