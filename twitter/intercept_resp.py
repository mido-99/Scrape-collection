from playwright.async_api import async_playwright
import asyncio
import jmespath


xhr_calls = []
def intercept_response(response):
    """capture all background requests and save them"""
    
    if response.request.resource_type == "xhr":
        xhr_calls.append(response)
    return response

async def scrape(url: str):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1280, "height": 720})
        page = await context.new_page()

        page.on("response", intercept_response)
        await page.goto(url)
        await page.wait_for_selector("[data-testid='tweet']")

        tweet_calls = [f for f in xhr_calls if "TweetResult" in f.url]
        for xhr in tweet_calls:
            data = await xhr.json()
            return data['data']['tweetResult']['result']

result = asyncio.run(scrape('https://twitter.com/Scrapfly_dev/status/1664267318053179398'))
# print(xhr_calls)
# print(result)

def parse_tweet(data):
    '''Parse Twitter tweet'''
    
    result = jmespath.search(
        """{
        created_at: legacy.created_at,
        attached_urls: legacy.entities.urls[].expanded_url,
        attached_urls2: legacy.entities.url.urls[].expanded_url,
        attached_media: legacy.entities.media[].media_url_https,
        tagged_users: legacy.entities.user_mentions[].screen_name,
        tagged_hashtags: legacy.entities.hashtags[].text,
        favorite_count: legacy.favorite_count,
        bookmark_count: legacy.bookmark_count,
        quote_count: legacy.quote_count,
        reply_count: legacy.reply_count,
        retweet_count: legacy.retweet_count,
        quote_count: legacy.quote_count,
        text: legacy.full_text,
        is_quote: legacy.is_quote_status,
        is_retweet: legacy.retweeted,
        language: legacy.lang,
        user_id: legacy.user_id_str,
        id: legacy.id_str,
        conversation_id: legacy.conversation_id_str,
        source: source,
        views: views.count
    }""", data
    )
    
    result['text'] = ''.join(result['text'].rsplit('https', 1)[:-1]).strip()
    return result

print(parse_tweet(result))