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

6. **To exit the virtual environment** when you're done:
   ```bash
   deactivate
   ```

By using this virtual environment, you can install Python packages freely without affecting the system-wide installation.
