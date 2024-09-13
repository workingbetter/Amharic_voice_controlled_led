import speech_recognition as sr
import paramiko

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="am-ET")  # Amharic language code
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, I'm having trouble with the speech recognition service.")
    return None

def send_command_to_pi(command):
    # Replace these with your Raspberry Pi credentials
    pi_ip = "192.168.0.10"
    pi_user = "pi"
    pi_password = "raspberry"

    # Set up SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(pi_ip, username=pi_user, password=pi_password)

    # Execute command on Raspberry Pi
    if command:
        stdin, stdout, stderr = ssh.exec_command(f'python3 /home/pi/led_control.py "{command}"')
        print(stdout.read().decode())
        print(stderr.read().decode())

    ssh.close()

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        send_command_to_pi(command)
