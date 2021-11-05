# Cube-Solver

This is the repo for my Rubik's Cube Solver robot, in the NJIT Robotics Club.

Currently it consists of main.py, which is the main program used to run the robot. It uses a hardcoded input at the moment, but it will be modified to allow for OpenCV to detect the sides of the cube and automatically input the colors. For installation / usage instructions, see below.

It uses [this library](https://github.com/Wiston999/python-rubik) to calculate a solution for the cube. Because of the restrictions of the algorithm used, the cube must be oriented with the top being yellow and the front being red.

The input as a string must correspond with this unwrapping of the cube, as described in the repository above.

![image](https://user-images.githubusercontent.com/21321412/136248812-0ce28f98-a8eb-423b-bdf9-ed5a264fb2a6.png)


The script generates a solution in cube notation, which we can pass to the Arduino to twist the cube according to the solution.
This Arduino portion hasn't been done yet, but I'll likely keep in this repository as well. The Arduino will wait for data to come in through the serial port, and accept the solution string.

This project is based on an instructibles project you can find [here.](https://www.instructables.com/id/Q-Bot-the-Open-Source-Rubiks-Cube-Solver/)

## Installation

You'll have to download [Python](https://www.python.org/downloads/) and the  [Arduino IDE](https://www.arduino.cc/en/software) in order to run this.

For Python you'll need to install the libraries using these commands:
- `pip install pySerial`
- `pip install rubik_solver`

Note you may need to run this as an administrator.

You'll also need to have the Arduino plugged in with a USB cable to interact with it.

This will also require you selecting the correct Arduino board in the Arduino IDE (We're using the Arduino MEGA) in Tools > Board > Arduino MEGA or MEGA 2560. Notably the other boards in the room are Arduino UNO's.


## Running the Port Test
The Port Test allows you to test the code for sending data from a Python script to the Arduino.

1. Open PortTest/PortTest.ino in the Arduino IDE and upload it into the Arduino MEGA.

1. Run port_test_main.py AFTER the Arduino code is done uploaded to the Arduino.

1. Enter a number into the python shell prompt, and the Arduino's LED should turn on for that many seconds.

It's important to note the port the Arduino IDE uses to upload to the Arduino is the same the Python script uses to communicate to the Arduino. This means you __cannot upload to the board while the python script is running__.

## Running the main Cube Solver code
The main code for the cube solver is currently in main.py.
It contains the code that will run when we run the Cube Solver robot itself.

Currently it consists of the code to input a cube's colors (by typing it out), the code to solve the cube, and it outputs the solution to the cube in step notation.

Ideally we will pass this solution to the Arduino, which will translate each step into a series of stepper movements.

## TODO
- Write boilerplate StepperMovement code in StepperMovement.ino that takes the solution in cube notation, and has a function for each possible step.
- Add Stepper motor testing code to repository
- Re-wire the Arduino to the breadboard
- Create wiring diagram for Arduino / breadboard / stepper motor connections
- Move color detecting code to this repository
