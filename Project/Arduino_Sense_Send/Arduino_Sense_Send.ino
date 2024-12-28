#include <TimerOne.h>
#include <SPI.h>
#include "WiFi.h"

#define RST_PIN 5    // Configurable, see typical pin layout above
#define SS_1_PIN 22  // Configurable, take a unused pin, only HIGH/LOW required, must be diffrent to SS 2
#define SS_2_PIN 23  // Configurable, take a unused pin, only HIGH/LOW required, must be diffrent to SS 1
#define SS_3_PIN 24
#define SS_4_PIN 25
byte ssPins[] = { SS_1_PIN, SS_2_PIN, SS_3_PIN, SS_4_PIN };
//int signal1[] = {46,43,42};// Red,yellow,green
//int signal2[] = {40,39,38};
//int signal3[] = {11,12,13};
//int signal4[] = {7,8,9};

int signal1[] = { 7, 8, 9 };
int signal2[] = { 46, 43, 42 };
int signal3[] = { 40, 39, 38 };
int signal4[] = { 11, 12, 13 };
int i;
int redDelay = 5000;
int blueDelay = 4500;
int yellowDelay = 3000;
//int delay_time = 2;
// Ultrasonic sensor pins
volatile int triggerpin1 = 28;
volatile int echopin1 = 29;
volatile int triggerpin2 = 31;
volatile int echopin2 = 30;
volatile int triggerpin3 = 33;
volatile int echopin3 = 32;
volatile int triggerpin4 = 35;
volatile int echopin4 = 34;
volatile long time;           // Variable for storing the time traveled
volatile int S1, S2, S3, S4;  // Variables for storing the distance covered
int t = 7;                    // distance under which it will look for vehicles.
void softInterr();

void setup() {
  Serial.begin(9600);
  Serial1.begin(115200);
  SPI.begin();
  Timer1.initialize(10000);           //Begin using the timer. This function must be called first. "microseconds" is the period of time the timer takes.
  Timer1.attachInterrupt(softInterr);  //Run a function each time the timer period finishes.

  // Declaring LED pins as output
  for (int i = 0; i < 3; i++) {
    pinMode(signal1[i], OUTPUT);
    pinMode(signal2[i], OUTPUT);
    pinMode(signal3[i], OUTPUT);
    pinMode(signal4[i], OUTPUT);
  }
  // Declaring ultrasonic sensor pins as output
  pinMode(triggerpin1, OUTPUT);
  pinMode(echopin1, INPUT);
  pinMode(triggerpin2, OUTPUT);
  pinMode(echopin2, INPUT);
  pinMode(triggerpin3, OUTPUT);
  pinMode(echopin3, INPUT);
  pinMode(triggerpin4, OUTPUT);
  pinMode(echopin4, INPUT);
  Serial.println("Initilaization is Over");
}
void loop() {
  // If there are vehicles at signal 1
  if (S1 < t) {
    signal1Function();
  }
  // If there are vehicles at signal 2
  if (S2 < t) {
    signal2Function();
  }
  // If there are vehicles at signal 3
  if (S3 < t) {
    signal3Function();
  }
  // If there are vehicles at signal 4
  if (S4 < t) {
    signal4Function();
  }
//  while (current_time - previous_time > delay_time) {
//    String data = "";
//    data += String(S1);
//    data += ",";
//    data += String(S2);
//    data += ",";
//    data += String(S3);
//    data += ",";
//    data += String(S4);
//    Serial1.write(data);
//  }
  if (Serial1.availableForWrite()) {
      String data = String(S1) + "," + String(S2) + "," + String(S3) + "," + String(S4);
      Serial1.println(data);
    }
}


void softInterr() {
  // Reading from first ultrasonic sensor
  digitalWrite(triggerpin1, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerpin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerpin1, LOW);
  time = pulseIn(echopin1, HIGH);
  S1 = time * 0.034 / 2;
  Serial.println("Distance from Sensor 1:");
  Serial.println(S1);


  // Reading from second ultrasonic sensor
  digitalWrite(triggerpin2, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerpin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerpin2, LOW);
  time = pulseIn(echopin2, HIGH);
  S2 = time * 0.034 / 2;
  Serial.println("Distance from Sensor 2:");
  Serial.println(S2);

  // Reading from third ultrasonic sensor
  digitalWrite(triggerpin3, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerpin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerpin3, LOW);
  time = pulseIn(echopin3, HIGH);
  S3 = time * 0.034 / 2;
  Serial.println("Distance from Sensor 3:");
  Serial.println(S3);

  // Reading from fourth ultrasonic sensor
  digitalWrite(triggerpin4, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerpin4, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerpin4, LOW);
  time = pulseIn(echopin4, HIGH);
  S4 = time * 0.034 / 2;
  Serial.println("Distance from Sensor 4:");
  Serial.println(S4);
}

void signal1Function() {
  Serial.println("signal 1");
  low();
  // Make RED LED LOW and make Green HIGH for 5 seconds
  digitalWrite(signal1[0], LOW);
  digitalWrite(signal1[2], HIGH);
  delay(redDelay);
  // if there are vehicels at other signals
  if (S2 < t || S3 < t || S4 < t) {
    // Make Green LED LOW and make yellow LED HIGH for 2 seconds
    digitalWrite(signal1[2], LOW);
    digitalWrite(signal1[1], HIGH);
    delay(yellowDelay);
  }
}

void signal2Function() {
  Serial.println("signal 2");
  low();
  digitalWrite(signal2[0], LOW);
  digitalWrite(signal2[2], HIGH);
  delay(redDelay);
  if (S1 < t || S3 < t || S4 < t) {
    digitalWrite(signal2[2], LOW);
    digitalWrite(signal2[1], HIGH);
    delay(yellowDelay);
  }
}

void signal3Function() {
  Serial.println("signal 3");
  low();
  digitalWrite(signal3[0], LOW);
  digitalWrite(signal3[2], HIGH);
  delay(redDelay);
  if (S1 < t || S2 < t || S4 < t) {
    digitalWrite(signal3[2], LOW);
    digitalWrite(signal3[1], HIGH);
    delay(yellowDelay);
  }
}

void signal4Function() {
  Serial.println("signal 4");
  low();
  digitalWrite(signal4[0], LOW);
  digitalWrite(signal4[2], HIGH);
  delay(redDelay);
  if (S1 < t || S2 < t || S3 < t) {
    digitalWrite(signal4[2], LOW);
    digitalWrite(signal4[1], HIGH);
    delay(yellowDelay);
  }
}

// Function to make all LED's LOW except RED one's.
void low() {
  for (int i = 1; i < 3; i++) {
    digitalWrite(signal1[i], LOW);
    digitalWrite(signal2[i], LOW);
    digitalWrite(signal3[i], LOW);
    digitalWrite(signal4[i], LOW);
  }
  for (int i = 0; i < 1; i++) {
    digitalWrite(signal1[i], HIGH);
    digitalWrite(signal2[i], HIGH);
    digitalWrite(signal3[i], HIGH);
    digitalWrite(signal4[i], HIGH);
  }
}
