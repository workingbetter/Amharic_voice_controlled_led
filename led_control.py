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
    while True:
        try:
            # Wait for a command input through the command-line argument
            if len(sys.argv) > 1:
                command = sys.argv[1]  # Get the command from arguments
                control_led(command)
                sys.argv = []  # Clear the argument after processing
            else:
                time.sleep(1)  # Sleep to avoid high CPU usage when no command is given
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(1)  # Ensure we don't crash the script on error
