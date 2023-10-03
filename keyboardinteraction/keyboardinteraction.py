import pyautogui

class KeyboardInteraction():
    
    def __init__(self):
        super().__init__()
        self.functDict = {"Press Q": self.press_q,
                          "Left Mouse": self.left_mouse,
                          "Right Mouse": self.right_mouse,
                          "Alt+Tab": self.alt_tab,
                          "Ctrl+C": self.ctrl_c,
                          "Ctrl+V": self.ctrl_v,
                          "Do Nothing": self.do_nothing}
    
    def processGesture(self, action):
        self.functDict[action]()

    def alt_tab(self):
        print("Pressing ALT+TAB")
        pyautogui.hotkey('alt', 'tab')

    def do_nothing(self):
        print("Doing Nothing")
        pass
    
    def press_q(self):
        print("Pressing Q")
        pyautogui.press('q')

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
