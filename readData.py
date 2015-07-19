from time import time
from uuid import getnode as get_mac
from ADC import readValue
from Influx import saveValues
from Device import getDevName, getChannelNames
    
MAC = get_mac()

postTime = 10 #seconds

devName = getDevName(MAC)

channelNames = getChannelNames(devName)

starttime = time()

data = []

while 1:

    for (i, channelName) in enumerate(channelNames):

        (timestamp , value) = readValue(i)
        data.append((channelName, timestamp, value))
    
    if ((time() - starttime) > postTime):
        saveValues(devName, data)
        data = []
        starttime = time()




