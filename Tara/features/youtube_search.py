import webbrowser

def search_on_youtube(query, search_type="video"):
    """
    Searches or plays a song on YouTube based on the given query.
    :param query: The search query (e.g., "how to code in Python").
    :param search_type: Type of search - "song" or "video".
    :return: True if successful, False if failed.
    """
    try:
        # Construct the YouTube search URL
        search_query = "+".join(query.split())  # Replace spaces with "+"
        
        if search_type == "song":
            print(f"TARA: Playing '{query}' on YouTube...")
            url = f"https://www.youtube.com/results?search_query={search_query}+song"
        else:
            print(f"TARA: Searching '{query}' on YouTube...")
            url = f"https://www.youtube.com/results?search_query={search_query}"

        # Open the URL in the default web browser
        webbrowser.open_new(url)
        return True
    except Exception as e:
        print(f"TARA: Error searching YouTube - {e}")
        return False
