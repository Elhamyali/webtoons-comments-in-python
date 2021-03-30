#Step 1- import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
# from selenium_move_cursor.MouseActions import move_to_element_chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import js
# import json
# import numpy -mas np
import time
import pandas as pd         #to save CSV file
# from bs4 import BeautifulSoup
# import ctypes         #to create text popup

#Step 2- define browser for "webdriver" and add the “ — headless” argument
opts = Options()
opts.add_argument(' — headless')
driver = webdriver.Chrome('chromedriver', options=opts)

#Step 3- add the target URL and the code to open the URL with the "webdriver"
url = 'https://www.webtoons.com/en/challenge/tested/list?title_no=231173'
# driver.maximize_window() #maximize the window
driver.get(url)          #open the URL
driver.implicitly_wait(220) #maximum time to load the link

#Step 4- Find all the elements to scrape on the comic's homepage: subject, date, like, episode number
element = driver.find_element(By.ID,"_listUl")
list_items = element.find_elements_by_css_selector("*")

subject_span = list_items[0].find_element_by_class_name('subj')
print(subject_span.text)

date_span = list_items[0].find_element_by_class_name('date')
print(date_span.text)

love_span = list_items[0].find_element_by_class_name('like_area')
print(love_span.text[4:])

episodeNumber_span = list_items[0].find_element_by_class_name('tx')
print(episodeNumber_span.text)

#step 5- scroll down to load the whole episode page
list_items[0].click()
driver.implicitly_wait(220)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")

#step 6- Find all the elements to scrape on the episode, open all replies, and open all paginated comments
element = driver.find_element(By.ID,"cbox_module")
# list_items = element.find_elements_by_css_selector("*")

subjectEpisode_span = driver.find_element_by_class_name('subj_episode')
print(subjectEpisode_span.text)

commentCount_span = element.find_element_by_class_name('u_cbox_count')
print(commentCount_span.text)

commentList_span = element.find_elements_by_class_name('u_cbox_comment')

for comment in commentList_span:

    username_span = comment.find_element_by_class_name('u_cbox_nick')
    print(username_span.text)

    commentDescription_span = comment.find_element_by_class_name('u_cbox_contents')
    print(commentDescription_span.text)

    likes_span = comment.find_element_by_class_name('u_cbox_cnt_recomm')
    print(likes_span.text)

    dislikes_span = comment.find_element_by_class_name('u_cbox_cnt_unrecomm')
    print(dislikes_span.text)

    replyCount_span = comment.find_element_by_class_name('u_cbox_reply_cnt')
    print(replyCount_span.text)

    if replyCount_span.text and int(replyCount_span.text) > 0:
        comment_class = comment.get_attribute('class').split(" ")[1]
        # this CSS Selector will find all of the replies, once they're there
        replies_selector = f".{comment_class} > .u_cbox_reply_area > .u_cbox_list > .u_cbox_comment"

        # this clicks on the reply button - for some reason calling .click on
        # replyCount_span directly doesn't work, probably ajax related.
        driver.execute_script("arguments[0].click();", replyCount_span)

        # wait until the comment has been re-added to the DOM with its replies
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, replies_selector))
        )

        replies = driver.find_elements(By.CSS_SELECTOR, replies_selector)

        for reply in replies:

            username_span = reply.find_element_by_class_name('u_cbox_nick')
            print(username_span.text)

            commentDescription_span = reply.find_element_by_class_name('u_cbox_contents')
            print(commentDescription_span.text)

            likes_span = reply.find_element_by_class_name('u_cbox_cnt_recomm')
            print(likes_span.text)

            dislikes_span = reply.find_element_by_class_name('u_cbox_cnt_unrecomm')
            print(dislikes_span.text)

# Step 7- Go back to the homepage
driver.back()

# Step 8- Repeat steps 4-7 and scrape the same data elements


# # Step 9- Save the results as a CSV file
# #save to dataframe
# df = pd.DataFrame({'Subject':subj, 'Date':date})

# #export as csv file
# df.to_csv('webtoons_tested_comments.csv')