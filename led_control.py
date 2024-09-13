from gpiozero import LED
import sys
import time

def control_led(command):
    led = LED(17)  # define LED pin according to BCM Numbering
    if command == "በራ":
        led.on()
        print("LED turned on miki")
    elif command == "ጠፋ":
        led.off()
        print("LED turned off")
    else:
        print("Unknown command")
       
    while True:
        time.sleep(1)  # Delay to keep the script running
       
if __name__ == '__main__':
    command = sys.argv[1]  # Get the command from arguments
    control_led(command)
