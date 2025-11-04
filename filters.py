import cv2
import numpy as np
from config import BLUR_KERNEL, CANNY_THRESHOLD1, CANNY_THRESHOLD2

class FilterProcessor:
    @staticmethod
    def apply_grayscale(frame):
        """Convert to grayscale"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    @staticmethod
    def apply_inverted(frame):
        """Invert colors"""
        return cv2.bitwise_not(frame)
    
    @staticmethod
    def apply_blur(frame):
        """Apply very powerful Gaussian blur"""
        return cv2.GaussianBlur(frame, BLUR_KERNEL, 0)
    
    @staticmethod
    def apply_edge_detection(frame):
        """Detect edges using Canny"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, CANNY_THRESHOLD1, CANNY_THRESHOLD2)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    @classmethod
    def apply_filter(cls, frame, filter_name):
        """Apply selected filter - ALWAYS returns BGR format"""
        filters = {
            "Grayscale": cls.apply_grayscale,
            "Inverted": cls.apply_inverted,
            "Blur": cls.apply_blur,
            "Edge Detection": cls.apply_edge_detection
        }
        
        filter_func = filters.get(filter_name, cls.apply_grayscale)
        result = filter_func(frame)
        
        # Ensure result is always BGR (3 channels)
        if len(result.shape) == 2:
            result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
        
        return result

