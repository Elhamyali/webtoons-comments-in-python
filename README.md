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
6. Find all the elements to scrape on the comic's episode, open all replies, and open all paginated comments pages
7. Go back to the homepage and click on previous episodes
8. Repeat steps 4-7 and scrape the same data elements
9. Save the results as a CSV file

## Final Output
A CSV file with the following data elements:
* 'Subject': subj
* 'Date': date
* 'Love': like_area
* 'Episode number': tx
* 'Subject Episode': subj_episode
* 'Comment Count': u_cbox_count (both primary comments and replies)
* 'Comment List': u_cbox_comment
* 'Username': u_cbox_nick
* 'Likes': u_cbox_cnt_recomm
* 'Dislikes': u_cbox_cnt_unrecomm
* 'Reply Count': u_cbox_reply_cnt
* 'Reply List': u_cbox_reply_area

## Assumptions
We checked robots.txt file of the URL: https://www.webtoons.com/en/challenge/tested/list?title_no=231173&page=1 and learned that we are allowed to scrape comic data.

## Resources
Interested in scraping Webtoons comments in R? Visit https://github.com/bryce-wong/webtoon_comments_in_R.
