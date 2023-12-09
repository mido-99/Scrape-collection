from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.zillow.com/ca/fsbo/'

r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1, timeout=5)

prices = r.html.find('span.PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr')
print (len(prices))

for p in range(len(prices)):
    print(p + prices[p])