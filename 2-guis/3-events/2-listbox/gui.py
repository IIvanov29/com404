from tkinter import *
from tkinter import messagebox
class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Song Maker")
        self.configure(bg="white")

        self.__add_frame()
        self.__add_row_frame()
        self.__add_heading_label()
        self.__add_entry_heading()
        self.__add_lyrics_entry()
        self.__add_lyrics_button()
        self.__add_listbox_heading()
        self.__add_listbox()
    
        


    def __add_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.configure(highlightthickness=4,highlightbackground="black",bg="white")
    
    def __add_heading_label(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=0,column=0,pady=10)
        self.heading_label.configure(text="Song Maker", font="Arial 24",bg="white")
    
    def __add_entry_heading(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=1,column=0,sticky=W,padx=2)
        self.heading_label.configure(text="Lyrics to add:", font="Arial 16",bg="white")

    def __add_row_frame(self):
        self.row_frame = Frame(self.frame)
        self.row_frame.grid(row=3,column=0)
        self.row_frame.configure(bg="white")

    def __add_lyrics_entry(self):
        self.lyrics_entry = Entry(self.row_frame)
        self.lyrics_entry.pack(side=LEFT,padx=5,pady=5)
        self.lyrics_entry.configure(borderwidth=0,highlightthickness=4,highlightbackground="black",width=15,font="Arial 23")

    def __add_lyrics_button(self):
        self.lyrics_button = Button(self.row_frame)
        self.lyrics_button.pack(side=RIGHT,padx=5,pady=5)
        self.lyrics_button.configure(borderwidth=4,relief=SOLID,highlightcolor="black",background="white",width=10,height=2,text="Add")
        self.lyrics_button.bind("<ButtonRelease-1>", self.putting_lyrics_in_listbox)

    def __add_listbox_heading(self):
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=4,column=0,sticky=W,padx=2)
        self.heading_label.configure(text="Lyrics:", font="Arial 16",bg="white")

    def __add_listbox(self):
        self.lyrics_listbox = Listbox(self.frame)
        self.lyrics_listbox.grid(row=6,column=0,pady=10)
        self.lyrics_listbox.configure(borderwidth=0,highlightthickness=4,highlightbackground="black",width=50,height=3,font="Arial 10")

    def putting_lyrics_in_listbox(self,event):

        lyrics = self.lyrics_entry.get()

        self.lyrics_listbox.insert(0,lyrics)

      