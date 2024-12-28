#include "WiFi.h"
#include <stdlib.h>
#include <WiFiClientSecure.h>
#include <MQTTClient.h>
#include <ArduinoJson.h>
#include "secrets.h"

int receive_count = 0;
bool received_all = false;
float data[4] = {0.0};

String from_mega;

// The MQTT topics that this device should publish/subscribe
#define AWS_IOT_PUBLISH_TOPIC_DENSITY "traffic_monitor/knkn9/traffic_density"

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

  Serial.print("Connecting to AWS IoT");

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

int current_id = 1;

void publishMessage(int current_id, float road1, float road2, float road3, float road4) {
  Serial.println("Publishing message");
  StaticJsonDocument<200> doc;
  doc["ID"] = current_id;
  doc["road1"] = road1;
  doc["road2"] = road2;
  doc["road3"] = road3;
  doc["road4"] = road4;
  // Determine the min_road based on the values
  int min_road;
  if (road1 <= road2 && road1 <= road3 && road1 <= road4) {
    min_road = 1;
  } else if (road2 <= road1 && road2 <= road3 && road2 <= road4) {
    min_road = 2;
  } else if (road3 <= road1 && road3 <= road2 && road3 <= road4) {
    min_road = 3;
  } else {
    min_road = 4;
  }
  doc["open"] = min_road;
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer);  // print to client
  client.publish(AWS_IOT_PUBLISH_TOPIC_LANE1, jsonBuffer);
}


void messageHandler(String &topic, String &payload) {
  Serial.println("incoming: " + topic + " - " + payload);
  //  StaticJsonDocument<200> doc;
  //  deserializeJson(doc, payload);
  //  const char* message = doc["message"];
}

void setup() {
  // put your setup code here, to run once:
  Serial2.begin(115200);
  Serial.begin(9600);
  Serial.println("Entering ConnectAWS");
  connectAWS();
  Serial.println("Exiting ConnectAWS");
}

void loop() {
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

    // Publish the separated parts
    if (partCount == 4) {
      publishMessage(current_id++,data[0], data[1], data[2], data[3]);
    }

    partCount = 0;
  }

  // Handle MQTT client events
  client.loop();
}
