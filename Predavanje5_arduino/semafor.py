import pyfirmata # Import pyFirmata
import time # Import the time

port = 'COM4'# Windows
#port = '/dev/ttyACM3' # Linux
#port = '/dev/tty.usbmodem11401'# Mac

HIGH = True# Create a high state for turn on led 
LOW = False # Create a low state for turn off led 
board = pyfirmata.Arduino(port) # Initialize the communication with the Arduino card
LED_pin13 = board.get_pin('d:13:o')
LED_pin12 = board.get_pin('d:12:o')
LED_pin11 = board.get_pin('d:11:o')# Initialize the pin (d => digital, 13 => Number of the pin, o => output)
    
for i in range(4): # Loop to blink the micro-led dix times
    LED_pin13.write(HIGH) # Turn on the led
    time.sleep(2)
    LED_pin12.write(HIGH)
    time.sleep(1)
    LED_pin13.write(LOW)
    LED_pin12.write(LOW)
    time.sleep(0.1)
    LED_pin11.write(HIGH)
    time.sleep(3)
    LED_pin11.write(LOW)
    time.sleep(0.1)
    LED_pin12.write(HIGH)
    time.sleep(1)
    LED_pin12.write(LOW)
    time.sleep(0.1)
    LED_pin13.write(HIGH)
    time.sleep(1)

board.exit() # Closing the communication with the Arduino card

