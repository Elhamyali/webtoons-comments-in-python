# Scraping Tested Comic Episodes on Webtoons using Python and Selenium

## Summary
This is a step-by-step guide to scrape Tested episodes with the following data elements in a csv file:
* episode name
* total # of loves per episode
* total # of comments per episode
* usernames
* comments descriptions
* replies descriptions
* likes per comment
* dislikes per comment

## Required Tools
* Python 3.4 or greater: https://www.python.org/downloads/
* Selenium 3.14 or greater, a Python library: https://pypi.org/project/selenium/
* ChromeDriver WebDriver for Chrome: download here https://chromedriver.chromium.org/downloads
* An interactive editor (IDE) like Microsoft Visual Code: https://code.visualstudio.com/download

## Steps
1. Import required libraries
2. Define browser for "webdriver" and add the " - headless" argument
3. Add the target URL and the code to open the URL with the "webdriver"
4. Find all the elements to scrape on the comic's homepage
5. Scroll down to load the whole page
6. Find all the elements to scrape on the comic's episode
7. Open all replies 
8. If available, click on next button for comments (pagination)
9. Scrape comments and click previous page button
10. Save the results as a CSV file: save to data frame and export as CSV file 
