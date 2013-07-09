//
// Simple way to exercise the serial port
//
//

//
// Operation:
//    Open the Serial Montior
//    On startup (or after hitting the reset button, the arduino says hello
//    Enter any string you want after than and hit return
//    Notice that the code on the arduino is looking for a newline char. The 
//    Serial monitor doesn't send on by default.  User the dropdown at the bottom
//    to read "Newline"
//

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
