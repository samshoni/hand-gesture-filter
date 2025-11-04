import cv2
import numpy as np
import time
from hand_detector import HandDetector
from filters import FilterProcessor
from config import FILTERS, FRAME_COLOR, FRAME_THICKNESS

class HandGestureFilterApp:
    def __init__(self):
        self.detector = HandDetector()
        self.current_filter_index = 0
        self.frame_vertices = None
        self.last_filter_change_time = time.time()
        self.filter_change_interval = 5.5
    
    def check_frame_gesture(self, hand_points):
        if len(hand_points) < 2:
            return None
        
        hand1_points = hand_points[0]
        hand2_points = hand_points[1]
        
        thumb1 = hand1_points[4]
        index1 = hand1_points[8]
        thumb2 = hand2_points[4]
        index2 = hand2_points[8]
        
        distance = np.sqrt((thumb1[0] - thumb2[0])**2 + (thumb1[1] - thumb2[1])**2)
        
        if distance > 50:
            frame_vertices = np.array([index1, index2, thumb2, thumb1], dtype=np.int32)
            return frame_vertices
        
        return None
    
    def apply_filter_to_region(self, frame, vertices):
        """Apply filter ONLY inside frame - keep outside completely normal"""
        if vertices is None or len(vertices) < 4:
            return frame, None
        
        # Create mask for inside the frame
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [vertices], 255)
        
        # Extract the region inside the frame
        frame_region = frame.copy()
        frame_region[mask == 0] = 0  # Black out outside temporarily
        
        # Apply filter
        filtered_frame = FilterProcessor.apply_filter(frame_region, FILTERS[self.current_filter_index])
        
        # Use np.where to blend properly: 
        # Where mask is white (255), use filtered frame
        # Where mask is black (0), use original frame
        mask_3d = mask[:, :, np.newaxis]  # Convert 2D mask to 3D
        result = np.where(mask_3d == 255, filtered_frame, frame)
        
        return result.astype(np.uint8), vertices
    
    def draw_ui(self, frame, vertices):
        h, w = frame.shape[:2]
        
        if vertices is not None and len(vertices) >= 4:
            cv2.polylines(frame, [vertices], True, FRAME_COLOR, FRAME_THICKNESS)
        
        filter_text = f"Filter: {FILTERS[self.current_filter_index]} (Auto-change in 4s)"
        cv2.putText(frame, filter_text, (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        instructions = [
            "SPACE: Manual Switch | LEFT/RIGHT: Change | ESC: Exit"
        ]
        
        for idx, instruction in enumerate(instructions):
            cv2.putText(frame, instruction, (10, h - 20),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
        
        return frame
    
    def auto_change_filter(self):
        current_time = time.time()
        if current_time - self.last_filter_change_time >= self.filter_change_interval:
            self.current_filter_index = (self.current_filter_index + 1) % len(FILTERS)
            self.last_filter_change_time = current_time
            print(f"Auto-changed to: {FILTERS[self.current_filter_index]}")
    
    def run(self):
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Cannot open webcam")
            return
        
        print("Starting Hand Gesture Filter Application...")
        print("Controls:")
        print("  SPACE: Manual switch to next filter")
        print("  LEFT Arrow: Previous filter")
        print("  RIGHT Arrow: Next filter")
        print("  ESC: Exit")
        print()
        print(f"Available Filters: {', '.join(FILTERS)}")
        print("Filters will auto-change every 4 seconds...")
        print()
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Cannot read frame")
                break
            
            frame = cv2.flip(frame, 1)
            h, w = frame.shape[:2]
            
            results = self.detector.detect_hands(frame)
            hand_points = self.detector.get_hand_points(results, h, w)
            
            frame = self.detector.draw_landmarks(frame, results)
            
            vertices = self.check_frame_gesture(hand_points)
            self.frame_vertices = vertices
            
            if vertices is not None:
                frame, _ = self.apply_filter_to_region(frame, vertices)
            
            frame = self.draw_ui(frame, vertices)
            
            self.auto_change_filter()
            
            cv2.imshow('Hand Gesture Filter', frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                print("Exiting application...")
                break
            elif key == ord(' '):
                self.current_filter_index = (self.current_filter_index + 1) % len(FILTERS)
                self.last_filter_change_time = time.time()
                print(f"Manual change to: {FILTERS[self.current_filter_index]}")
            elif key == 81:
                self.current_filter_index = (self.current_filter_index - 1) % len(FILTERS)
                self.last_filter_change_time = time.time()
                print(f"Changed to: {FILTERS[self.current_filter_index]}")
            elif key == 83:
                self.current_filter_index = (self.current_filter_index + 1) % len(FILTERS)
                self.last_filter_change_time = time.time()
                print(f"Changed to: {FILTERS[self.current_filter_index]}")
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = HandGestureFilterApp()
    app.run()

