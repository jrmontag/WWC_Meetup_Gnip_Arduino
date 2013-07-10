
/*
  Blink LED based on serial input
  Turns on an LED for the specified number of blinks, then shuts it off for 2 seconds.
 
  This example code is in the public domain.
*/

char c;

// Pin 13 has an LED connected on UNO Arduino boards.
// Let's give it a give it a name:
int led = 13;

void setup() {
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
    pinMode(led, OUTPUT);  
}

// the loop routine runs over and over again forever:
void loop() {
    read_serial_input();
    delay(50);
}

void read_serial_input() {
   if (Serial.available() > 0) {
       //creates variable string_value with length 2
       static char string_value[2]; 
       // read the incoming byte
       // we are only reading 1 char, so blinks are only 0-9
       c = (char) Serial.read();
       if (c != '\n') {
         string_value[0]=c;
         // valid string ending 
         string_value[1]='\0';
         int value = atoi(string_value);
         for (int j = 0; j<value; j++) {
             digitalWrite(led, HIGH); // turn the LED on (HIGH is the voltage level)
             delay(300);            
             digitalWrite(led, LOW);  // turn the LED off by making the voltage LOW
             delay(300);           
         } 
         Serial.print("count change\n");
         delay(500);
       }
       else {
         Serial.print("newline\n");
       }
    }
}
