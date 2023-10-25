#include <Arduino.h>

const int ANALOG_PIN = A0;
const int PIN_ANALOG_MAX_VALUE = 1023;

const float PIN_BASE_VOLTAGE = 3.3;
const float TENSION_DECALAGE = 500;

int AnalogValue = 0;
int MvParDegreeCelcius = 10;

float PinVoltage = 0;
float TMP36Temperature = 0;

const int MS_DELAI = 1000;


void setup() {
  Serial.begin(9600);
  pinMode(ANALOG_PIN, INPUT);
}

void loop() {
  AnalogValue = analogRead(ANALOG_PIN);
  PinVoltage = (AnalogValue * PIN_BASE_VOLTAGE) / PIN_ANALOG_MAX_VALUE;
  TMP36Temperature = (PinVoltage * 1000 - TENSION_DECALAGE) / MvParDegreeCelcius;

  Serial.print(TMP36Temperature, 2); 
  Serial.println(" ");

  delay(MS_DELAI);
}
