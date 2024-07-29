from playwright.async_api import async_playwright
import asyncio
import jmespath
from dotenv import get_variable


xhr_calls = []
def intercept_response(response):
    """capture all background requests and save them"""
    
    if response.request.resource_type == "xhr":
        xhr_calls.append(response)
    return response

async def scrape(url: str):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=4)
        context = await browser.new_context(viewport={"width": 1280, "height": 720})
        page = await context.new_page()

        page.on("response", intercept_response)
        await page.goto(url)
        print('Login required!')
        await page.wait_for_selector('''//span[text()='Sign in to X']''', timeout=20_000)
        await page.fill('input[autocomplete="username"]', get_variable('.env', 'USERNAME'))
        # await page.fill('text="hone, email, or username"', dotenv.get_variable('.env', 'USERNAME'))
        await page.click('text="Next"')
        await page.fill('text="Password"', get_variable('PASSWORD'))
        await page.click('text="Log in"')
        
        feed = await page.wait_for_selector("[data-testid='primaryColumn']", timeout=20000)
        return xhr_calls
    
result = asyncio.run(scrape("https://x.com/Scrapfly_dev"))
print(result)