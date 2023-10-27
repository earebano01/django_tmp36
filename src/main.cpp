
#include "DHT.h"

#define DHTPIN 22 
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println(F("DHT11 test!"));
  dht.begin();
}

void loop() {
  delay(10000);
  float hum = dht.readHumidity();
  float cel = dht.readTemperature();
  float fhr = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(hum) || isnan(cel) || isnan(fhr)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(fhr, hum);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(cel, hum, false);

  // humidity
  Serial.print(hum);
  Serial.print(F(", "));

  // celsius
  Serial.print(cel);
  Serial.print(F(", "));

  // fahrenheit
  Serial.print(fhr);
  Serial.print(F(", "));
  
  //heat index celsius
  Serial.print(hic);
  Serial.print(F(", "));

  //heat index fahrenheit
  Serial.println(hif);
}
