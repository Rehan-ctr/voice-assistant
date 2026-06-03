import pyttsx3
import speech_recognition as sr
import webbrowser

# Initialize the speech engine and recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    command_clean = c.lower().strip()
    if "open google" in command_clean:
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facebook" in command_clean:
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command_clean:
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in command_clean:
        speak("opening whatsapp")
        webbrowser.open("https://whatsapp.com")
    else:
        speak("Command not recognized")

if __name__ == "__main__":
    speak("hey how can i help you")
    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                # Adjust for background noise for better accuracy
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening for wake word 'google'...")
                # Listen without a strict 1-second limit
                audio = r.listen(source, timeout=5)
            
            word = r.recognize_google(audio)
            print(f"Heard: {word}")
            
            # Robust wake word check
            if "google" in word.lower():
                speak("boll be")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print("google active. Listening for command...")
                    audio = r.listen(source, timeout=5)
                    command = r.recognize_google(audio)
                    print(f"Command heard: {command}")
                    processCommand(command)
                    
        except sr.WaitTimeoutError:
            # Silently continue when no sound is captured to avoid console clutter
            continue
        except sr.UnknownValueError:
            # Speech recognition couldn't understand the audio, keep listening
            continue
        except sr.RequestError as e:
            print(f"API Request Error: {e}")
        except Exception as e:
            print(f"Error: {e}")