Key Features:

NodeMCU Integration: Used NodeMCU with in-built Wi-Fi capabilities to connect sensors to the local network for real-time traffic density monitoring.

MQTT Protocol: Implemented MQTT for low-power, low-bandwidth data transmission between NodeMCU and the cloud server.

AWS Configuration:

DynamoDB: Employed for storing traffic data efficiently.

API Gateway: Configured to route data between NodeMCU and the cloud server.

SageMaker: Utilized for deploying machine learning models to analyze traffic patterns and provide insights.

System Architecture

Sensors: Collect real-time traffic data.

NodeMCU: Gathers sensor data and transmits it to the cloud using MQTT protocol.

Cloud Server:

AWS DynamoDB: Stores traffic data for further processing.

AWS API Gateway: Facilitates communication between the NodeMCU and server.

AWS SageMaker: Processes the stored data using ML models for traffic analysis.

Output: Provides actionable insights on traffic density.
