int analog_in = 0;
int V_in = 5;
float V_out = 0;
float R_known = 220;
float R = 0;
float temp = 0;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  analog_in = analogRead(A0);
  temp = analog_in*V_in;
  V_out = (temp)/1024.0;
  R = R_known*((V_in/V_out)-1);
  Serial.print("V: ");
  Serial.println(V_out);
  Serial.print("R: ");
  Serial.println(R);
  delay(1000);
}

