#include <TimerOne.h>

// traffic lights - R, Y, G
int traffic1[] = {22, 23, 25};
int traffic2[] = {30, 31, 32};
int traffic3[] = {38, 39, 40};
int traffic4[] = {46, 47, 48};

volatile int trig[] = {12, 11, 9, 7};
volatile int echo[] = {13, 10, 8, 6};

volatile int distance[4] = {0, 0, 0, 0};
volatile long duration;

int distance_required = 20;

int yellowdelay = 5000;
int greendelay = 6000;
int reddelay = 3000;

unsigned long lane1Timer = 0;
unsigned long lane2Timer = 0;
unsigned long lane3Timer = 0;
unsigned long lane4Timer = 0;

const unsigned long laneDuration = 60000; // 1 minute

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Timer1.initialize(10000000);
  Timer1.attachInterrupt(detection);
  for (int i = 0; i <= 2; i++) {
    pinMode(traffic1[i], OUTPUT);
    pinMode(traffic2[i], OUTPUT);
    pinMode(traffic3[i], OUTPUT);
    pinMode(traffic4[i], OUTPUT);
  }

  for (int i = 0; i <= 3; i++) {
    pinMode(trig[i], OUTPUT);
    pinMode(echo[i], INPUT);
  }
}

void loop() {
  if (distance_required >= distance[0]) {
    trafficlane1();
  }

  if (distance_required >= distance[1]) {
    trafficlane2();
  }

  if (distance_required >= distance[2]) {
    trafficlane3();
  }

  if (distance_required >= distance[3]) {
    trafficlane4();
  }
}

void detection() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(trig[i], LOW);
    delayMicroseconds(2);
    digitalWrite(trig[i], HIGH);
    delayMicroseconds(10);
    digitalWrite(trig[i], LOW);
    duration = pulseIn(echo[i], HIGH);
    distance[i] = (duration * 0.0343) / 2;

    Serial.print("S");
    Serial.print(i + 1);
    Serial.print(": ");
    Serial.print(distance[i]);
    Serial.print("cm   ");
    Serial.flush();
  }
  Serial.println("");
}

void trafficlane1() {
  clear();
  Serial.println("LANE 1 is ON!!");
  digitalWrite(traffic1[0], LOW);
  digitalWrite(traffic1[2], HIGH);
  
  if (millis() - lane1Timer >= laneDuration) {
    digitalWrite(traffic1[2], LOW);
    digitalWrite(traffic1[1], HIGH);
    delay(yellowdelay);
  } else {
    lane1Timer = millis();
    delay(greendelay);
  }
}

void trafficlane2() {
  clear();
  Serial.println("LANE 2 is ON!!");
  digitalWrite(traffic2[0], LOW);
  digitalWrite(traffic2[2], HIGH);

  if (millis() - lane2Timer >= laneDuration) {
    digitalWrite(traffic2[2], LOW);
    digitalWrite(traffic2[1], HIGH);
    delay(yellowdelay);
  } else {
    lane2Timer = millis();
    delay(greendelay);
  }
}

void trafficlane3() {
  clear();
  Serial.println("LANE 3 is ON!!");
  digitalWrite(traffic3[0], LOW);
  digitalWrite(traffic3[2], HIGH);

  if (millis() - lane3Timer >= laneDuration) {
    digitalWrite(traffic3[2], LOW);
    digitalWrite(traffic3[1], HIGH);
    delay(yellowdelay);
  } else {
    lane3Timer = millis();
    delay(greendelay);
  }
}

void trafficlane4() {
  clear();
  Serial.println("LANE 4 is ON!!");
  digitalWrite(traffic4[0], LOW);
  digitalWrite(traffic4[2], HIGH);

  if (millis() - lane4Timer >= laneDuration) {
    digitalWrite(traffic4[2], LOW);
    digitalWrite(traffic4[1], HIGH);
    delay(yellowdelay);
  } else {
    lane4Timer = millis();
    delay(greendelay);
  }
}

void clear() {
  for (int i = 1; i < 3; i++) {
    digitalWrite(traffic1[i], LOW);
    digitalWrite(traffic2[i], LOW);
    digitalWrite(traffic3[i], LOW);
    digitalWrite(traffic4[i], LOW);
  }

  digitalWrite(traffic1[0], HIGH);
  digitalWrite(traffic2[0], HIGH);
  digitalWrite(traffic3[0], HIGH);
  digitalWrite(traffic4[0], HIGH);
}
