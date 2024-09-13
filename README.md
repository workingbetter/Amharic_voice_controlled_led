# Amharic_voice_controlled_led

Amharic voice controlled led using raspberrypi with accessories, linux and python

It looks like `python3-speechrecognition` is not available in the **Raspberry Pi OS repositories** by default. In this case, let's proceed with **creating a virtual environment** and installing `SpeechRecognition` through `pip` inside that environment.

### **Steps to Create a Virtual Environment and Install SpeechRecognition**

1. **Install `python3-venv`** (if not already installed):
   ```bash
   sudo apt install python3-venv
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv myenv
   ```

3. **Activate the virtual environment**:
   ```bash
   source myenv/bin/activate
   ```

4. **Install `SpeechRecognition`** inside the virtual environment:
   ```bash
   pip install SpeechRecognition
   ```

5. **Now you can run your Python scripts inside the virtual environment**:
   ```bash
   python3 your_script.py
   ```


Let's create a full project that incorporates voice recognition (using Google’s Speech-to-Text API) to control your LED through **Raspberry Pi GPIO**.

We’ll combine:
1. **Voice command recognition** to detect when you say "turn on" and "turn off" (in your local language).
2. **LED control** using the `gpiozero` library.

### **Hardware Setup**:
- **Raspberry Pi**: Make sure you have it running with GPIO pin access.
- **LED**: Connected to **GPIO 17** through a **220 ohm resistor**.
- **Laptop**: Using VNC to remotely control the Pi and access your laptop's mic for voice input.

### **Circuit Setup**:
1. **Connect the shorter leg** (cathode) of the LED to the **ground pin** of the Raspberry Pi.
2. **Connect the longer leg** (anode) of the LED to one side of a **220-ohm resistor**.
3. **Connect the other side** of the resistor to **GPIO pin 17**.

---

### **Python Code for Voice-Controlled LED**

This code will:
1. **Listen** for voice commands via the laptop’s microphone (using **Google Speech Recognition**).
2. **Control the LED** based on the recognized commands (turn on/off in your language).

#### **Step 1: Install Dependencies**
On your **Raspberry Pi**, install the necessary libraries:
```bash
pip install SpeechRecognition
pip install gpiozero
pip install pyaudio
```

If `pyaudio` doesn’t install properly, run this:
```bash
sudo apt-get install python3-pyaudio
```

#### **Step 2: Complete Code**

```python
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
    if "እንደታብል" in command:  # Word for "turn on" in Amharic
        led.on()
        print("LED turned ON")
    elif "እንደታታል" in command:  # Word for "turn off" in Amharic
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
```

#### **Step 3: How It Works**
1. **Voice Command**: The `listen_for_command()` function listens for your voice via the **laptop’s mic** (through VNC) and converts it to text.
2. **LED Control**: If the recognized command contains the word for **"turn on"** or **"turn off"** (in Amharic, or another language), it turns the LED on or off using `gpiozero`.

---

### **Full Procedure**:

1. **Set Up Circuit**:
   - Connect the LED to **GPIO 17** via a **220 ohm resistor** as described above.

2. **Enable VNC on Raspberry Pi**:
   - If you haven't already, enable **VNC** on the Pi by going to **Raspberry Pi Configuration** > **Interfaces** > Enable **VNC**.
   - On your laptop, use **VNC Viewer** to remotely access the Pi’s desktop.

3. **Test Speech Recognition**:
   - Run the code on your Pi through VNC and speak commands into your laptop’s mic.
   - **Language Specific Commands**: Ensure that the **Amharic language code** (`am-ET`) or your desired language code is used in the `recognize_google()` function.

4. **Run the Script**:
   - Open a terminal on your Pi and run:
     ```bash
     python3 your_script_name.py
     ```
   - It will listen for commands like **"እንደታብል"** (for "on") or **"እንደታታል"** (for "off") and control the LED accordingly.

5. **Test the LED**:
   - Say **"እንደታብል"** into your mic. The LED should turn on.
   - Say **"እንደታታል"** to turn it off.

---

### **Next Steps**
- **Adjust the Commands**: Depending on the words you use for "on" and "off," modify the `if` conditions in `control_led()`.
- **Test with Different Phrases**: Ensure your voice recognition works well by printing the output before controlling the LED.

This setup will provide a smooth way to control your LED with **voice commands in your language** using **Raspberry Pi** and your **laptop’s mic**.
6. **To exit the virtual environment** when you're done:
   ```bash
   deactivate
   ```

By using this virtual environment, you can install Python packages freely without affecting the system-wide installation.
