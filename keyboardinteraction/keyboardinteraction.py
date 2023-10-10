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
    
    def processGesture(self, action):
        print("%20s" % ("Executing Action: "), end='')
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