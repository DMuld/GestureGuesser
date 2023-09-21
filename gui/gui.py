import tkinter
import customtkinter

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Mappings
        self.gestureToCommandMap = {}
        self.gestures = ["Z", "O", "Swipe"]
        self.maps = ["CNTL+Z", "LEFT-MOUSE", "ALT-TAB"]
        self.defaultMap = {self.gestures[i]:self.maps[i] for i in range(len(self.gestures))}

        # Window
        self.title('Gesture Guesser')         #Rename this to the name of the project
        self.geometry('1200x800')
        for i in range(12):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        # Widgets
        self.title = customtkinter.CTkLabel(self, text='Change the Gesture-Map (Vision will not work until GUI is closed)')
        self.title.grid(row=0, column=0, columnspan=12, rowspan=1, sticky="ew")

        # Buttons
        self.savebutton = customtkinter.CTkButton(self, text="Save and Close", command=self.saveButton)
        self.savebutton.grid(row=11, column=6, padx=20, pady=20, columnspan=6, sticky="ew")
        self.cancelbutton = customtkinter.CTkButton(self, text="Cancel and Close", command=self.cancelButton)
        self.cancelbutton.grid(row=11, column=0, padx=20, pady=20, columnspan=6, sticky="ew")

        # Create Map Frame (Where the mapping occurs)
        self.mapframe = customtkinter.CTkFrame(self)
        self.mapframe.grid(row=1, column=0, padx=20, pady=20, columnspan=12, rowspan=10, sticky="nsew")
        for i in range(12):
            self.mapframe.grid_columnconfigure(i, weight=1)
            self.mapframe.grid_rowconfigure(i, weight=1)

        # Objects Inside Frame
        self.gesturelabel = customtkinter.CTkLabel(self, text='Gestures')
        self.gesturelabel.grid(row=1, column=1, columnspan=5, rowspan=1, sticky="ew")
        self.maplabel = customtkinter.CTkLabel(self, text='Maps')
        self.maplabel.grid(row=1, column=6, columnspan=5, rowspan=1, sticky="ew")

        # Doesn't work have todo it statically
        # self.gesture = []
        # self.map = []
        # for i in range(len(self.gestures)):
        #     # Change the gesture to a static value, not a Option menu
        #     self.gesture.append(1)
        #     self.map.append(1)
        #     self.gesture[i] = customtkinter.CTkOptionMenu(self.mapframe, values=self.gestures, command=lambda value: self.handleGestureChange(, value))
        #     self.gesture[i].grid(row=i+2, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )
        #     self.map[i] = customtkinter.CTkOptionMenu(self.mapframe, values=self.maps, command=self.handleMapChange)
        #     self.map[i].grid(row=i+2, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )
        
        # These are for the options menu. Tried doing it dynamically and it wouldn't work. 
        self.gesture1 = customtkinter.CTkLabel(self.mapframe, text=self.gestures[0])
        self.gesture1.grid(row=2, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )
        self.map1 = customtkinter.CTkOptionMenu(self.mapframe, values=self.maps, command=self.handleMap1Change)
        self.map1.grid(row=2, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )

        self.gesture2 = customtkinter.CTkLabel(self.mapframe, text=self.gestures[1])
        self.gesture2.grid(row=3, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )
        self.map2 = customtkinter.CTkOptionMenu(self.mapframe, values=self.maps, command=self.handleMap2Change)
        self.map2.grid(row=3, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )

        self.gesture3 = customtkinter.CTkLabel(self.mapframe, text=self.gestures[2])
        self.gesture3.grid(row=4, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )
        self.map2 = customtkinter.CTkOptionMenu(self.mapframe, values=self.maps, command=self.handleMap3Change)
        self.map2.grid(row=4, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew" )

    def getMapping(self):
        return self.defaultMap

    def saveButton(self):    
        # This needs to return the new mapping.
        print("Saved New Mapping")
        print(self.defaultMap)
        self.destroy()

    def cancelButton(self):
        print("Cancelled New Mapping")
        self.destroy()
        return None
    

    # I know this is bad, I tried to have these as one function, but it won't return the index, so I would have to blindly guess the index.
    def handleMap1Change(self, val1):
        print("Map for Gesture Changed!")
        print("Map", val1)
        self.defaultMap[self.gestures[0]] = val1

    def handleMap2Change(self, val1):
        print("Map for Gesture Changed!")
        print("Map", val1)
        self.defaultMap[self.gestures[1]] = val1

    def handleMap3Change(self, val1):
        print("Map for Gesture Changed!")
        print("Map", val1)
        self.defaultMap[self.gestures[2]] = val1