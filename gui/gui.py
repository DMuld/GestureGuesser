import customtkinter

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Mappings
        self.gestureToCommandMap = {}
        self.gestures = ["Closed_Fist", "Open_Palm", "Pointing_Up",
                         "Thumb_Down", "Thumb_Up",
                         "Victory", "ILoveYou"]
        self.maps = ["Do Nothing", "Left Mouse", "Right Mouse", "Alt+Tab", "Ctrl+C", "Ctrl+V", "Press Q"]
        # self.defaultMap = {self.gestures[i]:self.maps[i] for i in range(len(self.gestures))}
        self.defaultMap = GUI.getDefaultMapping()

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

        # Gave a better name for the GUI, and removed the point up, as that is reserved for mouse movements.
        self.mappings = []
        self.mappingsToName = {}
        self.mappingsToName['Closed_Fist'] = "Closed Fist"
        self.mappingsToName['Open_Palm'] = "Open Palm"
        self.mappingsToName['Thumb_Down'] = "Thumb Down"
        self.mappingsToName['Thumb_Up'] = "Thumb Up"
        self.mappingsToName['Victory'] = "Peace Sign"
        self.mappingsToName['ILoveYou'] = "I Love You"
        self.gestures.remove('Pointing_Up')
        for i in range(len(self.gestures)):
            label = customtkinter.CTkLabel(self.mapframe, text=self.mappingsToName[self.gestures[i]])
            label.grid(row=i+2, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew")
            self.mappings.append(customtkinter.CTkOptionMenu(self.mapframe, values=self.maps, command=self.handleMapChange))
            self.mappings[i].grid(row=i+2, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew")

    def getMapping(self):
        return self.defaultMap
    
    @staticmethod
    def getDefaultMapping():
        return {'Closed_Fist': 'Do Nothing',
                'Open_Palm': 'Do Nothing',
                'Pointing_Up': 'Do Nothing',
                'Thumb_Down': 'Do Nothing',
                'Thumb_Up': 'Do Nothing',
                'Victory': 'Do Nothing',
                'ILoveYou': 'Do Nothing'}

    def saveButton(self):    
        print("Saved New Mapping")
        print(self.defaultMap)
        self.destroy()

    def cancelButton(self):
        print("Cancelled New Mapping")
        self.destroy()
        return None
    
    def handleMapChange(self, value):
        print("Map for Gesture Changed!")
        print("Map", value)
        for i in range(len(self.mappings)):
            if (value == self.mappings[i].get()):
                self.defaultMap[self.gestures[i]] = value
        