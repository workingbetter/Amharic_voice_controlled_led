# -*- coding: utf-8 -*-
"""Amharic voice controlled Led.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1itAISJ6byfBdTbZn-YCLJeZTGDLI6D5I
"""

import speech_recognition as sr
from gpiozero import LED
from time import sleep

# Setup for the LED
led = LED(17)

# Initialize recognizer
recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google API in Amharic (replace with your language code)
            command = recognizer.recognize_google(audio, language="am-ET")  # Use "am-ET" for Amharic
            print(f"Recognized Command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

def control_led(command):
    # Replace "on_word" and "off_word" with your actual spoken words in your language
    if "አብሪው" in command:  # Word for "turn on" in Amharic
        led.on()
        print("LED turned ON")
    elif "አጥፊው" in command:  # Word for "turn off" in Amharic
        led.off()
        print("LED turned OFF")
    else:
        print("Unrecognized command.")

try:
    while True:
        command = listen_for_command()
        if command:
            control_led(command)
        sleep(1)

except KeyboardInterrupt:
    print("Ending program")