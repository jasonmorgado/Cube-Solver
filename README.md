# Cube-Solver
 
This is the repo for my Rubik's Cube Solver robot, in the NJIT Robotics Club.

Currently it consists of main.py, which is the main program used to run the robot. It uses a hardcoded input at the moment, but it will be modified to allow for OpenCV to detect the sides of the cube and automatically input the colors. To test it, run `python main.py`.

It uses [this library](https://github.com/Wiston999/python-rubik) to calculate a solution for the cube. Because of the restrictions of the algorithm used, the cube must be oriented with the top being yellow and the front being red.

The input as a string must correspond with this unwrapping of the cube, as described in the repository above.
![image](https://user-images.githubusercontent.com/21321412/136248812-0ce28f98-a8eb-423b-bdf9-ed5a264fb2a6.png)


The script generates a solution in cube notation, which we can pass to the arduino to twist the cube according to the solution. 
This arduino portion hasn't been done yet, but I'll likely keep in this repository as well. The arduino will wait for data to come in through the serial port, and accept the solution string.

This project is based on an instructibles project you can find [here.](https://www.instructables.com/id/Q-Bot-the-Open-Source-Rubiks-Cube-Solver/)
