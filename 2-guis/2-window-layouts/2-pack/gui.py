from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Newsletter")
        self.configure(bg = "#b0a7ad",height = 180, width = 350)


        self.add_frame()
        self.add_heading_label()
        self.add_info_label()
        self.add_frame1()
        self.add_email_label()
        self.add_entry()
        self.add_button()      
        
        

    def add_heading_label(self):
        self.add_heading_label = Label(self.add_frame)
        self.add_heading_label.pack(pady=10,side=TOP)
        self.add_heading_label.configure(font = "Arial 17", text = "RECIEVE OUR NEWSLETTER")

    def add_info_label(self):
        self.add_info_label = Label(self.add_frame)
        self.add_info_label.pack(pady = 15,anchor=N)
        self.add_info_label.configure(text = "Please enter your email below to recieve our newsletter.")

    def add_frame(self):
        self.add_frame = Frame() 
        self.add_frame.pack(pady=10,padx=10)
        self.add_frame.configure( height = 150, width=300)

    def add_frame1(self):
        self.add_frame1 = Frame(self.add_frame)
        self.add_frame1.pack(pady=10)
        self.add_frame1.configure(bg="black",height=5,width=300)

    def add_email_label(self):
        self.add_email_label = Label(self.add_frame1)
        self.add_email_label.pack(side=LEFT)
        self.add_email_label.configure(text="Email:")

    def add_entry(self):
        self.add_entry = Entry(self.add_frame1)
        self.add_entry.pack(side=RIGHT)
        self.add_entry.configure(width=35)
    
    def add_button(self):
        self.add_button = Button(self.add_frame)
        self.add_button.pack(anchor=S,fill = Y)
        self.add_button.configure(text = "Subscribe",bg="#ffdef5" ,height = 1, width = 46)    