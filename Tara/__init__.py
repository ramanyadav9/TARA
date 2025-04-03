import speech_recognition as sr
import pyttsx3

from Tara.features import datetime
from Tara.features import youtube_search
from Tara.features import google_search
from Tara.features import tell_about_person
from Tara.features.news import get_latest_news
from Tara.features import tell_joke
from Tara.features import weather



# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class TaraAssistant:
    def __init__(self):
        pass

    def mic_input(self):
        """
        Fetch input from microphone.
        :return: User's voice input as text if successful, False if failed.
        """
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.energy_threshold = 4000
                audio = r.listen(source)
            try:
                print("Recognizing...")
                command = r.recognize_google(audio, language='en-in').lower()
                print(f'You said: {command}')
            except:
                print('Please try again.')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return False

    def tts(self, text):
        """
        Convert text to speech.
        :param text: Text to be spoken.
        :return: True if successful, False if failed.
        """
        try:
            engine.say(text)
            engine.runAndWait()
            engine.setProperty('rate', 175)
            return True
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
            return False

    def tell_me_date(self):
        """
        Get the current date.
        """
        return datetime.get_date()

    def tell_time(self):
        """
        Get the current time.
        """
        return datetime.get_time()
    
    def search_on_youtube(self, query, search_type="video"):
        """
        Search or play content on YouTube.
        """
        return youtube_search.search_on_youtube(query, search_type)


   
    
    def search_on_google(self, query):
        """
        Perform a Google search.
        """
        return google_search.search_on_google(query)
    
    def tell_about_person(self, person_name):
        """
        Fetch and speak information about a person from Wikipedia. Summary text.
        """
        info = tell_about_person.get_person_info(person_name)
        self.tts(info)
        return info
    

    def get_latest_news(self):
        """
        fetch the news from the new api and give top 4 headlines 
        """

        return get_latest_news()
    
    def get_joke(self):
        """
        Fetch and speak a joke.
        """
        return tell_joke.get_joke()
    

    def tell_weather(self, city):
        """
        Fetch and speak the weather of a city.
        :param city: Name of the city.
        """
        weather_info = weather.get_weather(city)
        self.tts(weather_info)
        return weather_info

