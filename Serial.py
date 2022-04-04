import serial
import time
import json
from pubnub.pubnub import PubNub
from pubnub.pubnub import SubscribeListener
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException
import pubnub
pnconf = PNConfiguration()
pnconf.publish_key = 'pub-c-3fd6be7a-dcdf-4f41-aae4-c189865725dc'
pnconf.subscribe_key = 'sub-c-023cb6a4-7a58-11ec-add2-a260b15b99c5'
pnconf.uuid = 'mehta'
pubnub = PubNub(pnconf)
channel='Mehta728' 
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
pubnub.subscribe().channels(channel).execute()
my_listener.wait_for_connect()
print('connected')
x=0
y=0

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    data=int_val = int.from_bytes(data, "big", signed="True")
    return data


while True:
    result = my_listener.wait_for_message_on(channel)
    print(result.message['humidity'])
    x= result.message['temp']
    y= result.message['humidity']
    if(y > 20 and y < 40):
        value = write_read('1')
    elif(y > 40 and y < 50):
        value = write_read('2')
    elif(y> 50):
        value = write_read('3')
    #value = write_read(num)
    #print(value) # printing the value



'''import serial
import time

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

for i in range(50):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = string # convert the unicode string to an int
        print(num)

ser.close()'''
'''import serial
import time
from pubnub.pubnub import PubNub
from pubnub.pubnub import SubscribeListener
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException
import pubnub
pnconf = PNConfiguration()
pnconf.publish_key = 'pub-c-3dd4d929-0243-4c13-a11f-d8076bbcfc0c'
pnconf.subscribe_key = 'sub-c-278756ba-8923-11ec-9f2b-a2cedba671e8'
pnconf.uuid = 'karan1199'
pubnub = PubNub(pnconf)
channel='karan1199' 
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
pubnub.subscribe().channels(channel).execute()
my_listener.wait_for_connect()
print('connected')
data = { 
'message': 0
}
pubnub.publish().channel(channel).message(data).sync()

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    data=int_val = int.from_bytes(data, "big", signed="True")
    return data


while True:
    result = my_listener.wait_for_message_on(channel)
    print(result.message)
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value
'''
    





