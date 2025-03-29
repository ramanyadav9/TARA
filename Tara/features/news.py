import requests

def get_news():
    """
    Fetches the top 4 latest news headlines.
    :return: List of top 4 headlines or error message.
    """
    try:
        # API call to NewsAPI
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=f52786f46dab4727a167c77429a55088")
        
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            # Get the articles and limit to top 4
            articles = data.get("articles", [])[:4]
            
            if not articles:
                return ["No news articles found."]
            
            # Extracting titles
            headlines = [article['title'] for article in articles]
            return headlines
        else:
            return [f"Failed to fetch news. Status code: {r.status_code}"]
    
    except Exception as e:
        return [f"Error fetching news: {str(e)}"]
