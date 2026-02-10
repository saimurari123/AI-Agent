import random
import speech_recognition as sr
import pyttsx3
import datetime

# Initialize TTS engine
engine = pyttsx3.init()

# Listening state
listening = False

# Speak function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Intent dictionaries
intent = {
        'greeting': ['hello', 'hi', 'hey', 'howdy', 'greetings', 'salutations'],
    'farewell': ['bye', 'goodbye', 'see you later', 'take care', 'farewell'],
    'gratitude': ['thank you', 'thanks', 'appreciate it', 'grateful', 'much obliged'],
    'query': ['how are you', 'how are you doing', 'how is it going', 'how do you do', 'how are you feeling'],
    'weather': ['weather', 'forecast', 'temperature'],
    'time': ['time'],
    'reminder': ['remind me', 'set a reminder', 'remind me to', 'set reminder'],
    'joke': ['tell me a joke', 'make me laugh', 'joke', 'funny', 'humor'],
    'meaning': ['what is', 'define', 'meaning of', 'explain', 'tell me about'],
    'translate': ['translate', 'translation', 'convert', 'interpret', 'change'],
    'who are you': ['who are you', 'tell me about yourself', 'introduce yourself', 'who is this', 'what are you'],
    'what is your name': ['what is your name', 'who are you', 'name', 'your name', 'identify yourself']
}

response = {
    'greeting': ['Hello! How can I assist you today?', 'Hi there! What can I do for you?', 'Hey! How may I help you?'],
    'farewell': ['Goodbye! Have a great day!', 'See you later! Take care!', 'Farewell! Until next time!'],
    'gratitude': ['You are welcome!', 'No problem! Anytime!', 'Glad to help!'],
    'query': ['I am just a computer program, but I am doing well!', 'I am functioning as expected, thank you!', 'I am here to assist you!'],
    'weather': ['The weather is great!', 'It is sunny outside!', 'It looks like it might rain today!'],
    'time': [datetime.datetime.now().strftime("The current time is %H:%M:%S")],
    'joke': [
        'Why did the scarecrow win an award? Because he was outstanding in his field!',
        'Why don’t scientists trust atoms? Because they make up everything!',
        'I told my computer I needed a break, and now it won’t stop sending me beach wallpapers!'
    ],
    'translate': ['I can help you with translations. What do you want to translate?', 'Please provide the text you want to translate!'],
    'who are you': ['I am your virtual assistant!', 'I am a computer program designed to help you!', 'I am here to assist you with anything you need!'],
    'what is your name': ['My name is Jarvis!', 'I am called Jarvis!', 'You can call me Jarvis!'],
}

# Process command
def process__command(command):
    command = command.lower()
    found_intent = False

    if 'stop' in command:
        global listening
        listening = False
        speak("Okay, I’ll stop listening. Say 'Jarvis' when you need me.")
        return

    for key, keywords in intent.items():
        for keyword in keywords:
            if keyword in command:
                response_list = response.get(key)
                if response_list:
                    reply = random.choice(response_list)
                    speak(reply)
                    found_intent = True
                    return

    if not found_intent:
        speak("I'm not sure how to respond to that.")

# Main listening loop
def process_voice():
    global listening
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("Jarvis is standing by. Say 'Jarvis' to activate me.")
        while True:
            try:
                print("🎤 Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio).lower()
                print("You:", command)

                if not listening:
                    if "jarvis" in command:
                        listening = True
                        speak("Yes, I’m listening.")
                else:
                    process__command(command)

            except sr.UnknownValueError:
                # Could not understand audio
                pass
            except sr.WaitTimeoutError:
                # Timeout waiting for speech
                pass
            except Exception as e:
                print("Error:", str(e))

# Start the assistant
if __name__ == "__main__":
    process_voice()
