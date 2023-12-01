import customtkinter
import json

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
        self.geometry('1200x850')
        for i in range(12):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        # Widgets
        self.title = customtkinter.CTkLabel(self, text='Change the Gesture-Map (Vision will not work until GUI is closed)')
        self.title.grid(row=0, column=0, columnspan=12, rowspan=1, sticky="ew")

        # Buttons
        self.savebutton = customtkinter.CTkButton(self, text="Save and Close", command=self.saveButton)
        self.savebutton.grid(row=12, column=6, padx=20, pady=20, columnspan=6, sticky="ew")
        self.cancelbutton = customtkinter.CTkButton(self, text="Cancel and Close", command=self.cancelButton)
        self.cancelbutton.grid(row=12, column=0, padx=20, pady=20, columnspan=6, sticky="ew")

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
        self.funcsavebutton.grid(row=10, column=1, padx=20, pady=35, columnspan=3, sticky="ew")
        self.nametextbox = customtkinter.CTkTextbox(self, height=20)
        self.nametextbox.grid(row=10, column=5, padx=20, pady=35, columnspan=3, sticky="ew")
        self.nametextbox.insert('1.0', "Function Name")
        self.commandtextbox = customtkinter.CTkTextbox(self, height=20)
        self.commandtextbox.grid(row=10, column=8, padx=20, pady=35, columnspan=3, sticky="ew")
        self.commandtextbox.insert('1.0', "Keyboard Command")

        # Gave a better name for the GUI, and removed the point up, as that is reserved for mouse movements.
        self.mappings = []
        for i in range(len(self.gestures)):
            label = customtkinter.CTkLabel(self.mapframe, text=self.gestureLabels[i])
            label.grid(row=i+2, column=1, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew")
            self.mappings.append(customtkinter.CTkOptionMenu(self.mapframe, values=self.functions))
            self.mappings[i].grid(row=i+2, column=6, padx=20, pady=20, columnspan=5, rowspan=1, sticky="ew")
            initialValue = self.currentMapping[self.gestures[i]]
            self.mappings[i].set(initialValue)
        # Label to display the instructions
        self.instructions_label = customtkinter.CTkTextbox(self, height = 600, width=400, wrap="word")
        self.instructions_label.grid(row=2, column=15, sticky="ew")
        self.instructions_label.insert('1.0', '''USING THE CUSTOM KEYBOARD COMMAND FUNCTION:

To add a custom keyboard command, enter the command's name into the first text box.

The keys to be pressed go in the second text box.

The format is key+key+key... with no spaces. A couple examples would be a+b+c, ctrl+c, win+r, and alt+tab.

As you can see, non-character keys have special names listed here:

['\\t', '\\n', '\\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']''')   
        self.instructions_label.grid_remove()  # Initially hide the label

        # Button to toggle visibility of instructions
        self.toggle_button = customtkinter.CTkButton(self, text="Toggle Instructions", command=self.toggleInstructions)
        self.toggle_button.grid(row=11, column=3, columnspan=5, sticky="ew")

    def toggleInstructions(self):
        # Toggle the visibility of the instructions label
        if self.instructions_label.winfo_ismapped():
            self.instructions_label.grid_remove()

        else:
            self.instructions_label.grid()
            

    def getMapping(self):
        return self.currentMapping
    
    def getFunctions(self):
        return self.functions
    
    @staticmethod
    def getDefaultMapping():
        # Read from a file, if it does not exist, then this is the default mapping.
        file = open("mapping.txt", "r")
        tempObj = file.readlines()
        if tempObj != []:
            res = tempObj[0].replace("'", '"')
            res = json.loads(res)
            return res
        file.close()
        return {'Closed_Fist': 'Do Nothing',
                'Open_Palm': 'Do Nothing',
                'Thumb_Down': 'Do Nothing',
                'Thumb_Up': 'Do Nothing',
                'Victory': 'Do Nothing',
                'ILoveYou': 'Do Nothing'}
    
    @staticmethod
    def setDefaultMapping(mapObj):
        file = open("mapping.txt", "w")
        file.write(str(mapObj))
        file.close()
        return
    
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
        self.setDefaultMapping(self.currentMapping)
        self.destroy()

    def cancelButton(self):
        print("Cancelled New Mapping")
        self.destroy()      

    def saveFunction(self):
        functionName = self.nametextbox.get('1.0', customtkinter.END)
        functionName = functionName[0 : -1]

        functionCommand = self.commandtextbox.get('1.0', customtkinter.END)
        functionCommand = functionCommand[0 : -1]

        returnVal = self.keyboardInteraction.createNewFunction(functionName, functionCommand, True)
        
        if (returnVal < 0):
            return
        
        print("Success: Added function '%s'" % functionName)
        
        self.functions.append(functionName)

        for mapping in self.mappings:
            mapping.configure(values=self.functions)