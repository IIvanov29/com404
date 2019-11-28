from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Gui")

        self.ambulance_image = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\ambulance.gif")
        self.bike_image = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\bike.gif")
        self.plane_image = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\plane.gif")

        self.__add_secondary_frame()
        self.__add_trasnport_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()


    def __add_secondary_frame(self):
        self.secondary_frame = Frame()
        self.secondary_frame.grid(row=1,column=0,columnspan=3)
        self.secondary_frame.configure(highlightthickness=4,highlightbackground="black",bg="white")

    def __add_trasnport_heading_label(self):
        self.transport_heading_label = Label(self.secondary_frame)
        self.transport_heading_label.grid(row=1,column=0,columnspan=3)
        self.transport_heading_label.configure(text="TRANSPORT",background="white", font="Arial 16")
    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label(self.secondary_frame)
        self.ambulance_image_label.grid(row=2, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,height=60,width=60,background="white")

    def __add_bike_image_label(self):
        self.bike_image_label = Label(self.secondary_frame)
        self.bike_image_label.grid(row=2, column=1)
        self.bike_image_label.configure(image=self.bike_image,height=60,width=60,background="white")

    def __add_plane_image_label(self):
        self.plane_image_label = Label(self.secondary_frame)
        self.plane_image_label.grid(row=2, column=2)
        self.plane_image_label.configure(image=self.plane_image,height=60,width=60,background="white")


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()