import requests
from bs4 import BeautifulSoup

# URL for Yahoo Finance page
url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'

# Headers to mimic a browser request
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Successfully retrieved the webpage')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'lxml')

# Extract specific company details
try:
    # Extracting specific company details
    previous_close = soup.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'}).text.strip()
    open_price = soup.find('fin-streamer', {'data-field': 'regularMarketOpen'}).text.strip()
    day_range = soup.find('fin-streamer', {'data-field': 'regularMarketDayRange'}).text.strip()
    week_52_range = soup.find('fin-streamer', {'data-field': 'fiftyTwoWeekRange'}).text.strip()
    market_cap = soup.find('fin-streamer', {'data-field': 'marketCap'}).text.strip()
    # Extract PE Ratio (TTM)
    pe_label = soup.find('span', class_='label', title='PE Ratio (TTM)')
    pe_value = pe_label.find_next_sibling('span').find('fin-streamer').text.strip()

    # Extract EPS (TTM)
    eps_label = soup.find('span', class_='label', title='EPS (TTM)')
    eps_value = eps_label.find_next_sibling('span').find('fin-streamer').text.strip()

    # Print the scraped details
    print("\n### Stock Price ###")
    print(f"Open Price: {open_price}")
    print(f"Previous Close: {previous_close}")
    print(f"Day's Range: {day_range}")
    print(f"52 Week Range: {week_52_range}")
    print("\n### Company Details ###")
    print(f"Market Cap: {market_cap}")
    print(f"PE Ratio (TTM): {pe_value}")
    print(f"EPS (TTM): {eps_value}")

except AttributeError as e:
    print("Error while scraping data. Some fields may not be found.")
    print(e)
