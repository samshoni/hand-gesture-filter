# Hand detection settings
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.5
MAX_HANDS = 2

# Filter settings
BLUR_KERNEL = (51, 51)  # Much larger = much more powerful blur
CANNY_THRESHOLD1 = 100
CANNY_THRESHOLD2 = 200

# Frame settings
FRAME_THICKNESS = 3
FRAME_COLOR = (0, 255, 0)

# Available filters - ONLY 4 filters now
FILTERS = [
    "Grayscale",
    "Inverted",
    "Blur",
    "Edge Detection"
]

