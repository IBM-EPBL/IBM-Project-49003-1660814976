import wiotp.sdk.device
import time
import os
import datetime
import random
myComfig = {
    "identity": {
        "orgId": "k7mplh",
        "typeId": "NodeMCU",
        "deviceId": "12345"
    },
    "auth": {
        "token": "12345678"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHamdlers=None)
client.connect()


def myCommandCallback(cmd):
    print("Message Received From IBM IoT Platform: %s "%cmd.data['command'])
    m=cmd.data['command']
    if(m=="motoron"):
        print("Motor is switched on")
    elif(m=="motoroff"):
        print("Motor is switched off")
    print(" ")
while True:
    soil=random.randint(0,100)
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    myData=('soil_moisture': soil, 'temperature': temp,'humidity':hum)
    client.pulishEvent(enterId="status", msgFormat="json",data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s",myData)
    time.sleep(2)
    client.commandCallback= myCommandCallback
client.disconnect()
