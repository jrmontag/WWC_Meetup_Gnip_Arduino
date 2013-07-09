String buffer = ""; 
char c;

/*
  Blink
  Turns on an LED for the specified number of blinks, then shuts it off for 2 seconds.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;


void setup() {
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
    pinMode(led, OUTPUT);  
}

// the loop routine runs over and over again forever:
void loop() {
    //echo();
    readColor();
    delay(50);
}
void readColor() {
   if (Serial.available() > 0) {
       static char string_value[2]; //creates variable string_value with length 2
       // read the incoming byte:
       c = (char) Serial.read(); 
       string_value[0]=c; 
       string_value[1]='\0';
       int value = atoi(string_value);
       for (int j = 0; j<value; j++) {
           digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
           delay(300);               // wait for a second
           digitalWrite(led, LOW);   // turn the LED off by making the voltage LOW
           delay(300);         // wait for a second
       } 
       delay(2000);
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
