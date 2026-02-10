import speech_recognition as sr
import pyttsx3
import wikipedia
# Wake word
WakeUp = "jarvis"

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)      # slower speech
engine.setProperty('volume', 1.0)    # max volume

# Set voice (optional - use female voice if available)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # voices[1] is usually female

recognizer = sr.Recognizer()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listenforwakeup():
    with sr.Microphone() as source:
        print("🎤 Listening for Wake Word...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            speak(f"You said: {command}")
            if WakeUp in command.lower():
                print("✅ Wake Word Detected")
                return True
        except sr.WaitTimeoutError:
            speak("⏱No speech detected (timeout).")
        except sr.UnknownValueError:
            speak(" Could not understand.")
        except sr.RequestError:
            speak(" Could not request results. Check your internet.")
        return False

def recognize_speech():
    with sr.Microphone() as source:
        speak("Hello Sir, Good morning. Jarvis at your service.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening for command...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            speak("Timeout while waiting for command.")
        except sr.UnknownValueError:
            speak("Could not understand the command.")
        except sr.RequestError:
            speak("Google API request failed.")
        return ""

# Main loop
while True:
    if listenforwakeup():
        command = recognize_speech()
        if command:
            speak(f"You said: {command}")
            if "exit" in command.lower():
                speak("Goodbye!")
                break
    else:
        print("👂 No wake word. Listening again...\n")
