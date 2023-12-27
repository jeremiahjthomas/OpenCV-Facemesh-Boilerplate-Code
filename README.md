# Real-time FaceMesh Visualization with OpenCV

This Python script demonstrates real-time facial landmarks detection and visualization using the FaceMesh model from Mediapipe and OpenCV. The script captures video from a webcam, detects facial landmarks, and overlays them on the video feed.

## Features:
- Utilizes the `mediapipe` library for facial landmarks detection.
- Draws facial landmarks and connections on the video feed using OpenCV.
- The script dynamically adapts to the default video source (0 or 1) based on availability.
- Press 'q' to exit the script.

## Requirements:
- Python 3.x
- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)
- NumPy (`numpy`)

## Usage:
1. Install the required libraries: `pip install opencv-python mediapipe numpy`
2. Run the script: `python script_name.py`
3. Adjust the webcam if needed and observe real-time facial landmarks detection.

## Notes:
- The script uses the FaceMesh model with refined landmarks.
- Detected facial landmarks are drawn on the video feed, including iris connections.
- Customize the drawing specifications to modify the appearance of the landmarks and connections.

Feel free to integrate this script into your applications for facial landmarks visualization or use it as a starting point for further development.
