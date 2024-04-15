#define Echo_EingangsPin 7 // Echo input pin
#define Trigger_AusgangsPin 8 // Trigger output pin
#define BUZZER 5
#include "Arduino_SensorKit.h"
 
// Required variables are defined
int maximumRange = 300;
int minimumRange = 2;
long distance;
long duration;
 
void setup () {
 pinMode (Trigger_AusgangsPin, OUTPUT);
 pinMode (Echo_EingangsPin, INPUT);
 Serial.begin (9600);
 pinMode(BUZZER, OUTPUT);
 Oled.begin();
 Oled.setFlipMode(true);
}
 
void loop () {
 
 // Distance measurement is started by means of the 10us long trigger signal
 digitalWrite (Trigger_AusgangsPin, HIGH);
 delayMicroseconds (10);
 digitalWrite (Trigger_AusgangsPin, LOW);
  
 // Now we wait at the echo input until the signal has been activated
 // and then the time measured how long it remains activated
 duration = pulseIn (Echo_EingangsPin, HIGH);
 // Now the distance is calculated using the recorded time
 distance = duration / 58.2;
 // Check whether the measured value is within the permissible distance
 if (distance>= maximumRange || distance <= minimumRange)
 {
    // If not, an error message is output.
      Serial.println ("\nDistance outside the measuring range");
      Serial.println ("-----------------------------------");
 }
 else
 {
    // The calculated distance is output in the serial output
      Serial.print ("The distance is:");
      Serial.print (distance);
      Serial.println ("cm");
      Serial.println ("-----------------------------------");
 }
  // Pause between the individual measurements
 if (distance <= 2*minimumRange) {
 tone(BUZZER, 10); //Set the voltage to high and makes a noise
 delay(100);
 }
 else if (distance > 2*minimumRange & distance <= 5*minimumRange) {
 tone(BUZZER, 30);
 delay(100);
 }
 else if (distance > 5*minimumRange & distance <= 10*minimumRange) {
 tone(BUZZER, 80);
 delay(100);
 }
 else {
 noTone(BUZZER);//Sets the voltage to low and makes no noise
 delay(100);
 }
 int random_value = analogRead(A0);   //read value from A0
 Oled.setFont(u8x8_font_chroma48medium8_r); 
 Oled.setCursor(0, 33);    // Set the Coordinates 
 Oled.print("Distance:");  
 Oled.print(distance); // Print the Values 
 Oled.print("cm");
 Oled.refreshDisplay();    // Update the Display 
 delay(100);
}
