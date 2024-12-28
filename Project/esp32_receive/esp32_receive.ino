#include "WiFi.h"
#include <stdlib.h>
#include <WiFiClientSecure.h>
#include <MQTTClient.h>
#include <ArduinoJson.h>
#include "secrets.h"

int receive_count = 0;
bool received_all = false;
int data[4] = { 0 };

String from_mega;

// The MQTT topics that this device should publish/subscribe
#define AWS_IOT_PUBLISH_TOPIC_LANE1 "traffic_monitor/knkn9/traffic_density"
//#define AWS_IOT_PUBLISH_TOPIC_LANE2 "traffic_monitor/lane2/traffic_density"
//#define AWS_IOT_PUBLISH_TOPIC_LANE3 "traffic_monitor/lane3/traffic_density"
//#define AWS_IOT_PUBLISH_TOPIC_LANE4 "traffic_monitor/lane4/traffic_density"

WiFiClientSecure net = WiFiClientSecure();
MQTTClient client = MQTTClient(256);
void connectAWS() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.println("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Configure WiFiClientSecure to use the AWS IoT device credentials
  net.setCACert(AWS_CERT_CA);
  net.setCertificate(AWS_CERT_CRT);
  net.setPrivateKey(AWS_CERT_PRIVATE);

  // Connect to the MQTT broker on the AWS endpoint we defined earlier
  client.begin(AWS_IOT_ENDPOINT, 8883, net);

  // Create a message handler
  client.onMessage(messageHandler);

  Serial.print("Connecting to AWS IOT");

  while (!client.connect(THINGNAME)) {
    Serial.print(".");
    delay(1000);
  }   

  if (!client.connected()) {
    Serial.println("AWS IoT Timeout!");
    return;
  }

  // Subscribe to a topic
  // client.subscribe(AWS_IOT_SUBSCRIBE_TOPIC);

  Serial.println("AWS IoT Connected!");
}

void publishMessage(int lane, float density) {
  Serial.println("Publishing message");
  StaticJsonDocument<200> doc;
  doc["ID"] = millis();
  doc["LANE"] = lane;
  doc["TRAFFIC_DENSITY"] = density;
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer);  // print to client

  if (lane == 1) {
    client.publish(AWS_IOT_PUBLISH_TOPIC_LANE1, jsonBuffer);
  } else if (lane == 2) {
    client.publish(AWS_IOT_PUBLISH_TOPIC_LANE2, jsonBuffer);
  } else if (lane == 3) {
    client.publish(AWS_IOT_PUBLISH_TOPIC_LANE3, jsonBuffer);
  } else {
    client.publish(AWS_IOT_PUBLISH_TOPIC_LANE4, jsonBuffer);
  }
}

void messageHandler(String &topic, String &payload) {
  Serial.println("incoming: " + topic + " - " + payload);

  //  StaticJsonDocument<200> doc;
  //  deserializeJson(doc, payload);
  //  const char* message = doc["message"];
}

void setup() {
  // put your setup code here, to run once:
  Serial2.begin(9600);
  Serial.begin(9600);
  Serial.println("Entering ConnectAWS");
  connectAWS();
  Serial.println("Exiting ConnectAWS");
}

void loop() {

  // float array[4] = {12.1,1.2,3.3,4.5};
  // for(int i= 0; i<4;i++){
  //   publishMessage(i + 1, array[i]);
  //   delay(100);
  // }
  // delay(10000);

  if (Serial2.available() > 0) {
    from_mega = Serial2.readString();
    Serial.println(from_mega);
    float parts[4];  // Array to store the separated parts
    char charArray[from_mega.length() + 1];
    from_mega.toCharArray(charArray, sizeof(charArray));
    // Start tokenizing the input string

    char *token = strtok(charArray, ",");
    int partCount = 0;

    // Iterate through all parts until no more tokens are found or the maximum number of parts is reached
    while (token != NULL) {
      parts[partCount] = atof(token);  // Store the part in the array
      partCount++;
      token = strtok(NULL, ",");  // Get the next token
    }

    // Print the separated parts
    for (int i = 0; i < 4; i++) {
      Serial.println(parts[i]);
      publishMessage(i + 1, parts[i]);
    }

    partCount = 0;
  }
}
