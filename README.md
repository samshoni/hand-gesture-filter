# Hand Gesture Filter - Real-Time OpenCV Project

A real-time hand gesture recognition system that applies various image filters to a user-defined frame region created by hand gestures.

## Demo

![Hand Gesture Filter Demo](images/Screenshot%20from%202025-11-04%2012-13-08.png)

*The application detects hand gestures and applies real-time filters (Grayscale, Inverted, Blur, Edge Detection) inside the hand-formed frame region.*

## Features

- **Real-time hand detection** using MediaPipe
- **Hand frame gesture recognition** - form a rectangle with your hands to create a filter frame
- **4 powerful filters**:
  - 🖤 Grayscale: Black and white effect
  - ⚫⚪ Inverted: Inverted colors
  - 🌫️ Blur: Powerful Gaussian blur (51x51 kernel)
  - 🔍 Edge Detection: Canny edge detection
- **Auto-switching filters** every 4 seconds
- **Manual filter control** with keyboard shortcuts
- **Real-time processing** at 30 FPS without GPU

## Requirements

- Python 3.8+
- Ubuntu 22.04 (or any Linux/Mac/Windows with Python)
- Webcam
- OpenCV
- MediaPipe
- NumPy

## Installation

### Step 1: Clone Repository

git clone https://github.com/YOUR_USERNAME/hand-gesture-filter.git
cd hand-gesture-filter

text

### Step 2: Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

text

### Step 3: Install Dependencies

pip install -r requirements.txt

text

Or manually:

pip install opencv-python mediapipe numpy

text

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

1. Run the application
2. Position your hands in front of the webcam
3. **Form a rectangular frame** with your index fingers and thumbs from both hands
4. The selected filter will be applied **only inside the frame**
5. Area outside the frame remains **normal and unfiltered**
6. Use arrow keys or SPACE to manually switch between filters
7. **Filters automatically change every 4 seconds**

## Project Structure

hand-gesture-filter/
├── gesture_filter.py # Main application (150 lines)
├── hand_detector.py # Hand detection using MediaPipe (50 lines)
├── filters.py # Filter implementations (80 lines)
├── config.py # Configuration settings (20 lines)
├── requirements.txt # Python dependencies
├── README.md # This file
├── .gitignore # Git ignore rules
├── images/ # Screenshots and demos
│ └── Screenshot from 2025-11-04 12-13-08.png
└── venv/ # Virtual environment

text

## File Descriptions

### gesture_filter.py
Main application controller containing:
- `HandGestureFilterApp` class - core application logic
- Frame detection logic - detects hand gesture forming rectangle
- Real-time UI rendering - displays filter name and controls
- Auto-filter switching - changes filter every 4 seconds
- Keyboard event handling - manual filter control

### hand_detector.py
MediaPipe hand detection wrapper:
- Initializes MediaPipe Hands solution
- Detects 21 hand landmarks per hand
- Draws hand skeleton visualization
- Extracts XY coordinates for hand points

### filters.py
Image filter implementations:
- `apply_grayscale()` - converts to black and white
- `apply_inverted()` - inverts pixel colors
- `apply_blur()` - Gaussian blur with 51x51 kernel
- `apply_edge_detection()` - Canny edge detection
- All filters return BGR format for consistency

### config.py
Configuration parameters:
- MediaPipe detection confidence thresholds
- Filter parameters (blur kernel size, Canny edge thresholds)
- Frame visual settings (color, thickness)
- Available filters list

## Technical Implementation

### Hand Frame Detection Algorithm
1. Detect 21 hand landmarks using MediaPipe for each hand
2. Extract thumb (landmark 4) and index finger (landmark 8) positions from both hands
3. Calculate Euclidean distance between hand pairs
4. If distance > 50 pixels, recognize as "frame gesture"
5. Create polygon mask using thumb and index positions as corners

### Filter Application Process
1. Create binary mask for the frame region
2. Extract pixels inside the frame boundary
3. Apply selected filter to extracted region
4. Use `np.where()` to blend filtered region with original background
5. Avoid white screen issue by proper masking and blending

### Performance Optimization
- Uses pre-trained MediaPipe models (lightweight)
- Runs on CPU without GPU acceleration
- Processes 30 FPS on standard laptop hardware
- Efficient masking using NumPy operations

## Customization

### Change Blur Strength

Edit `config.py` and modify `BLUR_KERNEL`:

BLUR_KERNEL = (51, 51) # Current: very strong blur
Other options:
BLUR_KERNEL = (21, 21) # Light blur
BLUR_KERNEL = (35, 35) # Medium blur
BLUR_KERNEL = (71, 71) # Extremely strong blur


### Change Auto-Switch Time

Edit `gesture_filter.py` and modify `filter_change_interval`:

self.filter_change_interval = 4.0 # Time in seconds
Options:
2.0 # Switch every 2 seconds
4.0 # Switch every 4 seconds (current)
6.0 # Switch every 6 seconds



## Learning Outcomes

This project demonstrates:
- ✅ **Real-time Computer Vision** with OpenCV
- ✅ **Hand Pose Estimation** using pre-trained ML models (MediaPipe)
- ✅ **Image Processing** techniques (masking, blending, filtering)
- ✅ **Event-driven Programming** with keyboard controls
- ✅ **Object-Oriented Design** with clean architecture
- ✅ **Python Software Development** best practices
- ✅ **Git & GitHub** version control workflow

## Resume Highlights

Perfect talking points for interviews:

> "Developed real-time hand gesture recognition system using MediaPipe detecting 21 hand landmarks with 0.7 detection confidence, achieving 30 FPS processing on CPU."

> "Implemented 4 image filters (Grayscale, Inverted, Blur, Edge Detection) with dynamic region-based masking using OpenCV and NumPy, ensuring filtered area stays within hand-formed frame boundaries."

> "Created modular Python architecture with separate classes for detection, filtering, and application logic, following SOLID principles and best practices."

> "Solved color inversion overflow issue by implementing proper mask-based blending with np.where() instead of cv2.add(), eliminating white screen artifacts."

## Future Enhancements

- 🎬 Video recording with applied filters and export
- 🖼️ More filters (Sepia, HSV, Cartoon, Thermal, Night Vision)
- 📱 Multi-hand gesture support (different filters per hand)
- 🎨 GUI interface with filter preview thumbnails
- 🚀 ROS2 Humble integration for robotics applications
- 🎯 Gesture-based drawing application
- ⚡ Performance metrics display (FPS counter, latency)
- 🔄 Filter chaining (apply multiple filters sequentially)

## Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Programming language |
| **OpenCV 4.8** | Image processing and video capture |
| **MediaPipe 0.10** | Hand pose estimation and detection |
| **NumPy 1.24** | Numerical operations and array manipulation |
| **Git** | Version control |

## Author

**Sam** - Robotics & Automation Engineer
- 📍 Location: Changanacherry, Kerala, India
- 🎓 Final year student
- 🤖 Focus: ROS2 Humble, Autonomous Systems, Computer Vision
- 💻 Skills: Python, C++, OpenCV, MediaPipe, Arduino, ROS2

## License

MIT License - Open source and free to use!

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...

text

See LICENSE file for details.

## Acknowledgments

- **MediaPipe** - Google's hand detection models and framework
- **OpenCV** - Open source computer vision library
- **Python Community** - Excellent libraries and documentation

## Contributing

Found a bug? Have suggestions? Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Contact & Support

- GitHub: [github.com/samshoni](https://github.com/samshoni)

---

**Project Status**: ✅ Complete and tested on Ubuntu 22.04 with ROS2 Humble

**Last Updated**: November 4, 2025

For bugs, suggestions, or collaboration, feel free to create an issue or reach out!

⭐ **If you found this project useful, please consider giving it a star!**
