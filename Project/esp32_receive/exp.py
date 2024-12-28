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
    road1 = max(min(road1, 30), 4)
    road2 += trend_direction2
    road2 = max(min(road2, 28), 4)
    road3 += trend_direction3
    road3 = max(min(road3, 30), 4)
    road4 += trend_direction4
    road4 = max(min(road4, 28), 4)
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
        if previous_signal[-1]==curr: #curr is the current open signal
            for i in min_order:     # Iterate through the sorted order of signal values
                if i[1]<=18 and i[0]!=curr: #Check if any other signal value is less than the threshold value and it is not the current signal value that is being checked for opening curr
                    return False
            return True
        else:                   # curr is not the current open signal
            if curr in previous_signal[-2:]:    #check if the signal was open in the two previous signals
                for i in min_order:   # Iterate through the sorted order of signal values
                    if i[1]<=18 and i[0]!=curr and i[0]!=open_signal:#Check if any other signal value is less than the threshold, It is not the curr signal that is being checked and it is not the current open signal
                        return False
            return True
    else:
        if previous_signal[-1]==curr: #curr is not the current open signal
            for i in min_order:   # Iterate through the sorted order of signal values
                if i[1]<=18 and i[0]!=curr: #Check if any other signal value is less than the threshold value and it is not the current signal value that is being checked for opening curr
                    return False
            return True
        else:   # curr is not the current open signal
            if curr in previous_signal[-2:]:    #check if the signal was open in the two previous signals
                for i in min_order:   # Iterate through the sorted order of signal values
                    if i[1]<=18 and i[0]!=curr and i[0]!=open_signal: #Check if any other signal value is less than the threshold, It is not the curr signal that is being checked and it is not the current open signal
                        return False
            return True

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
    handle_signal_change(open_signal)
    print("Timer: ",timer)
    print("Signal_History: ",previous_signal)

    minute = int(timestamp[14:16])
    hour = int(timestamp[11:13])
    day = days[int(timestamp[8:10])%7]
    message = {
        "ID": current_id,
        "open": open_signal,  # Placeholder for the road with minimum traffic
        "road1": road1,
        "road2": road2,
        "road3": road3,
        "road4": road4,
        "Timestamp": timestamp,
        "Minute": minute,
        "Hour": hour,
        "Day": day
    }
    current_id += 1
    return message

def trend_gen():
    global trend_direction1, trend_direction2, trend_direction3, trend_direction4, trend_duration
    trend_duration = random.randint(20, 100)
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
    global current_id,timer,total_seconds, current_timestamp, trend_duration, extra_timer, days
    current_id = 50401
    timer = 0
    extra_timer = 0
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Define the start and end timestamps
    start_timestamp = datetime.datetime(2023, 5, 25, 18, 0, 0)
    end_timestamp = datetime.datetime(2023, 5, 25, 20, 0, 0)
    # Calculate the total number of seconds between the start and end timestamps
    total_seconds = int((end_timestamp - start_timestamp).total_seconds())
    current_timestamp = start_timestamp
    return

def set_signal_values():
    global road1,road2,road3,road4,signal_open_time,open_signal,previous_signal
    # road1 = 7
    # road2 = 5
    # road3 = 9
    # road4 = 11
    # road1 = 10
    # road2 = 11
    # road3 = 7
    # road4 = 8
    # road1 = 9
    # road2 = 8
    # road3 = 4
    # road4 = 10
    # road1 = 4
    # road2 = 8
    # road3 = 6
    # road4 = 5
    road1 = 9
    road2 = 15
    road3 = 18
    road4 = 24
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

        mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
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
