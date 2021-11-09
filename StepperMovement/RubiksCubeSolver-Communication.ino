
#include <AccelStepper.h>
int maxspeed = 10000;
int accel = 3500;

// Define a stepper and the pins it will use
AccelStepper M1(1,12,11);
AccelStepper M2(1,8,7);
AccelStepper M3(1,6,5);
AccelStepper M4(1,4,3);
AccelStepper M5(1,2,22);
AccelStepper M6(1,23,24);

// Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5

void setup()
{  

  // Change these to suit your stepper if you want
  M1.setMaxSpeed(maxspeed);
  M1.setAcceleration(accel);
  M2.setMaxSpeed(maxspeed);
  M2.setAcceleration(accel);
  M3.setMaxSpeed(maxspeed);
  M3.setAcceleration(accel);
  M4.setMaxSpeed(maxspeed);
  M4.setAcceleration(accel);
  M5.setMaxSpeed(maxspeed);
  M5.setAcceleration(accel);
  M6.setMaxSpeed(maxspeed);
  M6.setAcceleration(accel);

  //This ah
  M1.moveTo(100);
  M2.moveTo(100);
  M3.moveTo(100);
  M4.moveTo(100);
  M5.moveTo(100);   
  M6.moveTo(100);
}

void loop()
{
    // If at the end of travel go to the other end
   
    M1.run();
    M2.run();
    M3.run(); 
    M4.run();
    M5.run();
    M6.run();
}
