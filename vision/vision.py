import numpy as np
import cv2

class Vision():
    def __init__(self, visionToKBIEvent, guiToVisionEvent):
        super().__init__()
        self.videocapture = cv2.VideoCapture(0)       #This can also be a video file if you put a string with the path in it. 
        while True:
            ret, self.frame = self.videocapture.read()
            self.image = np.zeros(self.frame.shape, np.uint8)
            if (ret == False):
                print("ERROR: Issue with retrieving the video frame.")
            cv2.imshow('Frame', self.frame)         #Shows the actual image.
            # cv2.imshow('Frame', self.image)         #Shows the array image.

            if (cv2.waitKey(1) == ord('q')):
                break
            if (cv2.waitKey(1) == ord('u')):
                self.startUI()
            # if ():

            self.imageProcessing()

        self.stopVision(self.videocapture)

    # Stops the webcam and deletes the windows
    def stopVision(vc):
        vc.release()
        cv2.destoryAllWindows()

    # This will add the results to the queue for the backed. This will allow them to know what is up.
    def sendKBInteraction():  
        print("Need to implement the queue to KB interaction class")

    #This will need to be were the actual processing takes place.
    def imageProcessing():
        dosomething = ""
