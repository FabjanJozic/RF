int light_sensor = A3;
#define BUZZER 5
#include "Arduino_SensorKit.h"
 
void setup() {
  //Serial.begin(9600); //begin Serial Communication
  pinMode(BUZZER, OUTPUT);
  Oled.begin();
  Oled.setFlipMode(true);
}
 
void loop() {
  int raw_light = analogRead(light_sensor); // read the raw value from light_sensor pin (A3)
  int light = map(raw_light, 0, 1023, 0, 100); // map the value from 0, 1023 to 0, 100
  int buzz = 0;
  if (light < 15) {
  tone(BUZZER, 5); //Set the voltage to high and makes a noise
  delay(100);
  }
  else if (light >= 15 & light < 30) {
  buzz = 15;
  tone(BUZZER, buzz);
  delay(100);
  }
  else if (light >= 30 & light < 45) {
  buzz = 30;
  tone(BUZZER, buzz);
  delay(100);
  }
  else if (light >= 45 & light < 60) {
  buzz = 50;
  tone(BUZZER, buzz); //Set the voltage to high and makes a noise
  delay(100);
  }
  else if (light >= 60 & light < 75) {
  buzz = 75;
  tone(BUZZER, buzz);
  delay(100);
  }
  else if (light > 75) {
  buzz = 100;
  tone(BUZZER, buzz);
  delay(100);
  }
  else {
  noTone(BUZZER);//Sets the voltage to low and makes no noise
  delay(100);
  }

  int random_value = analogRead(A0);   //read value from A0
  Oled.setFont(u8x8_font_chroma48medium8_r); 
  Oled.setCursor(0, 33);    // Set the Coordinates 
  Oled.print("Light level: ");  
  Oled.print(light); // Print the Values 
  Oled.print("\nSound level: ");
  Oled.print(buzz);
  Oled.refreshDisplay();    // Update the Display 
  delay(100);
}


