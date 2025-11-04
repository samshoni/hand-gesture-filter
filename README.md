# Hand Gesture Filter - Real-Time OpenCV Project

A real-time hand gesture recognition system that applies various image filters to a user-defined frame region created by hand gestures.

## Features

- **Real-time hand detection** using MediaPipe
- **Hand frame gesture recognition** - form a rectangle with your hands to create a filter frame
- **4 powerful filters**:
  - Grayscale: Black and white effect
  - Inverted: Inverted colors
  - Blur: Powerful Gaussian blur (51x51 kernel)
  - Edge Detection: Canny edge detection
- **Auto-switching filters** every 4 seconds
- **Manual filter control** with keyboard shortcuts

## Requirements

- Python 3.8+
- Ubuntu 22.04 (or any Linux/Mac/Windows with Python)
- Webcam
- OpenCV
- MediaPipe
- NumPy

## Installation

### Step 1: Create Virtual Environment

mkdir hand_gesture_filter_project
cd hand_gesture_filter_project
python3 -m venv venv
source venv/bin/activate

text

### Step 2: Install Dependencies

pip install opencv-python mediapipe numpy

text

### Step 3: Clone this Repository

git clone https://github.com/YOUR_USERNAME/hand_gesture_filter.git
cd hand_gesture_filter

text

Or copy the files manually to your project folder.

## Usage

### Run the Application

source venv/bin/activate
python3 gesture_filter.py

text

### Controls

| Key | Action |
|-----|--------|
| **SPACE** | Switch to next filter |
| **LEFT Arrow** | Previous filter |
| **RIGHT Arrow** | Next filter |
| **ESC** | Exit application |

### How to Use

1. Open the application
2. Position your hands in front of the webcam
3. Form a rectangular frame with your index fingers and thumbs
4. The filter will be applied only inside the frame
5. Use arrow keys or SPACE to switch between filters
6. Filters auto-change every 4 seconds

## Project Structure

hand_gesture_filter_project/
├── gesture_filter.py # Main application
├── hand_detector.py # Hand detection using MediaPipe
├── filters.py # Filter implementations
├── config.py # Configuration settings
├── README.md # This file
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment

text

## File Descriptions

### gesture_filter.py
Main application file containing:
- HandGestureFilterApp class
- Frame detection logic
- UI rendering
- Auto-filter switching
- Keyboard controls

### hand_detector.py
MediaPipe hand detection wrapper:
- Hand landmark detection (21 points per hand)
- Hand skeleton visualization
- Point extraction

### filters.py
Image filter implementations:
- Grayscale conversion
- Color inversion
- Gaussian blur
- Edge detection (Canny)

### config.py
Configuration parameters:
- MediaPipe confidence thresholds
- Filter parameters (blur kernel size, Canny thresholds)
- Available filters list

## Customization

### Change Blur Strength

Edit `config.py`:

BLUR_KERNEL = (51, 51) # Change these numbers
Larger = stronger blur
(21, 21) = light blur
(35, 35) = medium blur
(51, 51) = very strong blur

text

### Change Auto-Switch Time

Edit `gesture_filter.py`:

self.filter_change_interval = 4.0 # Time in seconds

text

### Add More Filters

1. Add filter function in `filters.py`
2. Add filter name to FILTERS list in `config.py`
3. Add case in `apply_filter()` method

## Troubleshooting

### Error: "No module named 'cv2'"
- Make sure virtual environment is activated: `source venv/bin/activate`
- Install dependencies: `pip install opencv-python mediapipe numpy`

### Error: "Cannot open webcam"
- Check if webcam is available: `ls /dev/video*`
- Close other applications using webcam
- Try different camera index in gesture_filter.py

### Hand detection not working
- Ensure good lighting
- Keep hands clearly visible in frame
- Increase confidence threshold in config.py if needed

## Resume Points

This project demonstrates:
- ✅ Real-time computer vision with OpenCV
- ✅ Hand pose estimation using pre-trained ML models (MediaPipe)
- ✅ Image processing and filtering techniques
- ✅ Real-time frame masking and blending
- ✅ Event-driven programming
- ✅ Python software architecture
- ✅ Git version control and GitHub workflow

## Future Enhancements

- Add more filters (Sepia, HSV, Cartoon effects)
- Support for multiple hand frames simultaneously
- Video recording with applied filters
- Custom filter creation via GUI
- Performance optimization with threading
- ROS2 integration for robotics applications

## Author

Sam (Robotics & Automation Engineer)
- Location: Changanacherry, Kerala, India
- Preparing for: GATE 2026 Instrumentation Engineering

## License

MIT License - feel free to use and modify

## Acknowledgments

- MediaPipe for hand detection models
- OpenCV for image processing
- Python community

---

**Project Status**: ✅ Working and tested on Ubuntu 22.04

For bugs or suggestions, create an issue on GitHub!
