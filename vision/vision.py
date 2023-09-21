import mediapipe as mp
import cv2
import time
import math
import numpy as np
from typing import List, Mapping, Optional, Tuple, Union
import dataclasses
from gui.gui import GUI

@dataclasses.dataclass
class DrawingSpec:
    # Color for drawing the annotation. Default to the white color.
    color: Tuple[int, int, int] = (224, 224, 224)
    # Thickness for drawing the annotation. Default to 2 pixels.
    thickness: int = 2
    # Circle radius. Default to 2 pixels.
    circle_radius: int = 2

class Vision():
    def __init__(self):
        super().__init__()
        self.visionMapping = {}
        vid = cv2.VideoCapture(0)
        
        if (not vid.isOpened()):
            print("Error: video capture not opened")
            exit()

        options = mp.tasks.vision.GestureRecognizerOptions(
            base_options=mp.tasks.BaseOptions(model_asset_path='./vision/gesture_recognizer.task'),
            running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
            result_callback=self.process_result)
        
        recognizer =  mp.tasks.vision.GestureRecognizer.create_from_options(options)
        pTime = 0
        cTime = 0
        timeStamp = 0
        global frame
        global handConnections
        handConnections = mp.solutions.hands.HAND_CONNECTIONS
        global asyncFlag
        asyncFlag = False
        global pointerTrail
        pointerTrail = []
        global activeGesture
        activeGesture = "None"
        cv2.namedWindow("Gesture Guesser")

        # The loop that the vision uses.
        while (vid.isOpened()):
            success, frame = vid.read()

            if success:
                frame = cv2.flip(frame, 1)
                imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
                recognizer.recognize_async(image, timeStamp)
                timeStamp += 1
                cTime = time.time()
                fps = 1/(cTime-pTime)
                pTime = cTime
                cv2.putText(frame, "'q' to Exit", (10, 420), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
                cv2.putText(frame, "'u' for GUI", (10, 460), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
                cv2.putText(frame, str(int(fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
                trailConnections = []
                for i in range(1,len(pointerTrail)):
                    trailConnections.append((i-1, i))

                self.draw_landmarks(frame, pointerTrail, trailConnections, landmark_drawing_spec=DrawingSpec(color=(0, 255, 0)))

                cv2.putText(frame, activeGesture, (10, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
                
                while (not asyncFlag):
                    time.sleep(.01)

                cv2.imshow('Gesture Guesser', frame)

                asyncFlag = False
                
                # Reads the keyboard Input.
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Exit key 'q' pressed")
                    break
                if cv2.waitKey(1) & 0xFF == ord('u'):
                    print("Starting the UI")
                    guiObj = GUI()
                    guiObj.mainloop()
                    newMapping = guiObj.getMapping()
                    if (newMapping != None):
                        print("Vision Mapping Changed: ", newMapping)
                        self.visionMapping = newMapping
            else:
                print("Error: frame reading not successful")
                break
        
        vid.release()
        cv2.destroyAllWindows()

# 
# 
    # We need to find a way to process the green lines. 
# 
# 
    def process_image_to_map():
        print("Need to figure out a way to make ")

    def process_result(self, result: mp.tasks.vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
        global frame
        if (len(result.hand_landmarks) > 0):
            for landmarkList in result.hand_landmarks:
                self.draw_landmarks(frame, landmarkList, handConnections)
        global pointerTrail
        global activeGesture
        if (len(result.gestures) > 0):
            gesture = result.gestures[0][0].category_name
            if(gesture != activeGesture):
                print("Active Gesture:", gesture)
                activeGesture = gesture
            if (gesture == "Pointing_Up"):
                pointerTrail.append(result.hand_landmarks[0][8])
                if (len(pointerTrail) > 15):
                    pointerTrail.pop(0)
            else:
                if (len(pointerTrail) > 0):
                    pointerTrail.pop(0)
        else:
            if (len(pointerTrail) > 0):
                pointerTrail.pop(0)
            if (activeGesture != "None"):
                activeGesture = "None"
                print("Active Gesture:", activeGesture)
        global asyncFlag
        asyncFlag = True

    def draw_landmarks(
        self,
        image: np.ndarray,
        landmark_list,
        connections: Optional[List[Tuple[int, int]]] = None,
        landmark_drawing_spec: Union[DrawingSpec, Mapping[int, DrawingSpec]] = DrawingSpec(color=(0, 0, 255)),
        connection_drawing_spec: Union[DrawingSpec, Mapping[Tuple[int, int], DrawingSpec]] = DrawingSpec()):
        if not landmark_list:
            return
        image_rows, image_cols, _ = image.shape
        idx_to_coordinates = {}
        for idx, landmark in enumerate(landmark_list):
            landmark_px = self.convertToPixelCoords(landmark.x, landmark.y, image_cols, image_rows)
            if landmark_px:
                idx_to_coordinates[idx] = landmark_px
        if connections:
            num_landmarks = len(landmark_list)
            # Draws the connections if the start and end landmarks are both visible.
            for connection in connections:
                start_idx = connection[0]
                end_idx = connection[1]
                if not (0 <= start_idx < num_landmarks and 0 <= end_idx < num_landmarks):
                    raise ValueError(f'Landmark index is out of range. Invalid connection '
                                    f'from landmark #{start_idx} to landmark #{end_idx}.')
                if start_idx in idx_to_coordinates and end_idx in idx_to_coordinates:
                    drawing_spec = connection_drawing_spec[connection] if isinstance(
                        connection_drawing_spec, Mapping) else connection_drawing_spec
                    cv2.line(image, idx_to_coordinates[start_idx],
                            idx_to_coordinates[end_idx], drawing_spec.color,
                            drawing_spec.thickness)
        # Draws landmark points after finishing the connection lines, which is aesthetically better.
        if landmark_drawing_spec:
            for idx, landmark_px in idx_to_coordinates.items():
                drawing_spec = landmark_drawing_spec[idx] if isinstance(
                    landmark_drawing_spec, Mapping) else landmark_drawing_spec
                # White circle border
                circle_border_radius = max(drawing_spec.circle_radius + 1,
                                        int(drawing_spec.circle_radius * 1.2))
                cv2.circle(image, landmark_px, circle_border_radius, (224, 224, 224),
                        drawing_spec.thickness)
                # Fill color into the circle
                cv2.circle(image, landmark_px, drawing_spec.circle_radius,
                        drawing_spec.color, drawing_spec.thickness)
                
    def convertToPixelCoords(self, normalized_x: float, normalized_y: float, image_width: int, image_height: int):
        x_px = min(math.floor(normalized_x * image_width), image_width - 1)
        y_px = min(math.floor(normalized_y * image_height), image_height - 1)
        return x_px, y_px
