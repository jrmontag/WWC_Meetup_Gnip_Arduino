/*
Simple way to exercise the serial port


Instructions:
  -open the Serial Montior
  -on startup (or after hitting the reset button, the arduino says hello
  -serial monitor doesn't send on by default; select "Newline" from the dropdown
  -enter any string you want and hit return or click Send  
*/

String buffer = ""; 
char c;

void setup() {
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
    Serial.print("Hello, Arduino here!\n");
}

void loop() {
    echo();
    delay(50);
}

void echo() {
   if (Serial.available() > 0) {
       // read the incoming byte:
       c = (char) Serial.read();
       if (c == '\n') {
           Serial.print(buffer + '\n');
           buffer = "";
       } else {
           buffer += c;
       }
  }
}
