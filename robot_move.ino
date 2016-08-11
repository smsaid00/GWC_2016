#include <Servo.h> // Include servo library
 
Servo servoLeft; // Declare left servo signal
Servo servoRight; // Declare right servo signal
void setup() {
  Serial.begin(9600);                        
  servoLeft.attach(13); // Attach left signal to P13
  servoRight.attach(12); // Attach right signal to P12
  servoLeft.writeMicroseconds(1500); // Write 1500 to the left servo
  servoRight.writeMicroseconds(1500); // Write 1500 to the right servo
}  

void forward(){
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
}
void backwards(){
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
}

void right(){
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1700);
  }
void left(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1300);
}

void rest(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);  
}

void loop() {
  // to move clockwise, use values under 1500 (try 1300)
  // to move counter-clockwise, use values over 1500 (try 1700)
 //servoRight.writeMicroseconds(1700);
 //delay(2000);
 
// servoRight.writeMicroseconds(1700);
// servoLeft.writeMicroseconds(1700);

right();
delay(500);
left();
delay(500);


}
