import pyautogui


class KeyboardInteraction():

    def __init__(self):
        super().__init__()
        self.functDict = {"Press Q": self.press_q,
                          "Press U": self.press_u,
                          "Left Mouse": self.left_mouse,
                          "Right Mouse": self.right_mouse,
                          "Alt+Tab": self.alt_tab,
                          "Ctrl+C": self.ctrl_c,
                          "Ctrl+V": self.ctrl_v,
                          "Do Nothing": self.do_nothing,
                          "Press Enter": self.press_enter,
                          "Press Windows": self.press_windows}
        self.specialKeys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
                            ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                            '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
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
                            'command', 'option', 'optionleft', 'optionright']

    def createNewFunction(self, functionName: str, functionCommand: str, doSave: bool):

        if functionName in self.functDict:
            print("Error: Function name already in use")
            return -1

        args = functionCommand.split('+')

        for arg in args:
            if (len(arg) > 1 and arg not in self.specialKeys):
                print("Error: Invalid key name in sequence")
                return -1

        def newKeyboardFunction():
            print("Custom Command: '" + functionName + "'")
            pyautogui.hotkey(args)

        self.functDict[functionName] = newKeyboardFunction

        # Stores the mappings to a file.
        if (doSave == True):
            file = open("mapping-c.txt", "a")
            # Fix this to allow for the multi-step custom command
            argRet = ""
            for i in range(len(args)):
                argRet = argRet+"+"+str(args[i])
            file.write(functionName+"~"+argRet+"|")
            file.close()
        return 0

    def processGesture(self, action):
        print("%20s" % ("Executing: "), end='')
        self.functDict[action]()

    def alt_tab(self):
        print("Pressing ALT+TAB")
        pyautogui.hotkey('alt', 'tab')

    def do_nothing(self):
        print("Doing Nothing")

    def press_q(self):
        print("Pressing Q")
        pyautogui.press('q')

    def press_u(self):
        print("Pressing U")
        pyautogui.press('u')

    def ctrl_c(self):
        print("Pressing CTRL+C")
        pyautogui.hotkey('ctrl', 'c')

    def ctrl_v(self):
        print("Pressing CTRL+V")
        pyautogui.hotkey('ctrl', 'v')

    def left_mouse(self):
        print("Clicking Left Mouse Button")
        pyautogui.click()

    def right_mouse(self):
        print("Clicking Right Mouse Button")
        pyautogui.click(button='right')

    def press_enter(self):
        print("Pressing Enter")
        pyautogui.press('enter')

    def press_windows(self):
        print("Pressing Windows Key")
        pyautogui.press('win')
