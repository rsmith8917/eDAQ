from time import time
from uuid import getnode as get_mac
from ADC import readValue
#from Influx import saveValues
from PostgreSQL import saveValues
from Device import getDevName, getChannelNames
    
MAC = get_mac()

postTime = 10 #seconds

maxBufferLength = 100000

devName = getDevName(MAC)

channelNames = getChannelNames(devName)

starttime = time()

data = []

while 1:

    for (i, channelName) in enumerate(channelNames):

        (timestamp , value) = readValue(i)
        data.append((channelName, timestamp, value))

        
    if ((time() - starttime) > postTime):

        errorCode = saveValues(devName, data)

        if errorCode == 0:

            data = []

        elif len(data) > maxBufferLength:

            overflow = (len(data) - maxBufferLength)
            data = data[overflow:]

        starttime = time()

    print str(len(data))


