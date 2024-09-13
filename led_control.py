from gpiozero import LED
import sys
import signal
import time

# Initialize the LED (connected to GPIO pin 17)
led = LED(17)

def control_led(command):
    if command == "በራ":  # Amharic for "turn on"
        led.on()
        print("LED turned on, Miki")
    elif command == "ጠፋ":  # Amharic for "turn off"
        led.off()
        print("LED turned off")
    else:
        print("Unknown command")

def signal_handler(sig, frame):
    print("\nExiting gracefully...")
    led.off()  # Ensure LED is off when exiting
    sys.exit(0)

# Set up signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    try:
        while True:
            # Assume a command is passed as an argument when the script starts
            if len(sys.argv) > 1:
                command = sys.argv[1]  # Get the command from arguments
                control_led(command)
            else:
                print("No command provided. Waiting for input...")
                time.sleep(1)  # Sleep for a short period to avoid CPU overload
    except KeyboardInterrupt:
        signal_handler(None, None)  # Call the signal handler to clean up
