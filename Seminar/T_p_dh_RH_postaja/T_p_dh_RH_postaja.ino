#include "Arduino_SensorKit.h"
#define Environment Environment_I2C
 
float pressure;
 
void setup() {
  Pressure.begin();     //tlak i temperatura
  Oled.begin();      //ekran
  Oled.setFlipMode(true);
  Wire.begin();
  Environment.begin();     //tlak i vlaga zraka
}
 
void loop() {
  Oled.setFont(u8x8_font_chroma48medium8_r); 
  Oled.setCursor(0, 33);
  Oled.print("T: ");  
  Oled.print((Pressure.readTemperature()+Environment.readTemperature())/2);  //usrednjeni iznos temperature od oba senzora
  Oled.println("C");
  Oled.print("p: ");
  Oled.print(Pressure.readPressure());
  Oled.println("Pa");
  Oled.print("dh: ");
  Oled.print(Pressure.readAltitude());
  Oled.println("m");
  Oled.print("RH: ");
  Oled.print(Environment.readHumidity());
  Oled.println("%");
  Oled.refreshDisplay();
 
  delay(2500);
}