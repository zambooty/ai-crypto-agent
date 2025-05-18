import feedparser
import html # For unescaping HTML entities if present in content
import requests # Import the requests library

# It's good practice to also import requests if you were to fetch the URL content manually first,
# but feedparser.parse() can handle fetching the URL directly.
# import requests

COINDESK_RSS_URL = "https://www.coindesk.com/arc/outboundfeeds/rss/"

def fetch_coindesk_news():
    """
    Fetches and parses the CoinDesk RSS feed.
    Returns a list of dictionaries, where each dictionary represents an article.
    """
    print(f"Fetching news from: {COINDESK_RSS_URL}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    articles = []
    try:
        response = requests.get(COINDESK_RSS_URL, headers=headers, timeout=10) # Added timeout
        print(f"HTTP Status Code: {response.status_code}")
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        
        # It's good to check content type if possible, though feedparser is generally robust
        # print(f"Content-Type: {response.headers.get('content-type')}")
        
        # Ensure content is bytes for feedparser if it expects bytes, or str if it expects str.
        # feedparser usually handles this well with response.content (bytes) or response.text (decoded string).
        feed = feedparser.parse(response.content) # Using response.content (bytes)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return articles # Return empty list on request failure
    except Exception as e:
        print(f"An unexpected error occurred during fetching: {e}")
        return articles

    if feed.bozo:
        print(f"Warning: Feed may be ill-formed. Bozo flag set with exception: {feed.bozo_exception}")
        # We can still try to process entries if feed.entries is populated
        if not feed.entries:
            print("No entries found in the feed despite bozo flag.")
            # Optionally, print some of the raw content to see what was received
            # print("Raw feed content snippet:")
            # print(response.text[:500]) # Print first 500 chars of text response
            return articles

    print(f"Found {len(feed.entries)} articles.")

    for entry in feed.entries:
        article = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", None), # .get for optional fields
            "published_parsed": entry.get("published_parsed", None), # feedparser provides a parsed time tuple
            "summary": entry.get("summary", None),
            "guid": entry.get("id", entry.link), # Use link as fallback for guid
            "author": entry.get("author", None)
        }
        
        # Attempt to get full content if available
        if hasattr(entry, "content") and entry.content:
            # entry.content is usually a list, take the first item
            # The content might be HTML, so it's stored as is.
            # For plain text display, you might need to strip HTML tags later.
            article["full_content_html"] = entry.content[0].value
        elif hasattr(entry, "content_encoded"): # some feeds use <content:encoded>
             article["full_content_html"] = entry.content_encoded
        else:
            article["full_content_html"] = entry.get("summary", None) # Fallback to summary if no full content

        articles.append(article)
    
    return articles

if __name__ == "__main__":
    print("Starting news fetching process...")
    news_items = fetch_coindesk_news()
    if news_items:
        print(f"\n--- Fetched {len(news_items)} News Articles ---")
        for i, item in enumerate(news_items[:5]): # Print details of the first 5 articles
            print(f"\nArticle {i+1}:")
            print(f"  Title: {item['title']}")
            print(f"  Link: {item['link']}")
            print(f"  Published: {item['published']}")
            # print(f"  Summary: {html.unescape(item['summary']) if item['summary'] else 'N/A'}") # Example of unescaping
            # print(f"  Author: {item['author']}")
            # For full content, you'd typically process it further (e.g., strip HTML for NLP)
            # print(f"  Full Content Snippet (HTML): {item['full_content_html'][:200] + '...' if item['full_content_html'] else 'N/A'}")
        if len(news_items) > 5:
            print(f"\n... and {len(news_items) - 5} more articles.")
    else:
        print("No news items fetched or an error occurred.")
