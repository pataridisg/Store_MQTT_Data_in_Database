#!python3
import paho.mqtt.client as mqtt  #import the client1
import time 
#import I2C_LCD_driver

def on_connect(client, userdata, flags, rc):
    if rc==0:
		client.connected_flag=True #set flag
		print("connected OK")
		# mylcd.lcd_clear()
		# mylcd.lcd_display_string("Connected!", 1)
    else:
		print("Bad connection Returned code=",rc)
		# mylcd.lcd_clear()
		# mylcd.lcd_display_string("Bad connection", 1)
		
def on_message(client, userdata, message):
	print ("Time: %s" %time.strftime("%H:%M:%S"))
	print ("Message received: " + message.topic + ": " + message.payload)
	# mylcd.lcd_clear()
	# mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1) 
	# mylcd.lcd_display_string(message.topic + ": " + message.payload, 2) 


#mylcd = I2C_LCD_driver.lcd()

mqtt.Client.connected_flag=False	#create flag in class
broker="192.168.1.10"
port = 1883 
user = "pataridis"
password = "rs232"
mytopiclist = [("dummytemp1",0), ("hum1", 0) , ("temp2", 0), ("hum2", 0)]
#mytopic = "temp1"


# mylcd.lcd_clear()
# mylcd.lcd_display_string("Connecting...", 1)
# time.sleep(1)

client = mqtt.Client("pytemp1")             		#create new instance 
client.username_pw_set(user, password=password)    	#set username and password
client.on_connect=on_connect  						#bind call back function
client.on_message= on_message                      	#attach function to callback
client.loop_start()


print("Connecting to broker ",broker, "on port ", port)
client.connect(broker, port)      #connect to broker

while not client.connected_flag: #wait in loop
	print("Waiting for connection...")
	time.sleep(2)

print("Subscribing...")
# mylcd.lcd_clear()
# mylcd.lcd_display_string("Subscribing...", 1)
# time.sleep(2)
client.subscribe(mytopiclist)

try:
    while True:
		time.sleep(1)
		

 
except KeyboardInterrupt:
	print "Exiting...."
	time.sleep(1)
	client.disconnect()
	client.loop_stop()

# client.loop_stop()    #Stop loop 
# client.disconnect() # disconnect