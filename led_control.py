from gpiozero import LED
import sys

led = LED(17)  # define LED pin according to BCM Numbering

command = sys.argv[1]  # Get the command from arguments

if command.lower() == "on":
    led.on()
    print("LED turned on")
elif command.lower() == "off":
    led.off()
    print("LED turned off")
else:
    print("Unknown command")
