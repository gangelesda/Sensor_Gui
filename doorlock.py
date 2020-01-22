import Tkinter as tk
import time
from PIL import Image, ImageTk

class Master_Frame(tk.Tk):
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Lock_Screen, Pin_Screen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Lock_Screen)

class Pin_Screen(tk.Frame):
    def digitEnter(self, digit):
        currentPin = self.lbPin["text"]
        if(len(currentPin) < 4):
            self.lbPin.configure(text=currentPin+digit)

    def pinEnter(self, controller):
        if(self.lbPin["text"] == "6790"):
            controller.show_frame(Lock_Screen)

    def makeWidgets(self, controller):
        #Label
        self.lbPin = tk.Label(self, text="", height=2, width=36, bg="#ffffff")

        #Button Definition
        self.one_button = tk.Button(self, text="1", height=5, width=12, command=lambda: self.digitEnter("1"))
        self.two_button = tk.Button(self, text="2", height=5, width=12, command=lambda: self.digitEnter("2"))
        self.three_button = tk.Button(self, text="3", height=5, width=12, command=lambda: self.digitEnter("3"))
        self.four_button = tk.Button(self, text="4", height=5, width=12, command=lambda: self.digitEnter("4"))
        self.five_button = tk.Button(self, text="5", height=5, width=12, command=lambda: self.digitEnter("5"))
        self.six_button = tk.Button(self, text="6", height=5, width=12, command=lambda: self.digitEnter("6"))
        self.seven_button = tk.Button(self, text="7", height=5, width=12, command=lambda: self.digitEnter("7"))
        self.eight_button = tk.Button(self, text="8", height=5, width=12, command=lambda: self.digitEnter("8"))
        self.nine_button = tk.Button(self, text="9", height=5, width=12, command=lambda: self.digitEnter("9"))
        self.zero_button = tk.Button(self, text="0", height=5, width=12, command=lambda: self.digitEnter("0"))
        self.clear_button = tk.Button(self, text="Clear", height=1, width=10, command=lambda: self.lbPin.configure(text=""))
        self.enter_button = tk.Button(self, text="Enter", height=1, width=10, command=lambda: self.pinEnter(controller))
        self.back_button = tk.Button(self, text="Back", height=1, width=10, command=lambda: controller.show_frame(Lock_Screen))

        #Positioning
        self.lbPin.grid(row=0, column=0, columnspan=3, padx=(17,0), pady=(20,15))
        self.one_button.grid(row=1, column=0, padx=(17,0))
        self.two_button.grid(row=1, column=1)
        self.three_button.grid(row=1, column=2, padx=(0,17))
        self.four_button.grid(row=2, column=0, padx=(17,0))
        self.five_button.grid(row=2, column=1)
        self.six_button.grid(row=2, column=2, padx=(0,17))
        self.seven_button.grid(row=3, column=0, padx=(17,0))
        self.eight_button.grid(row=3, column=1)
        self.nine_button.grid(row=3, column=2, padx=(0,17))
        self.zero_button.grid(row=4, column=1)
        self.clear_button.grid(row=5, column=0, padx=(17,0), pady=(15,0))
        self.back_button.grid(row=5, column=1, pady=(15,0))
        self.enter_button.grid(row=5, column=2, pady=(15,0))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#ffffff")
        self.makeWidgets(controller)
      
class Lock_Screen(tk.Frame):
    def makeWidgets(self, controller):
        image_unlock = Image.open("unlock.png")
        image_unlock = image_unlock.resize((300,400), Image.ANTIALIAS)
        photo_unlock = ImageTk.PhotoImage(image_unlock)
        image_lock = Image.open("lock.png")
        image_lock = image_lock.resize((300,400), Image.ANTIALIAS)
        photo_lock = ImageTk.PhotoImage(image_lock)

        self.lbLock = tk.Label(self, image=photo_lock, bg="#ffffff")
        self.lbLock.image = photo_lock
        self.btManual = tk.Button(self, text="Manual", height=1, width=10, command=lambda: controller.show_frame(Pin_Screen))

        self.lbLock.grid(row=0, column=0, columnspan=3, padx=(10,10), pady=(15,10))
        self.btManual.grid(row=1, column=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.makeWidgets(controller)

doorlock_gui = Master_Frame()
doorlock_gui.geometry("320x480")
doorlock_gui.mainloop()


