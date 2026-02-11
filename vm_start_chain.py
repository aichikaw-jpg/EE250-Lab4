"""EE 250L Lab 04 start chain code """


import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


def on_message_from_pong(client,userdata,message):
        #cast the payload and convert it to integer
        messageNum = int(message.payload.decode())

        #add 1 to it, and put it into a variable for the new payload
        newMessage =  messageNum + 1

        #print the received payload
        print("Number Received: ", messageNum)
        time.sleep(1)

        client.publish("aichikaw/ping", str(newMessage))


if __name__ == '__main__':
    #IP address of rpi
    ip_address="10.189.147.211" 
    """your code here"""

    #payload: integer number
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

    client.connect(host="10.189.147.211", port=1883, keepalive=60)
    client.subscribe("aichikaw/pong")
    client.message_callback_add("aichikaw/pong", on_message_from_pong)

    #publish to rpi broker
    client.publish("aichikaw/ping", f"{payloadNum}")
    print("")
    time.sleep(4)


    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    while True: 
        time.sleep(1)

    
    

    


