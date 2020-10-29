# RTX 3070 Best Buy Bot

## Features
- Refreshes link until "Add to Cart" button is available
- Automate entire checkout process

## Prerequisites
- Sign up for a Best Buy account
- Add all billing/shipping info to your account (must only have one card on the account)

## Dependencies
- Selenium
	- `pip install selenium`
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
	- Extract the compressed chromedriver executable to a driectory of your choice (be sure to update the path in bot.py accordingly)
		- For the Windows machine I developed this on, I chose `C:\Program Files (x86)\ChromeDriver\chromedriver.exe`

## Running the Bot
1. Make sure you have [Python 3.9](https://www.python.org/downloads/release/python-390/)
2. Edit the info.py file with your Best Buy account email and password and cvv for the card on the account
3. Navigate to your project directory and run the bot.py script from your preferred environment
4. Feel free to change the Best Buy links in the bot.py file to any item on bestbuy.com
	- **NOTE:** From testing it appears that it depends on the price of the item wheter or not the cvv number is asked for. If you plan to use this bot for something cheaper you may need to remove/comment the segment of code detecting and filling in the cvv field.


