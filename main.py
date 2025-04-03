import sys
import random
from Tara import TaraAssistant
# from Tara.features.youtube_search import search_on_youtube
from Tara.features.google_search import search_on_google



# ================================ MEMORY ===========================================================================================================
GREETINGS = ["hello tara", "tara", "wake up tara", "you there tara", "time to work tara", "hey tara", "ok tara", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir", "your wish my command", "how can i help you sir?", "i am online and ready sir"]

# Initialize TARA
tara = TaraAssistant()

def speak(text):
    """
    Simulates TARA speaking.
    :param text: Text to be spoken.
    """
    print(f"TARA: {text}")
    tara.tts(text)

def startup():
    """
    Initializes TARA and performs startup tasks.
    """
    speak("Initializing TARA")
    # speak("Starting all systems applications")
    # # speak("Installing and checking all drivers")
    # # speak("Calibrating and examining all the core processors")
    # # speak("Checking the internet connection")
    # # speak("Wait a moment sir")
    # # speak("All drivers are up and running")
    # # speak("All systems have been activated")
    speak("Now I am online")
    hour = int(tara.tell_time().split(":")[0])
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    current_time = tara.tell_time()
    speak(f"Currently, it is {current_time}")
    speak("I am TARA. Online and ready, sir. Please tell me how may I help you.")

def main():
    """
    Main function to handle TARA's tasks.
    """
    startup()

    while True:
        command = tara.mic_input()  # Fetch voice input

        if not command:
            continue
        
        # date and time command 
        if "time" in command or "date" in command:
            if "time" in command:
                current_time = tara.tell_time()
                speak(f"Sir, the time is {current_time}")
            if "date" in command:
                current_date = tara.tell_me_date()
                speak(f"Sir, today's date is {current_date}")


        # YouTube - Play Song   # to perform this means directly playing song on yt i have to get youtube data api 
        elif any(word in command for word in ["play", "song", "music"]):
            song_name = command.replace("play", "").replace("song", "").replace("music", "").strip()
            if song_name:
                speak(f"Playing '{song_name}' on YouTube.")
                tara.search_on_youtube(song_name, search_type="song")
            else:
                speak("Please specify the song name.")

        # YouTube - Search Video
        elif any(word in command for word in ["youtube", "video", "find"]):
            query = command.replace("youtube", "").replace("find", "").replace("video", "").strip()
            if query:
                speak(f"Searching '{query}' on YouTube.")
                tara.search_on_youtube(query, search_type="video")
            else:
                speak("Please specify what you want to search for.")



        # google pe search karne ke liye
        elif "google" in command:
            query = command.replace("google", "").strip()
            if query:
                search_on_google(query)
            else:
                speak("Please specify what you want to search for.")


        # tell about the any person via wikipidia
        elif "tell me about" in command or "who is" in command or "search for" in command:
            if "tell me about" in command:
                person = command.split("tell me about", 1)[1].strip()
            elif "who is" in command:
                person = command.split("who is", 1)[1].strip()
            elif "search for" in command:
                person = command.split("search for", 1)[1].strip()
            
            if person:
                speak(f"Fetching information about {person}...")
                info = tara.tell_about_person(person)
                print(info)  # Optional: Display text in console
            else:
                speak("Please specify a person's name.")

        # Get Latest News
        elif "news" in command or "headlines" in command:
            speak("Fetching the latest news...")
            news_list = tara.get_latest_news()

            for news in news_list:
                speak(news)

        # tell random jokes 
        elif "joke" in command or "tell me a joke" in command:
            speak("Here's a joke for you.")
            joke = tara.get_joke()
            # print(joke)  
            speak(joke)

        # get the weather for any city asked from user
        elif "weather" in command or "temperature" in command:
            speak("Which city’s weather would you like to know?")
            city = tara.mic_input()
    
            if city:
                speak(f"Fetching weather details for {city}.")
                weather_report = tara.tell_weather(city)
                speak(weather_report)
                print(weather_report)  # Optional: Display in console
            else:
                speak("Sorry, I didn't catch the city name.")








        

        elif command in GREETINGS:
            speak(random.choice(GREETINGS_RES))

        elif "exit" in command or "bye" in command or "goodbye" in command:
            speak("Alright sir, going offline. It was nice working with you.")
            sys.exit()

        else:
            speak("Sorry sir, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()