import tkinter
import customtkinter

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Window
        self.title('Gesture Guesser')         #Rename this to the name of the project
        self.geometry('1200x800')
        i = 0
        while (i < 12):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)
            i+=1
        
        # Widgets
        self.title = customtkinter.CTkLabel(self, text='Change the Gesture-Map')
        self.title.grid(row=0, column=0, columnspan=12, rowspan=1, sticky="ew")

        # Buttons
        self.savebutton = customtkinter.CTkButton(self, text="Save", command=self.saveButton)
        self.savebutton.grid(row=11, column=6, padx=20, pady=20, columnspan=6, sticky="ew")
        self.cancelbutton = customtkinter.CTkButton(self, text="Cancel", command=self.cancelButton)
        self.cancelbutton.grid(row=11, column=0, padx=20, pady=20, columnspan=6, sticky="ew")

        # Create Map Frame
        self.gestures = ["Z", "O", "Swipe"]
        self.maps = ["CNTL+Z", "LEFT-MOUSE", "ALT-TAB"]
        self.mapframe = customtkinter.CTkFrame(self)
        self.mapframe.grid(row=1, column=0, padx=20, pady=20, columnspan=12, rowspan=10, sticky="nsew")
        i = 0
        while (i < 12):
            self.mapframe.grid_columnconfigure(i, weight=1)
            self.mapframe.grid_rowconfigure(i, weight=1)
            i+=1

        # Objects Inside Frame
        self.gesturelabel = customtkinter.CTkLabel(self, text='Gestures')
        self.gesturelabel.grid(row=1, column=1, columnspan=5, rowspan=1, sticky="ew")
        self.maplabel = customtkinter.CTkLabel(self, text='Maps')
        self.maplabel.grid(row=1, column=6, columnspan=5, rowspan=1, sticky="ew")
        self.gesture = customtkinter.CTkOptionMenu(self.mapframe, values=self.gestures, command=self.handleGestureChange)
        self.gesture.grid(row=2, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )
        self.map = customtkinter.CTkOptionMenu(self.mapframe, values=self.maps, command=self.handleMapChange)
        self.map.grid(row=2, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )


    def saveButton(self):
        print("Saved New Mapping")

    def cancelButton(self):
        print("Cancelled New Mapping")

    def handleGestureChange(self, val1):
        print("Gesture Changed!")

    def handleMapChange(self, val1):
        print("Map for Gesture Changed!")
