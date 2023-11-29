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

# Milestone Progression
## Milestone 1
This started with developing the baseline for the project. The project had the organization setup so that everyone would have their own place to work and reduce the overal number of merge errors that would occur. 

During this stages the tools that would be used where also decided. It would use CustomTKinter for the GUI as it provided a good looking UI that could be made relatively quickly. For the image recognition and the ML library we chose Open-CV and media-pipe. These provided easy integration for our program, had good documentation, and some prebuilt gestures that we could utilize from the beginning. Pyautogui was used for the keyboard interface for our program. 

## Milestone 2
This is where the Image Recognition, the Keyboard Interface, and the GUI were all connected. This provided us with the ability to test out the application as whole and to think about useful features that should be added into these services to better improve the UX. 

This Milestone also fixed some issues with the performace of the vision window. The 'mouse-move-gesture' feature would cause the framerate of the Image Recogntion to drop about 25% of the frames, which made the mouse movements feel unnatural.

## Milestone 3
Most of the issues bugs and nice to have features were added in this Milestone. Firstly, the ability to save the mappings for the users was added. This was a big improvement as everytime the program was started a user would need to re-map all of their gestures which was time consuming and annoying. 

This Milestone allowed for the user to make Custom Macros with a gesture. More specifically, this feature allows users to map a single gesture to a list of user-specified actions. This would be beneficial for long repetitive tasks.  

## Milestone 4
This Milestone was mainly testing the software and reviewing the user experience of the software. The usability team works with individuals outside the team to ask what improvements should be made the GUI. This lead to the development of some small changes to the GUI. 

The user-specified actions were also brought into the GUI so that a user would not need to open the GitHub README.md to figure out how to use the custom mappings. It should be provided by the user in the first place.
