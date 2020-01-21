from Tkinter import Tk, Label, Button, W

class MyFirstGUI:
    def makeWidgets(self, master):
        #Label
        self.lbPin = Label(master, text="", height=2, width=36)

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
        self.clear_button = Button(master, text="Clear", height=1, width=10)
        self.enter_button = Button(master, text="Enter", height=1, width=10)

        #Positioning
        self.lbPin.grid(row=0, column=0, columnspan=3, padx=(17,0), pady=(20,15))
        self.one_button.grid(row=1, column=0, padx=(17,0))
        self.two_button.grid(row=1, column=1)
        self.three_button.grid(row=1, column=2)
        self.four_button.grid(row=2, column=0, padx=(17,0))
        self.five_button.grid(row=2, column=1)
        self.six_button.grid(row=2, column=2)
        self.seven_button.grid(row=3, column=0, padx=(17,0))
        self.eight_button.grid(row=3, column=1)
        self.nine_button.grid(row=3, column=2)
        self.zero_button.grid(row=4, column=1)
        self.clear_button.grid(row=5, column=0, padx=(17,0), pady=(15,0))
        self.enter_button.grid(row=5, column=2, pady=(15,0))

    def __init__(self, master):
        self.master = master
        master.title("Doorlock")

        self.makeWidgets(master)
      

root = Tk()
root.geometry("320x480")
root.configure(bg='#ffffff')

doorlock_gui = MyFirstGUI(root)
root.mainloop()


