import wikipedia

def get_person_info(person_name):
    """
    Fetch information about a person from Wikipedia.
    """
    try:
        # Set language (optional)
        wikipedia.set_lang("en")
        
        # Get summary (first 3 sentences)
        summary = wikipedia.summary(person_name, sentences=3)
        return summary
        
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Please be more specific. Options: {', '.join(e.options[:5])}..."
    except wikipedia.exceptions.PageError:
        return "Sorry, no information found for this person."
    except Exception as e:
        return f"Error fetching data: {str(e)}"