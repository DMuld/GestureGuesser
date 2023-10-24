import customtkinter

class GUI(customtkinter.CTk):
    def __init__(self, mapping, keyboardInteraction, functions):
        super().__init__()

        # Mappings
        self.gestures = ["Closed_Fist", "Open_Palm", "Thumb_Down",
                         "Thumb_Up", "Victory", "ILoveYou"]
        self.gestureLabels = ["Closed Fist", "Open Palm", "Thumb Down",
                              "Thumb Up", "Victory", "I Love You"]
        self.functions = functions
        self.currentMapping = mapping
        self.keyboardInteraction = keyboardInteraction

        # Window
        self.title('Gesture Guesser') # Rename this to the name of the project
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

        # Button and fields to save new keyboard function
        self.funcsavebutton = customtkinter.CTkButton(self, text="Save New Function", command=self.saveFunction)
        self.funcsavebutton.grid(row=10, column=1, padx=20, pady=20, columnspan=3, sticky="ew")
        self.nametextbox = customtkinter.CTkTextbox(self, height=20)
        self.nametextbox.grid(row=10, column=5, padx=20, pady=20, columnspan=3, sticky="ew")
        self.nametextbox.insert('1.0', "Function Name")
        self.commandtextbox = customtkinter.CTkTextbox(self, height=20)
        self.commandtextbox.grid(row=10, column=8, padx=20, pady=20, columnspan=3, sticky="ew")
        self.commandtextbox.insert('1.0', "Keyboard Command (Read readme.md)")

        # Gave a better name for the GUI, and removed the point up, as that is reserved for mouse movements.
        self.mappings = []
        for i in range(len(self.gestures)):
            label = customtkinter.CTkLabel(self.mapframe, text=self.gestureLabels[i])
            label.grid(row=i+2, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew")
            self.mappings.append(customtkinter.CTkOptionMenu(self.mapframe, values=self.functions))
            self.mappings[i].grid(row=i+2, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew")
            initialValue = self.currentMapping[self.gestures[i]]
            self.mappings[i].set(initialValue)

    def getMapping(self):
        return self.currentMapping
    
    def getFunctions(self):
        return self.functions
    
    @staticmethod
    def getDefaultMapping():
        return {'Closed_Fist': 'Do Nothing',
                'Open_Palm': 'Do Nothing',
                'Thumb_Down': 'Do Nothing',
                'Thumb_Up': 'Do Nothing',
                'Victory': 'Do Nothing',
                'ILoveYou': 'Do Nothing'}
    
    @staticmethod
    def getDefaultFunctions():
        return ["Do Nothing", "Left Mouse", "Right Mouse", "Alt+Tab", "Ctrl+C",
                "Ctrl+V", "Press Q", "Press U", "Press Enter", "Press Windows"]
    
    def printMappings(self):
        print('-'*26)
        for i in range(len(self.gestures)):
            print("%12s: %s" % (self.gestureLabels[i], self.currentMapping[self.gestures[i]]))
        print('-'*26)

    def saveButton(self):    
        print("Saved New Mapping:")
        for i in range(len(self.mappings)):
            self.currentMapping[self.gestures[i]] = self.mappings[i].get()
        self.printMappings()
        self.destroy()

    def cancelButton(self):
        print("Cancelled New Mapping")
        self.destroy()        

    def saveFunction(self):
        functionName = self.nametextbox.get('1.0', customtkinter.END)
        functionName = functionName[0 : -1]

        functionCommand = self.commandtextbox.get('1.0', customtkinter.END)
        functionCommand = functionCommand[0 : -1]

        returnVal = self.keyboardInteraction.createNewFunction(functionName, functionCommand)

        if (returnVal == -1):
            print("Error: Could not add keyboard function")
            return
        
        self.functions.append(functionName)

        for mapping in self.mappings:
            mapping.configure(values=self.functions)