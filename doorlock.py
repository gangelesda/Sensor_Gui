from Tkinter import Tk, Label, Button, W

class MyFirstGUI:
    def makeWidgets(self, master):
        #Button Definition
        self.one_button = Button(master, text="1", height=5, width=12)
        self.two_button = Button(master, text="2", height=5, width=12)
        self.three_button = Button(master, text="3", height=5, width=12)
        self.four_button = Button(master, text="4", height=5, width=12)
        self.five_button = Button(master, text="5", height=5, width=12)
        self.six_button = Button(master, text="6", height=5, width=12)
        self.seven_button = Button(master, text="7", height=5, width=12)
        self.eight_button = Button(master, text="8", height=5, width=12)
        self.nine_button = Button(master, text="9", height=5, width=12)
        self.zero_button = Button(master, text="0", height=5, width=12)

        #Positioning
        self.one_button.grid(row=0, column=0, padx=(17,0), pady=(50,0))
        self.two_button.grid(row=0, column=1, pady=(50,0))
        self.three_button.grid(row=0, column=2, pady=(50,0))
        self.four_button.grid(row=1, column=0, padx=(17,0))
        self.five_button.grid(row=1, column=1)
        self.six_button.grid(row=1, column=2)
        self.seven_button.grid(row=2, column=0, padx=(17,0))
        self.eight_button.grid(row=2, column=1)
        self.nine_button.grid(row=2, column=2)
        self.zero_button.grid(row=3, column=1)

    def __init__(self, master):
        self.master = master
        master.title("Doorlock")

        self.makeWidgets(master)
      

root = Tk()
root.geometry("320x480")
root.configure(bg='#ffffff')

doorlock_gui = MyFirstGUI(root)
root.mainloop()


