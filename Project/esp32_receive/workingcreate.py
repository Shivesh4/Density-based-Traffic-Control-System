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

#     timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%SZ')
#     # Find the road with the minimum traffic value
#     min_road = min(road_params, key=lambda x: road_params[x]["peak_value"])
#     # min_road_number = int(min_road.replace("road", ""))

#     message = {
#         "ID": current_id,
#         # "open": min_road_number,  # Assuming road 1 is always open
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
#     min_traffic_value = 100000000
#     min_traffic_road = -1
#     for road in message.keys():
#         if road.startswith("road"):
#             if time_diff <= peak_time:
#                 # Increasing pattern with random factor
#                 traffic_value = (time_diff / peak_time) * message[road] * (1 + random.uniform(-0.1, 0.1))
#             else:
#                 # Decreasing pattern with random factor
#                 traffic_value = ((duration - time_diff) / (duration - peak_time)) * message[road] * (1 + random.uniform(-0.1, 0.1))  # Decreasing pattern
#             message[road] = int(traffic_value)
#             if traffic_value < min_traffic_value:
#                 min_traffic_value = traffic_value
#                 min_traffic_road = int(road[4])
#     # print(message)
#     message["open"] = min_traffic_road 

#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '{}' to the topic: '{}'".format(json.dumps(message), TOPIC))

#     current_timestamp += datetime.timedelta(minutes=1)  # Increment timestamp by 1 minute
#     t.sleep(0.5)
# print('Publish End')

# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()




''' Modified code for ensuring round robin '''
''' Going to change previous_signal to a list. Used this to populate Database. '''
# #!/usr/bin/env python3
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import random
import datetime
import time as t
import json


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

def handle_signal_change(current):
    global previous_signal, current_id, signal_open_time,timer
    timer-=1 
    if current == previous_signal[-1]:
        return
    else:
        signal_open_time['signal'] = current
        signal_open_time['start_time'] = current_id
        previous_signal.append(current)
    return

def message_generate(trend_direction1, trend_direction2, trend_direction3, trend_direction4, timestamp):
    global current_id, road1, road2, road3, road4, signal_open_time, open_signal, timer

    road1 += trend_direction1
    road2 += trend_direction2
    road3 += trend_direction3
    road4 += trend_direction4

    # Apply limits to stay within the range 0-14
    road1 = max(min(road1, 14), 0)
    road2 = max(min(road2, 14), 0)
    road3 = max(min(road3, 14), 0)
    road4 = max(min(road4, 14), 0)
    # Determine the road with the minimum distance
    min_distance = min(road1, road2, road3, road4)

    # Set the value of 'open' attribute based on the road with the minimum distance
    if min_distance == road1 and timer==0 and (1 not in previous_signal[-3:]):
        open_signal = 1
        timer = 60
    elif min_distance == road2 and timer==0 and (2 not in previous_signal[-3:]):
        open_signal = 2
        timer = 60
    elif min_distance == road3 and timer==0 and (3 not in previous_signal[-3:]):
        timer = 60
        open_signal = 3
    elif min_distance == road4 and timer==0 and (4 not in previous_signal[-3:]):
        timer = 60
        open_signal = 4
    # Check if the current open signal has been open for more than 1 minute
    if (open_signal == signal_open_time['signal']) and timer<=0:
    # ((current_id - signal_open_time['start_time']) >= 60):
        # Find the next minimum road value
        if road1 != min_distance and (open_signal != 1 or road1 == 0) and (1 not in previous_signal[-3:]):
            if (signal_open_time['signal']!= 1 and min_distance==road1):
                timer = 60
            else:
                timer = 20
            open_signal = 1
        elif road2 != min_distance and (open_signal != 2 or road2 == 0) and (2 not in previous_signal[-3:]):
            if (signal_open_time['signal']!= 2 and min_distance==road2):
                timer = 60
            else:
                timer = 20
            open_signal = 2
        elif road3 != min_distance and (open_signal != 3 or road3 == 0) and (3 not in previous_signal[-3:]):
            if (signal_open_time['signal']!= 3 and min_distance==road3):
                timer = 60
            else:
                timer = 20
            open_signal = 3
        elif road4 != min_distance and (open_signal != 4 or road4 == 0) and (4 not in previous_signal[-3:]):
            if (signal_open_time['signal']!= 4 and min_distance==road4):
                timer = 60
            else:
                timer = 20
            open_signal = 4
        # Update the signal open time and reset the start time
        signal_open_time['signal'] = open_signal
        signal_open_time['start_time'] = current_id
    handle_signal_change(open_signal)
    print("Timer: ",timer)
    print("Signal_History: ",previous_signal)
    message = {
        "ID": current_id,
        "open": open_signal,  # Placeholder for the road with minimum traffic
        "road1": road1,
        "road2": road2,
        "road3": road3,
        "road4": road4,
        "Timestamp": timestamp
    }
    current_id += 1
    return message

def trend_gen():
    global trend_direction1, trend_direction2, trend_direction3, trend_direction4

    trend_direction1 = random.uniform(-0.5, 0.5)
    trend_direction2 = random.uniform(-0.5, 0.5)
    trend_direction3 = random.uniform(-0.5, 0.5)
    trend_direction4 = random.uniform(-0.5, 0.5)

flag = 0
current_id = 2088
timer = 0
# Define the start and end timestamps
start_timestamp = datetime.datetime(2023, 5, 7, 1, 4, 47)
end_timestamp = datetime.datetime(2023, 5, 7, 1, 5, 0)

# Calculate the total number of seconds between the start and end timestamps
total_seconds = int((end_timestamp - start_timestamp).total_seconds())
current_timestamp = start_timestamp
trend_duration = random.randint(20, 60)
trend_gen()

road1 = 0
road2 = 0
road3 = 0.20278684
road4 = 0
time_diff = 0
signal_open_time = {'signal': 0, 'start_time': 0}
open_signal = 0
previous_signal = [0]
for i in range(total_seconds):
    # Calculate the current time difference within the duration
    time_diff +=1
    timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%SZ')
    if time_diff <= trend_duration:
        message = message_generate(trend_direction1, trend_direction2, trend_direction3, trend_direction4, timestamp_str)
    else:
        trend_gen()
        time_diff = 0
        trend_duration = random.randint(20, 60)
        message = message_generate(trend_direction1, trend_direction2, trend_direction3, trend_direction4, timestamp_str)
    if flag==0:
        signal_open_time['signal'] = message['open']
        previous_signal.append(message['open'])
        signal_open_time['start_time'] = current_id
        flag = 1
    mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '{}' to the topic: '{}'".format(json.dumps(message), TOPIC))
    print("Open Signal Details: ",signal_open_time)
    print("TimeDiff:", time_diff)
    print()
    current_timestamp += datetime.timedelta(seconds=1)
    t.sleep(0.1)

print('Publish End')

disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()