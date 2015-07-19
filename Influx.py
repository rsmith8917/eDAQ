import requests

def saveValues ( devName , data ):
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

