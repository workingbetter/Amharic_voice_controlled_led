# Amharic_voice_controlled_led
Amharic voice controlled led using raspberrypi with accessories, linux and python

Steps to Create a Virtual Environment and Install SpeechRecognition
Install python3-venv (if not already installed):

bash
Copy code
sudo apt install python3-venv
Create a virtual environment:

bash
Copy code
python3 -m venv myenv
Activate the virtual environment:

bash
Copy code
source myenv/bin/activate
Install SpeechRecognition inside the virtual environment:

bash
Copy code
pip install SpeechRecognition
Now you can run your Python scripts inside the virtual environment:

bash
Copy code
python3 your_script.py
To exit the virtual environment when you're done:

bash
Copy code
deactivate
By using this virtual environment, you can install Python packages freely without affecting the system-wide installation.
