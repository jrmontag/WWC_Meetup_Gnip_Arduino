#include <EL_Escudo.h>

String buffer = ""; 
char c;

void setup() {
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
    //echo();
    readColor();
    delay(50);
}

void light(int x) {
    EL.on(x);
    delay(1500);
    EL.off(x);  
}

void readColor() {
   if (Serial.available() > 0) {
       // read the incoming byte:
       c = (char) Serial.read();
   }
   if (c == 'y') {
      light(Achan);
   } else if (c == 'b') {
      light(Bchan);
   } else if (c == 'o') {
      light(Cchan);
   } else if (c == 'r') {
      light(Dchan);
   }
   Serial.print(c);
   c = 'n';
}

void echo() {
   if (Serial.available() > 0) {
       // read the incoming byte:
       c = (char) Serial.read();
       if (c == '\n') {
           Serial.print(buffer);
           buffer = "";
       } else {
           buffer += c;
       }
  }
}
