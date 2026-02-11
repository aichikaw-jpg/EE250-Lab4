"""EE 250L Lab 04 start chain code """


import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

#function for receiving the number from pong
#adds 1 and sends to the 2nd terminal
def on_message_from_pong(client,userdata,message):
        #cast the payload and convert it to integer
        messageNum = int(message.payload.decode())

        #add 1 to it, and put it into a variable for the new payload
        newMessage =  messageNum + 1

        #print the received payload
        print("Number Received: ", messageNum)
        #add a delay
        time.sleep(1)

        #send back the new message to ping
        client.publish("aichikaw/ping", str(newMessage))


if __name__ == '__main__':
    #IP address of rpi
    ip_address="10.189.147.211" 
    """your code here"""

    #payload: integer number at the start
    payloadNum = 4

    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python.
        
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    #connect to the raspberry pi
    client.connect(host="10.189.147.211", port=1883, keepalive=60)

    #subscribe to pong and run on_message_from_pong when it receives a message
    client.subscribe("aichikaw/pong")
    client.message_callback_add("aichikaw/pong", on_message_from_pong)

    #run once at the start
    #publish to rpi broker
    #print initial number
    print("Initial number:", payloadNum)
    client.publish("aichikaw/ping", f"{payloadNum}")
    time.sleep(4)


    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    #starts a loop
    client.loop_start()
    #keeps the loop going
    while True: 
        #creates a delay 
        time.sleep(1)

    
    

    


