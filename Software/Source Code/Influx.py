import datetime
import requests

def saveValues ( devName , data ):
    "Saves the specified values to the database"

    payload = ""

    for dataPoint in data:
        channelName = dataPoint[0]
        timestamp   = dataPoint[1]
        value       = dataPoint[2]

        timestamp = round((timestamp - datetime.datetime(1970,1,1)).total_seconds()*1000)

        payload += channelName + ",device=" + devName  + " value=" + str(value) + " " + repr(timestamp)
        payload = payload[:-2] + "\n" #Remove '.0' at end of timestamp and add newline char

    payload = payload[:-1] #Remove last newline char
    
    #print payload

    errorCode = 0    

    try:
        r = requests.post('http://192.168.0.105:8086/write?db=eDAQ&precision=ms', data=payload, timeout=1)
        if( r.status_code != 204 ):
            #print r.status_code
            errorCode = 1
    except:
        errorCode = 1
        pass

    return errorCode

