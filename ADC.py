import time
import random

def readValue ( channelNum ):
    "Reads an analog value from the specified channel number and returns a tuple containing the timestamp and the value"
    
    value = round(random.uniform(50,100),1)
    timestamp = int(round(time.time()*1000))

    time.sleep(1)

    return (timestamp, value)

