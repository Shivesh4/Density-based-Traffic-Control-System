# #!/usr/bin/env python3
# from awscrt import io, mqtt, auth, http
# from awsiot import mqtt_connection_builder
# import time as t
# import json
# import uuid
# import random
# from datetime import datetime

# current_id = 331

# def message_gen():
#     global current_id
#     timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
#     # Define the parameters for the pattern
#     duration = 20  # Total duration of the pattern in seconds
#     peak_time = 10  # Time (in seconds) when the traffic is at its peak
#     peak_value = 8  # Maximum traffic value
    
#     # Calculate the traffic values based on the time component
#     time_diff = t.time() % duration  # Current time within the duration
#     if time_diff <= peak_time:
#         traffic_value = (time_diff / peak_time) * peak_value  # Increasing pattern
#     else:
#         traffic_value = ((duration - time_diff) / (duration - peak_time)) * peak_value  # Decreasing pattern
    
#     # timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
#     Road1 = random.randint(2, 5)
#     Road2 = random.randint(0, 7)
#     Road3 = random.randint(0, 8)
#     Road4 = random.randint(0, 4)
#     roads = {
#     1: Road1,
#     2: Road2,
#     3: Road3,
#     4: Road4
#     }
#     min_road = min(roads, key=roads.get)
#     message = {
#         "ID": current_id,
#         # "Timestamp": timestamp,
#         "road1": Road1,
#         "road2": Road2,
#         "road3": Road3,
#         "road4": Road4,
#         "open": min_road,
#     }
#     current_id += 1
#     return message

# # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, TOPIC, and RANGE
# ENDPOINT = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com"
# CLIENT_ID = "traffic_monitor"
# PATH_TO_CERTIFICATE = "./dc.pem"
# PATH_TO_PRIVATE_KEY = "./private.pem"
# PATH_TO_AMAZON_ROOT_CA_1 = "./root.pem"
# TOPIC = "traffic_monitor/knkn9/traffic_density"
# RANGE = 10

# # Spin up resources
# event_loop_group = io.EventLoopGroup(1)
# host_resolver = io.DefaultHostResolver(event_loop_group)
# client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
# mqtt_connection = mqtt_connection_builder.mtls_from_path(
#         endpoint=ENDPOINT,
#         cert_filepath=PATH_TO_CERTIFICATE,
#         pri_key_filepath=PATH_TO_PRIVATE_KEY,
#         client_bootstrap=client_bootstrap,
#         ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
#         client_id=CLIENT_ID,
#         clean_session=False,
#         keep_alive_secs=6
#         )
# print("Connecting to {} with client ID '{}'...".format(
#     ENDPOINT, CLIENT_ID))
# # Make the connect() call
# connect_future = mqtt_connection.connect()
# # Future.result() waits until a result is available
# connect_future.result()
# print("Connected!")
# # Publish message to server desired number of times.
# print('Begin Publish')
# for i in range(RANGE):
#     message = message_gen()
#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '" + json.dumps(message) + "' to the topic: " + "'"+TOPIC+"'")
#     t.sleep(2)
# print('Publish End')
# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()


#!/usr/bin/env python3
# from awscrt import io, mqtt, auth, http
# from awsiot import mqtt_connection_builder
# import time as t
# import json
# import uuid
# import random
# import datetime

# current_id = 1000

# def message_gen():
#     global current_id
#     timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
#     # Define the parameters for the pattern
#     duration = 20  # Total duration of the pattern in seconds
    
#     # Define individual parameters for each road
#     road_params = {
#         "road1": {"peak_value": 6},
#         "road2": {"peak_value": 8},
#         "road3": {"peak_value": 7},
#         "road4": {"peak_value": 5}
#     }
    
#     message = {
#         "ID": current_id,
#         "Timestamp": timestamp,
#         "open": 1  # Assuming road 1 is always open
#     }
    
#     # Calculate the traffic values for each road based on the time component
#     for road, params in road_params.items():
#         peak_time = random.randint(5, 15)  # Random offset for peak time
        
#         time_diff = t.time() % duration  # Current time within the duration
        
#         if time_diff <= peak_time:
#             traffic_value = (time_diff / peak_time) * params["peak_value"]  # Increasing pattern
#         else:
#             traffic_value = ((duration - time_diff) / (duration - peak_time)) * params["peak_value"]  # Decreasing pattern
        
#         message[road] = traffic_value
    
#     current_id += 1
#     return message

# # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, TOPIC, and RANGE
# ENDPOINT = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com"
# CLIENT_ID = "traffic_monitor"
# PATH_TO_CERTIFICATE = "./dc.pem"
# PATH_TO_PRIVATE_KEY = "./private.pem"
# PATH_TO_AMAZON_ROOT_CA_1 = "./root.pem"
# TOPIC = "traffic_monitor/knkn9/traffic_density"
# RANGE = 

# # Spin up resources
# event_loop_group = io.EventLoopGroup(1)
# host_resolver = io.DefaultHostResolver(event_loop_group)
# client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
# mqtt_connection = mqtt_connection_builder.mtls_from_path(
#         endpoint=ENDPOINT,
#         cert_filepath=PATH_TO_CERTIFICATE,
#         pri_key_filepath=PATH_TO_PRIVATE_KEY,
#         client_bootstrap=client_bootstrap,
#         ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
#         client_id=CLIENT_ID,
#         clean_session=False,
#         keep_alive_secs=6
#         )
# print("Connecting to {} with client ID '{}'...".format(ENDPOINT, CLIENT_ID))
# # Make the connect() call
# connect_future = mqtt_connection.connect()
# # Future.result() waits until a result is available
# connect_future.result()
# print("Connected!")
# # Publish message to server desired number of times.
# print('Begin Publish')
# for i in range(RANGE):
#     message = message_gen()
#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '" + json.dumps(message) + "' to the topic: " + "'"+TOPIC+"'")
#     t.sleep(2)
# print('Publish End')
# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()







# #!/usr/bin/env python3
# from awscrt import io, mqtt, auth, http
# from awsiot import mqtt_connection_builder
# import time as t
# import json
# # import uuid
# import random
# import datetime
# # from datetime import datetime
# duration = 20
# current_id = 1
# def message_gen():
#     global current_id
    
#     # Define individual parameters for each road
#     road_params = {
#         "road1": {"peak_value": 6},
#         "road2": {"peak_value": 8},
#         "road3": {"peak_value": 7},
#         "road4": {"peak_value": 5}
#     }
    
#     message = {
#         "ID": current_id,
#         "open": 1  # Assuming road 1 is always open
#     }
    
#     # Calculate the traffic values for each road based on the time component
#     for road, params in road_params.items():
#         # min_duration = 15
#         # max_duration = 30
#         # duration = random.randint(min_duration, max_duration)
#         peak_time = random.randint(5, 15)  # Random offset for peak time
        
#         time_diff = t.time() % duration  # Current time within the duration
        
#         if time_diff <= peak_time:
#             traffic_value = (time_diff / peak_time) * params["peak_value"]  # Increasing pattern
#         else:
#             traffic_value = ((duration - time_diff) / (duration - peak_time)) * params["peak_value"]  # Decreasing pattern
        
#         # message[road] = round(traffic_value, 1)
#         message[road] = int(traffic_value)
#     current_id += 1
#     return message

# # Define the start and end timestamps
# start_timestamp = datetime.datetime(2023, 5, 1, 0, 0, 0)
# end_timestamp = datetime.datetime(2023, 5, 2, 0, 0, 0)

# # Calculate the total number of minutes between the start and end timestamps
# total_minutes = int((end_timestamp - start_timestamp).total_seconds() / 60)

# # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, TOPIC
# ENDPOINT = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com"
# CLIENT_ID = "traffic_monitor"
# PATH_TO_CERTIFICATE = "./dc.pem"
# PATH_TO_PRIVATE_KEY = "./private.pem"
# PATH_TO_AMAZON_ROOT_CA_1 = "./root.pem"
# TOPIC = "traffic_monitor/knkn9/traffic_density"

# # Spin up resources
# event_loop_group = io.EventLoopGroup(1)
# host_resolver = io.DefaultHostResolver(event_loop_group)
# client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
# mqtt_connection = mqtt_connection_builder.mtls_from_path(
#     endpoint=ENDPOINT,
#     cert_filepath=PATH_TO_CERTIFICATE,
#     pri_key_filepath=PATH_TO_PRIVATE_KEY,
#     client_bootstrap=client_bootstrap,
#     ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
#     client_id=CLIENT_ID,
#     clean_session=False,
#     keep_alive_secs=6
# )
# print("Connecting to {} with client ID '{}'...".format(ENDPOINT, CLIENT_ID))
# # Make the connect() call
# connect_future = mqtt_connection.connect()
# # Future.result() waits until a result is available
# connect_future.result()
# print("Connected!")

# # Publish message to server for the specified duration
# # print('Begin Publish')
# # for i in range(total_minutes):
# #     # Calculate the current timestamp
    
# #     current_timestamp = start_timestamp + datetime.timedelta(minutes=i)
# #     timestamp_str = current_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')

# #     message = message_gen()
# #     message['Timestamp'] = timestamp_str

# #     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
# #     print("Published: '" + json.dumps(message) + "' to the topic: " + "'"+TOPIC+"'")
# #     t.sleep(60)  # Sleep for 60 seconds (1 minute)
# # print('Publish End')

# print('Begin Publish')
# current_timestamp = start_timestamp
# for i in range(total_minutes):
#     timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%SZ')

#     message = message_gen()
#     message['Timestamp'] = timestamp_str

#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '" + json.dumps(message) + "' to the topic: " + "'"+TOPIC+"'")

#     current_timestamp += datetime.timedelta(minutes=1)  # Increment timestamp by 1 minute

# print('Publish End')

# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()





# #!/usr/bin/env python3
# from awscrt import io, mqtt, auth, http
# from awsiot import mqtt_connection_builder
# import time as t
# import json
# import random
# import datetime

# duration = 20
# current_id = 1


# def message_gen():
#     global current_id

#     # Define individual parameters for each road
#     road_params = {
#         "road1": {"peak_value": 6},
#         "road2": {"peak_value": 8},
#         "road3": {"peak_value": 7},
#         "road4": {"peak_value": 5}
#     }

#     message = {
#         "ID": current_id,
#         "open": 1  # Assuming road 1 is always open
#     }

#     # Calculate the traffic values for each road based on the time component
#     for road, params in road_params.items():
#         peak_time = random.randint(5, 15)  # Random offset for peak time

#         time_diff = t.time() % duration  # Current time within the duration

#         if time_diff <= peak_time:
#             traffic_value = (time_diff / peak_time) * params["peak_value"]  # Increasing pattern
#         else:
#             traffic_value = ((duration - time_diff) / (duration - peak_time)) * params[
#                 "peak_value"]  # Decreasing pattern

#         message[road] = int(traffic_value)
#     current_id += 1
#     return message


# # Define the start and end timestamps
# start_timestamp = datetime.datetime(2023, 5, 1, 0, 0, 0)
# end_timestamp = datetime.datetime(2023, 5, 2, 0, 0, 0)

# # Calculate the total number of minutes between the start and end timestamps
# total_minutes = int((end_timestamp - start_timestamp).total_seconds() / 60)

# # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, TOPIC
# ENDPOINT = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com"
# CLIENT_ID = "traffic_monitor"
# PATH_TO_CERTIFICATE = "./dc.pem"
# PATH_TO_PRIVATE_KEY = "./private.pem"
# PATH_TO_AMAZON_ROOT_CA_1 = "./root.pem"
# TOPIC = "traffic_monitor/knkn9/traffic_density"

# # Spin up resources
# event_loop_group = io.EventLoopGroup(1)
# host_resolver = io.DefaultHostResolver(event_loop_group)
# client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
# mqtt_connection = mqtt_connection_builder.mtls_from_path(
#     endpoint=ENDPOINT,
#     cert_filepath=PATH_TO_CERTIFICATE,
#     pri_key_filepath=PATH_TO_PRIVATE_KEY,
#     client_bootstrap=client_bootstrap,
#     ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
#     client_id=CLIENT_ID,
#     clean_session=False,
#     keep_alive_secs=6
# )
# print("Connecting to {} with client ID '{}'...".format(ENDPOINT, CLIENT_ID))
# # Make the connect() call
# connect_future = mqtt_connection.connect()
# # Future.result() waits until a result is available
# connect_future.result()
# print("Connected!")

# print('Begin Publish')
# current_timestamp = start_timestamp
# for i in range(total_minutes):
#     timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%SZ')

#     message = message_gen()
#     message['Timestamp'] = timestamp_str

#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '" + json.dumps(message) + "' to the topic: " + "'" + TOPIC + "'")

#     current_timestamp += datetime.timedelta(minutes=1)  # Increment timestamp by 1 minute

# print('Publish End')

# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()


#!/usr/bin/env python3
# from awscrt import io, mqtt, auth, http
# from awsiot import mqtt_connection_builder
# import time as t
# import json
# import random
# import datetime

# duration = 20
# current_id = 1

# def message_gen():
#     global current_id

#     # Define individual parameters for each road
#     road_params = {
#         "road1": {"peak_value": 6},
#         "road2": {"peak_value": 8},
#         "road3": {"peak_value": 7},
#         "road4": {"peak_value": 5}
#     }

#     timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%SZ')

#     message = {
#         "ID": current_id,
#         "open": 1,  # Assuming road 1 is always open
#         # "Timestamp": timestamp
#     }

#     # Calculate the traffic values for each road based on the peak_value parameter
#     for road, params in road_params.items():
#         message[road] = params["peak_value"]
#     current_id += 1
#     return message


# # Define the start and end timestamps
# start_timestamp = datetime.datetime(2023, 5, 1, 0, 0, 0)
# end_timestamp = datetime.datetime(2023, 5, 2, 0, 0, 0)

# # Calculate the total number of minutes between the start and end timestamps
# total_minutes = int((end_timestamp - start_timestamp).total_seconds() / 60)

# # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, TOPIC
# ENDPOINT = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com"
# CLIENT_ID = "traffic_monitor"
# PATH_TO_CERTIFICATE = "./dc.pem"
# PATH_TO_PRIVATE_KEY = "./private.pem"
# PATH_TO_AMAZON_ROOT_CA_1 = "./root.pem"
# TOPIC = "traffic_monitor/knkn9/traffic_density"

# # Spin up resources
# event_loop_group = io.EventLoopGroup(1)
# host_resolver = io.DefaultHostResolver(event_loop_group)
# client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
# mqtt_connection = mqtt_connection_builder.mtls_from_path(
#     endpoint=ENDPOINT,
#     cert_filepath=PATH_TO_CERTIFICATE,
#     pri_key_filepath=PATH_TO_PRIVATE_KEY,
#     client_bootstrap=client_bootstrap,
#     ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
#     client_id=CLIENT_ID,
#     clean_session=False,
#     keep_alive_secs=6
# )

# print("Connecting to {} with client ID '{}'...".format(ENDPOINT, CLIENT_ID))
# # Make the connect() call
# connect_future = mqtt_connection.connect()
# # Future.result() waits until a result is available
# connect_future.result()
# print("Connected!")

# print('Begin Publish')
# current_timestamp = start_timestamp

# # Calculate the peak time for the day
# peak_time = random.randint(5, 15)  # Random offset for peak time

# for i in range(total_minutes):
#     message = message_gen()
#     timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%SZ')
#     message['Timestamp'] = timestamp_str
#     # Calculate the current time difference within the duration
#     time_diff = t.time() % duration

#     for road in message.keys():
#         if road.startswith("road"):
#             if time_diff <= peak_time:
#                 traffic_value = (time_diff / peak_time) * message[road]  # Increasing pattern
#             else:
#                 traffic_value = ((duration - time_diff) / (duration - peak_time)) * message[road]  # Decreasing pattern
#             message[road] = int(traffic_value)

#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '{}' to the topic: '{}'".format(json.dumps(message), TOPIC))

#     current_timestamp += datetime.timedelta(minutes=1)  # Increment timestamp by 1 minute
#     t.sleep(1)
# print('Publish End')

# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()


# #!/usr/bin/env python3
# from awscrt import io, mqtt, auth, http
# from awsiot import mqtt_connection_builder
# import time as t
# import json
# import random
# import datetime

# current_id = 1

# def message_gen():
#     global current_id

#     # Define individual parameters for each road
#     road_params = {
#         "road1": {"peak_value": 6, "duration": random.randint(10, 30)},
#         "road2": {"peak_value": 8, "duration": random.randint(10, 30)},
#         "road3": {"peak_value": 7, "duration": random.randint(10, 30)},
#         "road4": {"peak_value": 5, "duration": random.randint(10, 30)}
#     }

#     timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%SZ')

#     message = {
#         "ID": current_id,
#         "open": 1,  # Assuming road 1 is always open
#         # "Timestamp": timestamp
#     }

#     # Calculate the traffic values for each road based on the peak_value parameter
#     for road, params in road_params.items():
#         message[road] = params["peak_value"]
#         if "last_update" not in params:
#             params["last_update"] = datetime.datetime.now()  # Store the last update time for the road
#     current_id += 1
#     return message, road_params


# # Define the start and end timestamps
# start_timestamp = datetime.datetime(2023, 5, 1, 0, 0, 0)
# end_timestamp = datetime.datetime(2023, 5, 1, 12, 0, 0)

# # Calculate the total number of minutes between the start and end timestamps
# total_minutes = int((end_timestamp - start_timestamp).total_seconds() / 60)

# # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, TOPIC
# ENDPOINT = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com"
# CLIENT_ID = "traffic_monitor"
# PATH_TO_CERTIFICATE = "./dc.pem"
# PATH_TO_PRIVATE_KEY = "./private.pem"
# PATH_TO_AMAZON_ROOT_CA_1 = "./root.pem"
# TOPIC = "traffic_monitor/knkn9/traffic_density"

# # Spin up resources
# event_loop_group = io.EventLoopGroup(1)
# host_resolver = io.DefaultHostResolver(event_loop_group)
# client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
# mqtt_connection = mqtt_connection_builder.mtls_from_path(
#     endpoint=ENDPOINT,
#     cert_filepath=PATH_TO_CERTIFICATE,
#     pri_key_filepath=PATH_TO_PRIVATE_KEY,
#     client_bootstrap=client_bootstrap,
#     ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
#     client_id=CLIENT_ID,
#     clean_session=False,
#     keep_alive_secs=6
# )

# print("Connecting to {} with client ID '{}'...".format(ENDPOINT, CLIENT_ID))
# # Make the connect() call
# connect_future = mqtt_connection.connect()
# # Future.result() waits until a result is available
# connect_future.result()
# print("Connected!")

# print('Begin Publish')
# current_timestamp = start_timestamp

# for i in range(total_minutes):
#     message, road_params = message_gen()
#     timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%SZ')
#     message['Timestamp'] = timestamp_str

#     for road, params in road_params.items():
#         time_diff = (current_timestamp - params["last_update"]).total_seconds()
#         duration = params["duration"]
#         if time_diff >= duration:
#             # Randomly update the peak value and duration for the road
#             params["peak_value"] = random.randint(1, 10)
#             params["duration"] = random.randint(10, 30)
#             params["last_update"] = current_timestamp

#         if time_diff <= duration / 2:
#            traffic_value = ((2 * time_diff) / duration-1) * params["peak_value"]  # Increasing pattern  # Increasing pattern
#         else:
#             traffic_value = ((2 * (duration - time_diff)) / duration-1) * params["peak_value"]  # Decreasing pattern  # Decreasing pattern
#         message[road] = int(traffic_value)

#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '{}' to the topic: '{}'".format(json.dumps(message), TOPIC))

#     current_timestamp += datetime.timedelta(minutes=1)  # Increment timestamp by 1 minute
#     # t.sleep(1)
# print('Publish End')

# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()




## Modified

#!/usr/bin/env python3
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
import random
import datetime

duration = 300
current_id = 1

def message_gen():
    global current_id

    # Define individual parameters for each road
    road_params = {
        "road1": {"peak_value": 6},
        "road2": {"peak_value": 8},
        "road3": {"peak_value": 7},
        "road4": {"peak_value": 5}
    }

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%SZ')
    # Find the road with the minimum traffic value
    min_traffic_value = float('inf')
    min_traffic_road = None

    message = {
        "ID": current_id,
        "open": None,  # Placeholder for the road with minimum traffic
        # "Timestamp": timestamp
    }

    # Calculate the traffic values for each road based on the peak_value parameter
    for road, params in road_params.items():
        if time_diff <= peak_time:
            traffic_value = (time_diff / peak_time) * params["peak_value"]  # Increasing pattern
        else:
            traffic_value = ((duration - time_diff) / (duration - peak_time)) * params["peak_value"]  # Decreasing pattern
        traffic_value = int(traffic_value)
        message[road] = traffic_value

        if traffic_value < min_traffic_value:
            min_traffic_value = traffic_value
            min_traffic_road = road

    message["open"] = int(min_traffic_road.replace("road", "")) if min_traffic_road is not None else None

    current_id += 1
    return message


# Rest of the code...


# Define the start and end timestamps
start_timestamp = datetime.datetime(2023, 5, 1, 0, 0, 0)
end_timestamp = datetime.datetime(2023, 5, 2, 0, 0, 0)

# Calculate the total number of minutes between the start and end timestamps
total_minutes = int((end_timestamp - start_timestamp).total_seconds() / 60)

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, TOPIC
ENDPOINT = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "traffic_monitor"
PATH_TO_CERTIFICATE = "./dc.pem"
PATH_TO_PRIVATE_KEY = "./private.pem"
PATH_TO_AMAZON_ROOT_CA_1 = "./root.pem"
TOPIC = "traffic_monitor/knkn9/traffic_density"

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERTIFICATE,
    pri_key_filepath=PATH_TO_PRIVATE_KEY,
    client_bootstrap=client_bootstrap,
    ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=6
)

print("Connecting to {} with client ID '{}'...".format(ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")

print('Begin Publish')
current_timestamp = start_timestamp

# Calculate the peak time for the day
peak_time = random.randint(5, 15)  # Random offset for peak time

for i in range(total_minutes):
    message = message_gen()
    timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%SZ')
    message['Timestamp'] = timestamp_str
    # Calculate the current time difference within the duration
    time_diff = t.time() % duration
    mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '{}' to the topic: '{}'".format(json.dumps(message), TOPIC))

    current_timestamp += datetime.timedelta(minutes=1)  # Increment timestamp by 1 minute
    t.sleep(1)
print('Publish End')

disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()