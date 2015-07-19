import requests
import time
import random
from uuid import getnode as get_mac

def readValue ( channelNum ):
    "Reads an analog value from the specified channel number and returns a tuple containing the timestamp and the value"
    
    value = round(random.uniform(50,100),1)
    timestamp = int(round(time.time()*1000))

    time.sleep(1)

    return (timestamp, value)



def saveValue ( devName , data ):
    "Saves the specified values to the database"

    payload = ""

    for dataPoint in data:
        channelName = dataPoint[0]
        timestamp   = dataPoint[1]
        value       = dataPoint[2]
        payload += channelName + ",device=" + devName  + " value=" + str(value) + " " + repr(timestamp)
        payload = payload[:-1] + "\n" #Remove 'L' in long int representation of timestamp and add newline char

    payload = payload[:-1] #Remove last newline char
    
    
    try:
        r = requests.post('http://192.168.0.105:8086/write?db=eDAQ&precision=ms',data=payload)
    except:
        pass

    return



def getDevName ( MAC ):
    "Looks up the device's name from the specified MAC address"

    return "edaq1"


def getChannelNames ( devName ):
    "Looks up the specified device's channel names"

    return ["temp1", "temp2"]


    
MAC = get_mac()

devName = getDevName(MAC)

channelNames = getChannelNames(devName)


while 1:
    data = []

    for (i, channelName) in enumerate(channelNames):

        (timestamp , value) = readValue(i)
        data.append((channelName, timestamp, value))
        
    saveValue(devName, data)




