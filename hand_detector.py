import cv2
import mediapipe as mp
from config import MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE, MAX_HANDS

class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )
    
    def detect_hands(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        return results
    
    def draw_landmarks(self, frame, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )
        return frame
    
    def get_hand_points(self, results, frame_height, frame_width):
        hand_points = []
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                points = []
                for landmark in hand_landmarks.landmark:
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    points.append((x, y))
                hand_points.append(points)
        
        return hand_points
