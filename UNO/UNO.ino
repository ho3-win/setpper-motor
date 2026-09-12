#include "ADS1115.h"
#include <SPI.h>
#include <Wire.h>

ADS1115 adc0(ADS1115_DEFAULT_ADDRESS);
byte lm35pin = A0;
const int alertReadyPin = 2;
byte temperature = 0;
int temperature2 = 0;



void setup(){
  Wire.begin();
  Serial.begin(9600);
  

  adc0.initialize();
  adc0.setMode(ADS1115_MODE_SINGLESHOT);
  adc0.setRate(ADS1115_RATE_8);
  adc0.setGain(ADS1115_PGA_1P024);
  pinMode(alertReadyPin, INPUT_PULLUP);
  adc0.setConversionReadyPinMode();
  
 
  pinMode(MISO, OUTPUT);
  SPCR |= _BV(SPE);     
  SPCR |= _BV(SPIE);    

}

ISR(SPI_STC_vect) {
  byte command = SPDR;
  if(command==1){
  SPDR = temperature;
  }
  if(command==2){
SPDR= (byte)temperature2;
  } 
}

void loop(){
 
  adc0.setMultiplexer(ADS1115_MUX_P0_NG);
  adc0.triggerConversion();
  
  while(digitalRead(alertReadyPin) == HIGH);
  
  temperature = adc0.getMilliVolts(true) / 10;
  

  
  int analogValue = analogRead(lm35pin);
float voltage = analogValue * (5.0 / 1023.0);  
temperature2 = (int)(voltage * 100); 
  
  delay(1000);
}