# from threading import Thread
import multiprocessing
from gui.gui import GUI
from vision.vision import Vision

# Starts the execution of the user interface I think the vision software will need to start that. 
def startGUI(guiToVisionEvent):
    guiObj = GUI(guiToVisionEvent)
    guiObj.mainloop()

def startVision(visionToKBIEvent, guiToVisionEvent):
    visionObj = Vision(visionToKBIEvent, guiToVisionEvent)


# def startKBinput():


# Starting procedure
if __name__ == '__main__':
    visionToKBIEvent = multiprocessing.Event()
    guiToVisionEvent = multiprocessing.Event()

    
    guiObj = multiprocessing.Process(name='guiObj', target=startGUI, args=(guiToVisionEvent,))
    visionObj = multiprocessing.Process(name='visionObj', target=startVision, args=(visionToKBIEvent,guiToVisionEvent,))
    guiObj.start()
    visionObj.start()


# Main loop
# is_running = True
# while (is_running):
    # this will stop when the KB does a command to stop the program.