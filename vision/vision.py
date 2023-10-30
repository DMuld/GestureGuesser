import mediapipe as mp
import cv2
import time
import dataclasses
from gui.gui import GUI
from keyboardinteraction.keyboardinteraction import KeyboardInteraction
# from collections import deque
import pyautogui

# Stolen from MediaPipe source code
@dataclasses.dataclass
class DrawingSpecs:
    # Color for drawing the annotation. Default to the white color
    color: (int, int, int) = (224, 224, 224)
    # Thickness for drawing the annotation. Default to 2 pixels
    thickness: int = 2
    # Circle radius. Default to 2 pixels
    circle_radius: int = 2

class Vision():
    def __init__(self):
        super().__init__()

        # Gets the default mapping
        self.visionMapping = GUI.getDefaultMapping()

        # Because we now have custom commands, we need to keep track of them
        self.functions = GUI.getDefaultFunctions()

        # Gets your video capture device
        self.vid = cv2.VideoCapture(0)
        if (not self.vid.isOpened()):
            print("Error: video capture not detected")
            exit()

        # Options for constructing the gesture recognizer object
        # "process_results" is the callback function for the async function "recognize_async"
        # The callback function is where we can actually process the results
        options = mp.tasks.vision.GestureRecognizerOptions(
            base_options=mp.tasks.BaseOptions(model_asset_path='./vision/gesture_recognizer.task'),
            running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
            result_callback=self.process_result)
        
        # Construct the recognizer
        self.recognizer =  mp.tasks.vision.GestureRecognizer.create_from_options(options)

        # Current frame
        self.frame = None

        # Instructions to draw_landmarks on how to connect the dots
        self.handConnections = mp.solutions.hands.HAND_CONNECTIONS

         # Determined when the function has returned so we can actually draw to the frame
        self.asyncFlag = False

        # The queue of landmarks/coordinates collected when the user is doing a certain gesture
        # self.pointerTrail = deque()

        # These are the current landmarks that the recognizer has detected
        self.currentLandmarks = []

        # The current detected gesture and the last one. Used to detect when there is a change
        self.activeGesture = "None"
        self.lastActiveGesture = "None"

        # Keyboard interaction class
        self.keyboardInteract = KeyboardInteraction()

    def mainloop(self):
        # For the framerate calculation
        frameStart = 0
        frameEnd = 0

        # This is an incrementing variable that needs to be passed to "recognize_async"
        frameNumber = 0

        # Creates window
        cv2.namedWindow("Gesture Guesser")

        # Height and width of the screen
        screenWidth, screenHeight = pyautogui.size()

        # The loop that the vision uses.
        while (self.vid.isOpened()):
            # Read the frame
            success, self.frame = self.vid.read()

            if success:
                # Mirrors the image
                self.frame = cv2.flip(self.frame, 1)
                # Converts it from BGR to RGB
                imgRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                # Makes MediaPipe image object
                image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
                # Starts the actual recognition. Results get passed to "process_results"
                self.recognizer.recognize_async(image, frameNumber)

                # For async function
                frameNumber += 1

                # Get FPS and put it on the frame
                frameEnd = time.time()
                fps = 1/(time.time()-frameStart)
                frameStart = frameEnd
                cv2.putText(self.frame, str(int(fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

                # Instructions
                cv2.putText(self.frame, "'q' to Exit", (10, 420), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
                cv2.putText(self.frame, "'u' for GUI", (10, 460), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

                # Puts the active gesture on the frame
                cv2.putText(self.frame, self.activeGesture, (10, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

                # Creates instructions for draw_landmarks to connect the dots on the pointer trail
                # trailConnections = []
                # for i in range(1,len(self.pointerTrail)):
                #     trailConnections.append((i-1, i))

                # Draws the pointer trail
                # self.draw_landmarks(self.frame, self.pointerTrail, trailConnections, landmark_drawing_spec=DrawingSpecs(color=(0, 255, 0)))

                # See if we should do any keyboard interaction
                self.processGestureToKeys(self.keyboardInteract)

                # if (cv2.getWindowProperty("Gesture Guesser", 0) < 0):
                #     print("Window closed. Exiting.")
                #     break

                if (len(self.currentLandmarks) > 0 and self.activeGesture == "Pointing_Up"):
                    normalizedLocation = self.currentLandmarks[0][8]
                    pyautogui.moveTo(normalizedLocation.x*screenWidth, normalizedLocation.y*screenHeight, _pause=False)
                
                # Makes sure process_results has finsished before we show the frame
                while (not self.asyncFlag):
                    time.sleep(.01)
                self.asyncFlag = False

                # Show the frame
                cv2.imshow('Gesture Guesser', self.frame)
                
                # Reads the keyboard Input.
                key = cv2.waitKey(1)
                if key:

                    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
                    key = key & 0xFF

                    # If key = 'u' open the GUI
                    if key == ord('u'):
                        print("Starting the GUI")
                        guiObj = GUI(self.visionMapping, self.keyboardInteract, self.functions)
                        guiObj.mainloop()
                        self.visionMapping = guiObj.getMapping()
                        self.functions = guiObj.getFunctions()

                    # If key = 'q' end the loop
                    elif key == ord('q'):
                        print("Exit key 'q' pressed")
                        break
            else:
                print("Error: frame reading not successful")
                break
        
        # Cleanup
        self.vid.release()
        cv2.destroyAllWindows()

    # Start processing the current gesture to keyboard inputs
    def processGestureToKeys(self, keyboardInteract: KeyboardInteraction):
        if (self.activeGesture != self.lastActiveGesture):
            self.lastActiveGesture = self.activeGesture
            try:
                action = self.visionMapping[self.activeGesture]
                keyboardInteract.processGesture(action)
            except:
                pass

    # Processes results. Gets called by recognize_async
    def process_result(self, result: mp.tasks.vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):

        # Set current hand landmarks
        self.currentLandmarks = result.hand_landmarks

        # If we have any landmarks, draw them
        if (len(result.hand_landmarks) > 0):
            for landmarkList in result.hand_landmarks:
                self.draw_landmarks(self.frame, landmarkList, self.handConnections)
        
            # Check if the gesture is different, and if so, change activeGesture
            gesture = result.gestures[0][0].category_name
            if(gesture != self.activeGesture):
                if (gesture != "None"): print("%20s%s" % ("Gesture Detected: ", gesture))
                self.activeGesture = gesture
            
            # # If the gesture is pointing up, collect the landmark at the top of the pointer finger and put it into the queue
            # if (gesture == "Pointing_Up"):
            #     # Index 8 represents the coordinates of the tip of the pointer finger
            #     self.pointerTrail.append(result.hand_landmarks[0][8])
            #     # If the queue is too long, remove the first element
            #     if (len(self.pointerTrail) > 20):
            #         self.pointerTrail.popleft()
            # # If the active gesture is not pointing
            # else:
            #     if (len(self.pointerTrail) > 0):
            #         self.pointerTrail.popleft()

        # If there is no detection whatsoever
        else:
            # if (len(self.pointerTrail) > 0):
            #     self.pointerTrail.popleft()
            # If the user quickly moves their hand off screen, the active gesture might still be something other than None
            # If that's the case, set it to None
            if (self.activeGesture != "None"):
                self.activeGesture = "None"
        # Mark our work as done so the main loop can continue
        self.asyncFlag = True

    # Draws landmarks on the frame. From MediaPipe source code, but heavily modified
    def draw_landmarks(self, image, landmark_list,
        connections: [[(int, int)]] = None,
        landmark_drawing_spec: DrawingSpecs = DrawingSpecs(color=(0, 0, 255)),
        connection_drawing_spec: DrawingSpecs = DrawingSpecs()):

        # Gets image dimensions
        imageHeight, imageWidth, _ = image.shape

        # Gets coordinates, converts them to pixel coordinates, and stores them in a dictionary
        index_to_coordinates = {}
        for index, landmark in enumerate(landmark_list):
            landmark_px = self.convertToPixelCoords(landmark.x, landmark.y, imageWidth, imageHeight)
            index_to_coordinates[index] = landmark_px

        # If there are instructions on drawing connections between the landmarks
        if connections:
            # Draws the connections if the start and end landmarks are both visible.
            for connection in connections:
                start_index = connection[0]
                end_index = connection[1]
                cv2.line(image, index_to_coordinates[start_index],
                        index_to_coordinates[end_index], connection_drawing_spec.color,
                        connection_drawing_spec.thickness)
                    
        # Draws landmark points after finishing the connection lines, which is aesthetically better.
        for index, landmark_px in index_to_coordinates.items():
            # White circle border
            circle_border_radius = landmark_drawing_spec.circle_radius + 1
            cv2.circle(image, landmark_px, circle_border_radius, (255, 255, 255),
                    landmark_drawing_spec.thickness)
            # Fill color into the circle
            cv2.circle(image, landmark_px, landmark_drawing_spec.circle_radius,
                    landmark_drawing_spec.color, landmark_drawing_spec.thickness)
                
    # Converts normalized coordinates (from 0-1) to pixel coordinates
    def convertToPixelCoords(self, normalized_x: float, normalized_y: float, image_width: int, image_height: int):
        x = int(normalized_x * image_width)
        y = int(normalized_y * image_height)
        return x, y
