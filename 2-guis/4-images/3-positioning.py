from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Gui")

        self.map_image = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\map.png")
        self.bus_image = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\bus1.png")

        self.__add_main_frame()
        self.__add_heading_label()
        self.__add_map_frame()
        self.__add_map_image_label()
        self.__add_bus_image_label()


    def __add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.pack()
        self.main_frame.configure(highlightthickness=4,highlightbackground="black",bg="white")

    def __add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0,column=0,columnspan=3)
        self.heading_label.configure(text="Bus Journey",background="white", font="Arial 24")

    def __add_map_frame(self):
        self.map_frame = Frame(self.main_frame)
        self.map_frame.grid(row=1,column=0,padx=50,pady=20)
        self.map_frame.configure(width=715,height=583)

    def __add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0,y=0)
        self.map_image_label.configure(image=self.map_image)

    def __add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=20,y=20)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind('<B1-Motion>', self.change_bus_position)


    def change_bus_position(self,Event):
        mouse_y = str(Event.y)
        mouse_x = str(Event.x)
       
        self.bus_image_label.place(x=mouse_x,y=mouse_y)


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()