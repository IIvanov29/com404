from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Gui")

        self.cacti1_image = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\cactus1.png")
        self.cacti2_image = PhotoImage(file="U:\Programming\com404\\2-guis\\4-images\\cactus2.png")

        self.__add_main_frame()
        self.__add_heading_label()
        self.__add_cactus_image_label()
        self.__add_flip_button()


    def __add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.pack()
        self.main_frame.configure(highlightthickness=4,highlightbackground="black",bg="white")

    def __add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0,column=0,columnspan=3)
        self.heading_label.configure(text="Cactus Leaves",background="white", font="Arial 24")

    def __add_cactus_image_label(self):
        self.cactus_image_label = Label(self.main_frame)
        self.cactus_image_label.grid(row=1, column=0, padx=40,pady=10)
        self.cactus_image_label.configure(image=self.cacti1_image , width=300,height=300)
    
    def __add_flip_button(self):
        self.flip_button = Button(self.main_frame)
        self.flip_button.grid(row=2,column=0,pady=5)
        self.flip_button.configure(borderwidth=4,relief=SOLID,highlightcolor="black",background="white",width=10,height=2,text="Flip")
        self.flip_button.bind("<ButtonRelease-1>",self.__change_image)
        self.flip_button.bind("<ButtonRelease-3>",self.__change_image_back)

    def __change_image(self,event):
        self.cactus_image_label.configure(image=self.cacti2_image , width=300,height=300)
    
    def __change_image_back(self,event):
        self.cactus_image_label.configure(image=self.cacti1_image , width=300,height=300)

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()