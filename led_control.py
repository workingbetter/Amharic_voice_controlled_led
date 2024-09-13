from gpiozero import LED
import sys
import time
led = LED(17)

def control_led(command):
      # define LED pin according to BCM Numbering
    if "አብሪው" in command:
        led.on()
        time.sleep(4)
        print("LED turned on")
        
    elif command == "ጠፋ":
        led.off()
        time.sleep(4)
        print("LED turned off")
        
    else:
        print("Unknown command")
              
if __name__ == '__main__':
    try:
        command = sys.argv[1]  # Get the command from arguments
        control_led(command)
    except KeyboardInterrupt:
        print("ending")
