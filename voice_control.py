import speech_recognition as sr # For voice recognition
import RPi.GPIO as GPIO  # For controlling GPIO pins
import time

# Use GPIO pin 18 to control the LED
LIGHT_GPIO_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_GPIO_PIN, GPIO.OUT)

# Turn LED on
def turn_light_on():
    GPIO.output(LIGHT_GPIO_PIN, GPIO.HIGH)
# Turn LED off
def turn_light_off():
    GPIO.output(LIGHT_GPIO_PIN, GPIO.LOW)
# Listen to user's voice and return command
def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            return command
# Handle the voice command
def handle_command(command):
    if "light on" in command:
        turn_light_on()
    elif "light off" in command:
        turn_light_off()
    else:
        print("Command not recognized.")
# Main program loop
if __name__ == "__main__":
    try:
        while True:
            command = listen_for_command()
            if command:
                handle_command(command)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped by user.")
    finally:
        GPIO.cleanup()
