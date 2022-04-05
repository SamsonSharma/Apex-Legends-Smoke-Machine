import serial
import time as t
arduino = serial.Serial('/dev/ttyACM1', 9600)
from pynput.keyboard import Key, Listener



# use this for Xserv: xhost local:root
# run script as superuser

def partytime():
    arduino.write(str.encode('1')) # write(b'1')

def sadtime():
    arduino.write(str.encode('0'))

def show(key):
    try:
        if key.char == 'q' or key.char == 'Q':
            partytime()
            print("ptime")
            t.sleep(5)
            sadtime()
            
    except:
         print("shift buddy")

   
          
    # by pressing 'delete' button 
    # you can terminate the loop 
    if key == Key.delete: 
        return False
  
# Collect all event until released
with Listener(on_press = show) as listener:
    listener.join()

