#include <SPI.h>

#define SLAVE_SELECT 53


struct MotorPins {
  int in1, in2, in3, in4;
};

MotorPins motors[4] = {
  {8, 9, 10, 11},
  {4, 5, 6, 7},
  {25, 24, 23, 22},
  {29, 28, 27, 26}
};

int brightness = 0;
bool led_state = false;
float currentAngle[4] = {0, 0, 0, 0};

const float angles[9] = {-180, -135, -90, -45, 0, 45, 90, 135, 180};
const uint8_t states[9][4] = {
  {0,1,0,1}, 
  {0,1,0,0},
   {1,1,0,0},
    {1,0,0,0},
  {1,0,1,0}, 
  {0,0,1,0}, 
  {0,0,1,1},
   {0,0,0,1}, 
   {0,1,0,1}
};

void setPinsForMotor(int motor, float angle) {
  int best = 0;
  float minDiff = 999;
  
  for(int i = 0; i < 9; i++) {
    if(fabs(angle - angles[i]) < minDiff) {
      minDiff = fabs(angle - angles[i]);
      best = i;
    }
  }
  
  digitalWrite(motors[motor].in1, states[best][0] ? HIGH : LOW);
  digitalWrite(motors[motor].in2, states[best][1] ? HIGH : LOW);
  digitalWrite(motors[motor].in3, states[best][2] ? HIGH : LOW);
  digitalWrite(motors[motor].in4, states[best][3] ? HIGH : LOW);
  
  currentAngle[motor] = angles[best];
}

void resetAllMotors() {
  for(int i = 0; i < 4; i++) setPinsForMotor(i, 0);
}


void readTemp() {
  byte temp1, temp2;
  
  digitalWrite(SLAVE_SELECT, LOW);
  delay(1);
  SPI.transfer(1);
  delay(1);
  temp1 = SPI.transfer(0);
  delay(1);
  digitalWrite(SLAVE_SELECT, HIGH);
  delay(1);

 
  digitalWrite(SLAVE_SELECT, LOW);
  delay(1);
  SPI.transfer(2);  
  delay(1); 
  temp2 = SPI.transfer(0);
  delay(1);
  digitalWrite(SLAVE_SELECT, HIGH);
  
 
  Serial.print("Sensor 1 (ADS1115) : ");
  Serial.print(temp1);
  Serial.println(" C");
  Serial.print("Sensor 2 (UNO) : ");  
  Serial.print(temp2);
  Serial.println(" C");
}



void setup() {
  SPI.begin();
  pinMode(SLAVE_SELECT, OUTPUT);
  digitalWrite(SLAVE_SELECT, HIGH);
  Serial.begin(9600);
  

  for(int i = 0; i < 4; i++) {
    pinMode(motors[i].in1, OUTPUT);
    pinMode(motors[i].in2, OUTPUT);
    pinMode(motors[i].in3, OUTPUT);
    pinMode(motors[i].in4, OUTPUT);
    resetAllMotors();
  }
  
  pinMode(3, OUTPUT);  
  
  Serial.println("Master Ready!");
}

void loop() {
  if(Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    cmd.toUpperCase();
    
  
    if(cmd.startsWith("M")) {
      int motor = cmd[1] - '1';
      int idx1 = cmd.indexOf('_');
      int idx2 = cmd.lastIndexOf('_');
      
      String dir = cmd.substring(idx1+1, idx2);
      float angle = cmd.substring(idx2+1).toFloat();
      
      if(dir == "L") angle = -angle;
      float newAngle = currentAngle[motor] + angle;
      
      while(newAngle > 180) newAngle -= 360;
      while(newAngle < -180) newAngle += 360;
      
      setPinsForMotor(motor, newAngle);
      Serial.print("Motor ");
      Serial.print(motor+1);
      Serial.print(" = ");
      Serial.println(currentAngle[motor]);
    }
    
   
    else if(cmd.startsWith("ALL_")) {
      if(cmd == "ALL_HOME") {
        resetAllMotors();
        Serial.println("Reset done");
      } else {
        int idx = cmd.indexOf('_', 4);
        String dir = cmd.substring(4, idx);
        float angle = cmd.substring(idx+1).toFloat();
        if(dir == "L") angle = -angle;
        
        for(int i = 0; i < 4; i++) {
          float newAngle = currentAngle[i] + angle;
          while(newAngle > 180) newAngle -= 360;
          while(newAngle < -180) newAngle += 360;
          setPinsForMotor(i, newAngle);
        }
        Serial.println("All motors done");
      }
    }
    
   
    else if(cmd == "LED_ON") {
      for(int i = 0; i <= 255; i++) {
        analogWrite(3, i);
        delay(5);
      }
      led_state = true;
      Serial.println("LED ON");
    }
    else if(cmd == "LED_OFF") {
      for(int i = 255; i >= 0; i--) {
        analogWrite(3, i);
        delay(5);  
      }
       led_state = false;
      Serial.println("LED OFF");
    }
    
  
    else if(cmd == "TEMP") {
   readTemp();
    }
    

    else if(cmd == "STATUS") {
        if(led_state){
           Serial.println("LED IS ON 💡");
        }else{ Serial.println("LED IS OFF 🔌");}
         readTemp();
        Serial.println("-----------------------------");
      for(int i = 0; i < 4; i++) {
        Serial.print("M");
        Serial.print(i+1);
        Serial.print(": ");
        Serial.println(currentAngle[i]);
      }
       Serial.println("-----------------------------");
    }
        else if (cmd == "RESET") {
      resetAllMotors();
      Serial.println("Reset all motors to 0°");
      Serial.println("TARGET = 0.0");
      Serial.println("All motors done");
    }
    else {
      Serial.println("ERRORRR");
    }
  }
}