Key Features:
1. NodeMCU Integration: Used NodeMCU with in-built Wi-Fi capabilities to connect sensors to the local network for real-time traffic density monitoring.
2. MQTT Protocol: Implemented MQTT for low-power, low-bandwidth data transmission between NodeMCU and the cloud server.
3. AWS Configuration:
  i) DynamoDB: Employed for storing traffic data efficiently.
  ii) API Gateway: Configured to route data between NodeMCU and the cloud server.
  iii) SageMaker: Utilized for deploying machine learning models to analyze traffic patterns and provide insights.

*System Architecture*
1. Sensors: Collect real-time traffic data.
2. NodeMCU: Gathers sensor data and transmits it to the cloud using MQTT protocol.
3. Cloud Server:
  i) AWS DynamoDB: Stores traffic data for further processing.
  ii) AWS API Gateway: Facilitates communication between the NodeMCU and server.
  iii) AWS SageMaker: Processes the stored data using ML models for traffic analysis.

