# Gesture Guesser

Commands to Install:
```
pip install tkinter
pip install customtkinter
pip install opencv-python
pip install mediapipe
pip install pyautogui
```

Command to Run:
```
py -3.10 main.py
```

Important Links:

https://customtkinter.tomschimansky.com/documentation

Things to Note:
When starting the program it will take a second for the Webcam view to show up. 
To start the GUI, click the webcam portal and press 'u' on the keyboard. This will present the GUI and allow users to change the mapping between gestures and commands. 
Once you close the GUI, the vision software will start working again. 
To end the program click the vision software and press 'q'.

Also, if you look at the top right of the vision page, it shows some built-in commands that we could possibly use if the finger tracker is too difficult to implement. 

This project is primarily built for Windows, but it can work on Linux as well with one extra install:

For Debian based distros:
```
sudo apt install python3-tk
```

For Fedora users:
```
sudo dnf install python3-tkinter
```

For Arch users:
```
sudo pacman -S tk
```

<p>&nbsp;</p>

<b>USING THE CUSTOM KEYBOARD COMMAND FUNCTION:</b>

DISCLAIMER: Right now there is no error checking (to be added). Any invalid input will not work, and will most likely NOT give an error message.

To add a custom keyboard command, enter the command's name into the first text box.

The keys to be pressed go in the second text box.

The format is key+key+key... with no spaces. A couple examples would be `a+b+c`, `ctrl+c`, `win+r`, and `alt+tab`.

As you can see, non character keys have special names. To find the names for all non character keys, please consult the pyautogui documentation (https://pyautogui.readthedocs.io/en/latest/keyboard.html) or the list here:

```
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
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
'command', 'option', 'optionleft', 'optionright']
```