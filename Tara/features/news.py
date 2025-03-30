import requests
from Tara.config import config

def get_latest_news():
    """
    Fetches the latest news headlines using NewsAPI.
    """
    try:
        api_key = config.NEWS_API_KEY  # Import API key from config
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])[:4]  # Get top 4 news headlines
            
            if articles:
                news_list = [article["title"] for article in articles]
                return news_list
            else:
                return ["No news available at the moment."]
        else:
            return ["Failed to fetch news. Please try again later."]
    
    except Exception as e:
        return [f"Error: {str(e)}"]
