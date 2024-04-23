#define button 4
#define buzz 5

bool cheker = false;
bool linecheker = false;
bool buttonState = false;
bool lastButtonState = false;

const int pause_value = 500;  //vremenski razmak za unosenja signala
long signal_length = 0;
long pause = 0;
long lastDebounceTime = 0;
long debounceDelay = 20;

String morse = "";
String dash = "-";
String dot = "*";
String Text = "";

void setup() {
  Serial.begin(9600);
  pinMode(button, INPUT);
  pinMode(buzz, OUTPUT);
  Serial.println("\n Press button to start making Morse code");
}

void loop() {
  buttonState = digitalRead(button)==HIGH;
  Serial.println("jaje1 ");
  if (buttonState && lastButtonState) {      //provjera stanja predhodnog signala
    Serial.print("jaje2 ");
    signal_length++;
    if (signal_length < 2 * pause_value) tone(buzz, 1500);
    else tone(buzz, 1000);
  }
  else if (!buttonState && lastButtonState) {         //aktivira se kada se posalje * ili _
    if ((signal_length > debounceDelay) && (signal_length < 2 * pause_value )) morse += dot;
    else if (signal_length > 2 * pause_value) morse += dash;
    signal_length = 0;
    digitalWrite(13, LOW);
    noTone(buzz);
    Serial.print("koka ");
  }
  else if (buttonState && !lastButtonState) {   //aktivira se kada se resetiraju vrijednosti
    pause = 0;
    digitalWrite(13, HIGH);
    cheker = true;
    linecheker = true;
  }
  else if (!buttonState && !lastButtonState)  {
    ++pause;
    if (( pause > 3 * pause_value ) && (cheker)) {
      print_it(morse);
      cheker = false;
      morse = "";
    }
    if ((pause > 10 * pause_value) && (linecheker)) {
      Serial.println();
      linecheker = false;
    }
  }
  lastButtonState = buttonState;
  delay(10);
}

void print_it(String Code) {
  if (Code == "*-")    Text += "A";
  else if (Code == "-***")    Text += "B";
  else if (Code == "-*-*")    Text += "C";
  else if (Code == "-**")    Text += "D";
  else if (Code == "*")    Text += "E";
  else if (Code == "**-*")    Text += "F";
  else if (Code == "--*")    Text += "G";
  else if (Code == "****")    Text += "H";
  else if (Code == "**")    Text += "I";
  else if (Code == "*---")    Text += "J";
  else if (Code == "-*-")    Text += "K";
  else if (Code == "*-**")    Text += "L";
  else if (Code == "--")    Text += "M";
  else if (Code == "-*")    Text += "N";
  else if (Code == "---")    Text += "O";
  else if (Code == "*--*")    Text += "P";
  else if (Code == "--*-")    Text += "Q";
  else if (Code == "*-*")    Text += "R";
  else if (Code == "***")    Text += "S";
  else if (Code == "-")    Text += "T";
  else if (Code == "**-")    Text += "U";
  else if (Code == "***-")    Text += "V";
  else if (Code == "*--")    Text += "W";
  else if (Code == "-**-")    Text += "X";
  else if (Code == "-*--")    Text += "Y";
  else if (Code == "--**")    Text += "Z";
  else if (Code == "*----")    Text += "1";
  else if (Code == "**---")    Text += "2";
  else if (Code == "***--")    Text += "3";
  else if (Code == "****-")    Text += "4";
  else if (Code == "*****")    Text += "5";
  else if (Code == "-****")    Text += "6";
  else if (Code == "--***")    Text += "7";
  else if (Code == "---**")    Text += "8";
  else if (Code == "----*")    Text += "9";
  else if (Code == "-----")    Text += "0";
  else if (Code == "*-*-*-") {
    Serial.println(Text);
    Text = "";
  }
Code = "";
}