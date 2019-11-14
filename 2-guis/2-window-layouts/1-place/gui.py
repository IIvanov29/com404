from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Newsletter")
        self.configure(height = 180, width = 350)

        self.add_heading_label()
        self.add_info_label()
        self.add_button()
        self.add_entry()
        self.add_email_label()
        

    def add_heading_label(self):
        self.add_heading_label = Label()
        self.add_heading_label.place(x=10,y=0)
        self.add_heading_label.configure(font = "Arial 17", text = "RECIEVE OUR NEWSLETTER")

    def add_info_label(self):
        self.add_info_label = Label()
        self.add_info_label.place(x = 25, y = 60)
        self.add_info_label.configure(text = "Please enter your email below to recieve our newsletter.")

    def add_frame(self):
        self.add_frame = Frame() 
        self.add_frame.place(x = 10, y = 10)
        self.add_frame.configure(bg = "black", height = 150, width=300)
        
      
    def add_button(self):
        self.add_button = Button()
        self.add_button.place(x=10,y=135)
        self.add_button.configure(text = "Subscribe",bg="#ffdef5" ,height = 1, width = 46)

    def add_entry(self):
        self.add_entry = Entry()
        self.add_entry.place(x = 90, y = 100)
        self.add_entry.configure(width = 30, selectborderwidth = 20,highlightthickness = 0.5,highlightbackground = "Black")
    
    def add_email_label(self):
        self.add_email_label = Label()
        self.add_email_label.place(x = 50, y = 100)
        self.add_email_label.configure(text="Email:")
        