import pyjokes

def get_joke():
    """
    Fetches a random joke.
   """
    try:
        joke = pyjokes.get_joke()
        return joke
    except Exception as e:
        return f"Error fetching joke: {e}"
