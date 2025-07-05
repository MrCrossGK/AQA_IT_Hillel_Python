from datetime import datetime


def time_extractor():
    filtered_file = []
    key = "Key TSTFEED0300|7E3E|0400"
    with open('hblog.txt', 'r') as file:
        for line in file:
            if key in line:
                after = line.split("Timestamp")[1].strip()
                event_time = after.split()[0]
                conv_ev_time = datetime.strptime(event_time, "%H:%M:%S")
                filtered_file.append(conv_ev_time)
    return filtered_file
