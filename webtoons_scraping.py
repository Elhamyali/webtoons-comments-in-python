#step-by-step guide to scrape a dynamic website with Selenium from
#code source: https://medium.com/swlh/scraping-a-dynamic-web-page-its-selenium-da161999c975

############Step 0- check the if the URL you are trying to scrape allows you to do so from the robots.txt file############
# https://www.doordash.com/robots.txt (based on this output, it seems we can scrape data from this website)

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
# import js
# import json
# import numpy as np
import time
# import pandas as pd         #to save CSV file
from bs4 import BeautifulSoup
# import ctypes         #to create text popup

#Step 2- define browser for "webdriver" and add the “ — headless” argument
opts = Options()
opts.add_argument(' — headless')
driver = webdriver.Chrome('chromedriver', options=opts)

#Step 3- add the target URL and the code to open the URL with the "webdriver"

url = 'https://www.webtoons.com/en/challenge/tested/list?title_no=231173'
driver.maximize_window() #maximize the window
driver.get(url)          #open the URL
driver.implicitly_wait(220) #maximum time to load the link

# Find all the elements to scrape on the comic's homepage: subject, date, like, episode number
element = driver.find_element(By.ID,"_listUl")
list_items = element.find_elements_by_css_selector("*")

subject_span = list_items[0].find_element_by_class_name('subj')
print(subject_span.text)

date_span = list_items[0].find_element_by_class_name('date')
print(date_span.text)

like_span = list_items[0].find_element_by_class_name('like_area')
print(like_span.text[4:])

episodeNumber_span = list_items[0].find_element_by_class_name('tx')
print(episodeNumber_span.text)

#step 4- scroll down to load the whole page
list_items[0].click()
driver.implicitly_wait(220)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")

#step 5- Find all the elements to scrape on the comic's episode: username, comments, replies, likes, dislikes
element = driver.find_element(By.ID,"_listUl")
list_items = element.find_elements_by_css_selector("*")

commentCount_span = list_items[0].find_element_by_class_name('u_cbox_count')
print(commentCount_span.text)

username_span = list_items[0].find_element_by_class_name('u_cbox_nick')
print(username_span.text)

likes_span = list_items[0].find_element_by_class_name('u_cbox_cnt_recomm')
print(likes_span.text)

dislikes_span = list_items[0].find_element_by_class_name('u_cbox_cnt_unrecomm')
print(dislikes_span.text)

commentText_span = list_items[0].find_element_by_class_name('u_cbox_contents')
print(commentText_span.text)

# Extract all replies
# Click on all

# Step 6- Ask driver to click on back button to parse for all past episode
driver.back()
driver.execute_script("window.history.go(-1)")

# Step 7- Scrape elements listed in Step 5



# Step 6- load the page and range of pages############
# #define the lists
# names = []
# prices = []
#
# #extract the number of pages for the searched product
# driver.implicitly_wait(120)
# time.sleep(3)
# result = driver.page_source
# soup = BeautifulSoup(result, 'html.parser')
# page = list(soup.findAll('div', class_="sc-cvbbAY htjLED"))
# start = int(page[2].text)
# print('1st page:',start)
# last = int(page[-2].text)
# final = last +1
# print('last page:',final)
#
# #getting numbers out of string of pages
# print(f'first page:{start}, and last page with + 1: {final}')
#
# ############step 7- click on each store
# #set the page_range And
# #lloop all the pages of store
# for i in range(start, final, 1):
#  time.sleep(7)
#  #find the number of stores per page
#  list_length = len(driver.find_elements_by_xpath(“//div[@class=’StoreCard_root___1p3uN’]”))
#  products_per_page = list_length+1
#  #loop through the menues of each store on a page
#  for x in range(0, list_length, 1):
#  time.sleep(7)
#  driver.execute_script(“window.scrollTo({top:75, behavior:’smooth’,})”)
#  store_name = driver.find_elements_by_xpath(‘//div[@class=”StoreCard_storeDetail___3C0TX”]’)
#  strnm = store_name[x]
#  print(f’{x}- ‘, strnm.text)
#  time.sleep(4)
#  element=driver.find_elements_by_xpath(“//div[@class=’StoreCard_storeDetail___3C0TX’]”)
#  click = element[x]
#  move_to_element_chrome(driver, click, display_scaling=100)
#  time.sleep(7)
#  click.click()
#  driver.implicitly_wait(360)
#
# ############step 8- scrape menus and return to the page of stores after scraping
# time.sleep(20)
#  result = driver.page_source
#  time.sleep(11)
#  soup = BeautifulSoup(result, ‘html.parser’)
#  div = soup.find(‘div’, class_=”sc-jwJjzT kjdEnq”)
#  if div is not None:
#  time.sleep(25)
#  for i in div.findAll(‘div’, class_=”sc-htpNat Ieerz”):
#  pros = i.find(‘div’, class_=”sc-jEdsij hukZqW”)
#  print(‘writing (‘, pros.text, ‘) to disk’)
#  names.append(pros.text)
#  rates = i.find(‘span’, class_=”sc-bdVaJa eEdxFA”)
#  #if there is no price for the food, append ‘N/A’ in the list of ‘prices’
#  if rates is not None:
#  print(‘price: ‘, rates.text)
#  rate = rates.text
#  else:
#  print(‘N/A’)
#  rate = ‘N/A’
#  prices.append(rate)
#  driver.back()
#
# ############step 9- check the number of menus in the list of names
# length = len(names)
#
# ############step 10- break the loop on completion of about 10000 menus in the list and inform us with a popup, otherwise repeat the loop
# #if menu record reaches the target, exit the script and produce target completion message box
#  if ((length > 10000) and (length <10050)):
#  ctypes.windll.user32.MessageBoxW(0, f”Congratulations! We have succefully scraped {length} menues.”, “Project Completion”, 1)
#  break
#  else:
#  driver.back()
#  continue
#
# ############step 11- the whole process will be kept in a loop until we get about 10000 menus. If 10000 target is not reached on scraping all the stores on one page, click in the “next” button to scrape
#  #after scraping each store on a page, it will tell that it is going to next page
#  print(f’Now moving to page number {i}’)
#
#  #click next page button
#  driver.find_elements_by_xpath(‘//div[@class=”sc-gGBfsJ jFaVNA”]’)[1].click()
#
# ############step 12- save the results as a CSV file
# #save to dataframe
# df = pd.DataFrame({‘Name’:names, ‘Price’:prices})
#
# #export as csv file
# df.to_csv(‘doordash_menues.csv’)
