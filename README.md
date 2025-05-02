System Overview
Stage	Description
1. Elevator Door Detection	The camera monitors the elevator door and triggers the robot to enter when it opens.
2. Button Panel Scanning	Once inside, the camera detects the floor buttons and calculates distance to the target button.
3. Arm Control	The robotic arm receives commands to press the button at the calculated distance.
4. Floor Display Reading	The camera scans the display screen inside the elevator to track which floor the elevator is on.
5. Exit Logic	Once the elevator reaches the desired floor, the robot is signaled to exit.

Modules and Scripts
camera.py:	opens webcam stream and lets user capture test images (image processing for number pad and up and down arrows)
distanceestimate.py:	Tracks green-colored objects, estimates distance using bounding box size
main.py:	High-level elevator sequence runner (camera + arm logic)
main2.py:	Alternate minimal test runner
Servo_Pot_Control.ino:	Arduino code to control the servo motor based on angle or potentiometer input

Computer Vision Components
HSV Masking for color detection 
Contour Filtering + minAreaRect to detect buttons
Image matching for numbers


Notes
The system was tailored for a specific elevator layout (button positions and screen formats), improving an already existing project. The codes on this repo are only for the arm and computer vision parts of the project.
This controls a robotic arm to push an elevator button with image processing and ROS. The test images used for the project are present in the folder test images. 
The complete project allows the robot to press elevator buttons, detect the status of the door, check the floor number, and move out of the elevator when needed. This project was done to improve the mobile robot to enable it to move across floors in the university.
