import webbrowser

def search_on_google(query):
    """
    Searches for a query on Google or opens a website if a URL is provided.
    """
    # if not query.strip():
    #     print("TARA: Please specify something to search for.")
    #     return False

    try:
        # Directly open websites if detected
        if "open" in query.lower():
            website = query.lower().replace("open", "").strip()
            url = f"https://www.{website}.com"
            print(f"TARA: Opening {website}...")
        else:
            # Construct the Google search URL
            search_query = "+".join(query.split())
            url = f"https://www.google.com/search?q={search_query}"
            print(f"TARA: Searching for '{query}' on Google...")

        # Open the URL in the default web browser
        webbrowser.open_new(url)
        return True
    except Exception as e:
        print(f"TARA: Error searching Google - {e}")
        return False
