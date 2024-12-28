# #!/usr/bin/env python3
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import random
import datetime
import time as t
import json

def sort_road_values():
    global road1, road2, road3, road4, min_order, min_order_index
    temp = list()
    road1 += trend_direction1
    road1 = max(min(road1, 14), 0)
    road2 += trend_direction2
    road2 = max(min(road2, 14), 0)
    road3 += trend_direction3
    road3 = max(min(road3, 14), 0)
    road4 += trend_direction4
    road4 = max(min(road4, 14), 0)
    # Apply limits to stay within the range 0-14
    temp.append(road1)
    temp.append(road2)
    temp.append(road3)
    temp.append(road4)
    min_order_plus_one = sorted(enumerate(temp), key=lambda x: x[1])
    min_order = [(index + 1, value) for index, value in min_order_plus_one]
    min_order_index = [index+1 for index,_ in min_order_plus_one]
    return

def signal_calc():
    global open_signal, timer
    for i in min_order_index:
        if check_others(i) and timer<=0:     # function to check if the signal can be opened
            open_signal = i
            timer=30

def check_others(curr):
    if min_order[0][0]==curr:   # Check if the current signal is the lowest
        if previous_signal[-1]==curr: #Curr is not the current open signal
            for i in min_order:   # Check if the signal was the previously opened signal
                if i[1]<=5 and i[0]!=curr:
                    return False
            return True
        else:
            if curr in previous_signal[-2:]:
                for i in min_order:   # Check if the signal was the previously opened signal
                    if i[1]<=5 and i[0]!=curr and i[0]!=open_signal:
                        return False
            return True
    else:
        if previous_signal[-1]==curr: #Curr is not the current open signal
            for i in min_order:   # Check if the signal was the previously opened signal
                if i[1]<=5 and i[0]!=curr:
                    return False
            return True
        else:
            if curr in previous_signal[-2:]:
                for i in min_order:   # Check if the signal was the previously opened signal
                    if i[1]<=5 and i[0]!=curr and i[0]!=open_signal:
                        return False
            return True

## Added conditions
# def check_pthers(curr):
#     if min_order[0][0]==curr:   # Check if the current signal is the lowest
#         if previous_signal[-1]==curr: #Curr is not the current open signal
#             for i in min_order:   # Check if the signal was the previously opened signal
#                 if i[1]<=5 and i[0]!=curr:
#                     return False
#             return True
#         else:
#             if curr in previous_signal[-2:]:
#                 for i in min_order:   # Check if the signal was the previously opened signal
#                     if i[1]<=5 and i[0]!=curr and i[0]!=open_signal:
#                         return False
#             return True
#     else:
#         if previous_signal[-1]==curr: #Curr is not the current open signal
#             for i in min_order:   # Check if the signal was the previously opened signal
#                 if i[1]<=5 and i[0]!=curr:
#                     return False
#             return True
#         else:
#             if curr in previous_signal[-2:]:
#                 for i in min_order:   # Check if the signal was the previously opened signal
#                     if i[1]<=5 and i[0]!=curr and i[0]!=open_signal:
#                         return False
#             else:
#                 c=6
#                 p=0
#                 j=1
#                 for i in min_order:
#                     if i[1]<=5 and i[0]!=open_signal:
#                         if i[0]==curr:
#                             c=j
#                         elif i[0] in previous_signal[-2:]:
#                             j=j
#                         else:
#                             p=j
#                             break
#                     j+=1
#                 if c<p:
#                     return True
#                 return False


def handle_signal_change(current):
    global previous_signal, current_id, signal_open_time,timer,extra_timer
    timer-=1
    extra_timer+=1
    if current == previous_signal[-1]:
        if extra_timer>=30:
            extra_timer=0
            previous_signal.append(current)
        return
    else:
        extra_timer=0
        signal_open_time['signal'] = current
        signal_open_time['start_time'] = current_id
        previous_signal.append(current)
    return

def message_generate(timestamp):
    global current_id, signal_open_time, open_signal, timer
    # Determine the road with the minimum distance
    # min_distance = min(road1, road2, road3, road4)
    sort_road_values()
    print("Min_order: ",min_order)
    signal_calc()
    # # Set the value of 'open' attribute based on the road with the minimum distance
    # if min_distance == road1 and timer==0 and (1 not in previous_signal[-3:]):
    #     print("Normal Signal Change 1")
    #     open_signal = 1
    #     timer = 60
    # elif min_distance == road2 and timer==0 and (2 not in previous_signal[-3:]):
    #     print("Normal Signal Change 2")
    #     open_signal = 2
    #     timer = 60
    # elif min_distance == road3 and timer==0 and (3 not in previous_signal[-3:]):
    #     print("Normal Signal Change 3")
    #     timer = 60
    #     open_signal = 3
    # elif min_distance == road4 and timer==0 and (4 not in previous_signal[-3:]):
    #     print("Normal Signal Change 4")
    #     timer = 60
    #     open_signal = 4

    # # Check if the current open signal has been open for more than 1 minute
    # if (open_signal == signal_open_time['signal']) and timer<=0:
    # # ((current_id - signal_open_time['start_time']) >= 60):
    #     # Find the next minimum road value
    #     if road1 != min_distance and (open_signal != 1) and (1 not in previous_signal[-2:] and road1<=5):
    #         if (signal_open_time['signal']!= 1):
    #             timer = 60
    #             print("Exceptional Signal Change 1. 60 sec")
    #         else:
    #             timer = 20
    #             print("Exceptional Signal Change 1. 20 sec")
    #         open_signal = 1
    #     elif road2 != min_distance and (open_signal != 2) and (2 not in previous_signal[-2:] and road2<=5):
    #         if (signal_open_time['signal']!= 2):
    #             timer = 60
    #             print("Exceptional Signal Change 2. 60 sec")
    #         else:
    #             timer = 20
    #             print("Exceptional Signal Change 2. 20 sec")
    #         open_signal = 2
    #     elif road3 != min_distance and (open_signal != 3) and (3 not in previous_signal[-2:] and road3<=5):
    #         if (signal_open_time['signal']!= 3):
    #             timer = 60
    #             print("Exceptional Signal Change 3. 60 sec")
    #         else:
    #             timer = 20
    #             print("Exceptional Signal Change 3. 20 sec")
    #         open_signal = 3
    #     elif road4 != min_distance and (open_signal != 4) and (4 not in previous_signal[-2:] and road4<=5):
    #         if (signal_open_time['signal']!= 4):
    #             timer = 60
    #             print("Exceptional Signal Change 4. 60 sec")
    #         else:
    #             timer = 20
    #             print("Exceptional Signal Change 4. 20 sec")
    #         open_signal = 4
    #     # Update the signal open time and reset the start time
    #     signal_open_time['signal'] = open_signal
    #     signal_open_time['start_time'] = current_id
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
    global trend_direction1, trend_direction2, trend_direction3, trend_direction4, trend_duration
    trend_duration = random.randint(20, 40)
    trend_direction1 = random.uniform(-0.5, 0.5)
    trend_direction2 = random.uniform(-0.5, 0.5)
    trend_direction3 = random.uniform(-0.5, 0.5)
    trend_direction4 = random.uniform(-0.5, 0.5)
    return

def cloud_connect():
    global TOPIC, mqtt_connection
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
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")
    print('Begin Publish')
    return

def set_time_variables():
    global current_id,timer,total_seconds, current_timestamp, trend_duration, extra_timer
    current_id = 1
    timer = 0
    extra_timer = 0
    # Define the start and end timestamps
    start_timestamp = datetime.datetime(2023, 5, 1, 0, 0, 0)
    end_timestamp = datetime.datetime(2023, 5, 1, 12, 0, 0)
    # Calculate the total number of seconds between the start and end timestamps
    total_seconds = int((end_timestamp - start_timestamp).total_seconds())
    current_timestamp = start_timestamp
    return

def set_signal_values():
    global road1,road2,road3,road4,signal_open_time,open_signal,previous_signal
    road1 = 7
    road2 = 5
    road3 = 9
    road4 = 11

    signal_open_time = {'signal': 0, 'start_time': 0}
    open_signal = 0
    previous_signal = [0]
    return

if __name__ == '__main__':
    trend_gen()
    set_time_variables()
    set_signal_values()
    cloud_connect()
    time_diff = 0
    for i in range(total_seconds):
        time_diff +=1
        timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%SZ')
        if time_diff <= trend_duration:
            message = message_generate(timestamp_str)
        else:
            trend_gen()
            print("Change In trend!")
            time_diff = 0
            message = message_generate(timestamp_str)

        # mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
        print("Trend details: ", trend_direction1, trend_direction2, trend_direction3, trend_direction4)
        print("Published: '{}' to the topic: '{}'".format(json.dumps(message), TOPIC))
        print("Open Signal Details: ",signal_open_time)
        print("Trend Duration: ", trend_duration)
        print("TimeDiff:", time_diff)
        print()
        current_timestamp += datetime.timedelta(seconds=1)
        t.sleep(0.1)

    print('Publish End')

    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
