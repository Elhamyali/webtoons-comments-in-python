from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.support.expected_conditions as EC


options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 10)
url = "https://www.webtoons.com/en/challenge/tested/list?title_no=231173"
# url = "https://www.webtoons.com/en/drama/pyramid-game/list?title_no=2277"
# driver.maximize_window()

driver.get(url)

driver.implicitly_wait(10)


def get_episodes():
    return driver.find_element_by_id("_listUl").find_elements_by_tag_name("li")

try:
    while True:
        # scrape episode
        wait.until(EC.visibility_of_element_located((By.ID, "_listUl")))
        list_items = get_episodes()
        for i in range(len(list_items)):
            episodes = get_episodes()
            title = episodes[i].find_element_by_class_name("subj")
            print("title: ", title.text)
            date = episodes[i].find_element_by_class_name("date")
            print("date: ", date.text)
            loves = episodes[i].find_element_by_class_name("like_area")
            print("loves: ", loves.text[4:])
            episode_number = episodes[i].find_element_by_class_name("tx")
            print("episode number: ", episode_number.text)

            episodes[i].click()
            wait.until(EC.staleness_of(list_items[0]))

            # scrape comments
            try:
                while True:
                    comments = driver.find_element_by_id("cbox_module").find_elements_by_class_name("u_cbox_comment")
                    for comment in comments:
                        username = comment.find_element_by_class_name("u_cbox_nick")
                        print(username.text)
                        description = comment.find_element_by_class_name("u_cbox_contents")
                        print(description.text)
                        likes = comment.find_element_by_class_name("u_cbox_cnt_recomm")
                        print(likes.text)
                        dislikes = comment.find_element_by_class_name("u_cbox_cnt_unrecomm")
                        print(dislikes.text)
                        reply_count = comment.find_element_by_class_name("u_cbox_reply_cnt")
                        print(reply_count.text)

                        if reply_count.text and int(reply_count.text) > 0:
                            replies_button = comment.find_element_by_css_selector("a.u_cbox_btn_reply")
                            driver.execute_script("arguments[0].click();", replies_button)
                            comment_class = comment.get_attribute('class').split(" ")[1]
                            replies_selector = f".{comment_class} > .u_cbox_reply_area > .u_cbox_list > .u_cbox_comment"
                            replies = driver.find_elements_by_css_selector(replies_selector)

                            for reply in replies:
                                username = reply.find_element_by_class_name("u_cbox_nick")
                                print(username.text)
                                reply_description = reply.find_element_by_class_name("u_cbox_contents")
                                print(reply_description.text)
                                likes = reply.find_element_by_class_name("u_cbox_cnt_recomm")
                                print(likes.text)
                                dislikes = reply.find_element_by_class_name("u_cbox_cnt_unrecomm")
                                print(dislikes.text)

                    while True:
                        pages = driver.find_element_by_class_name("u_cbox_paginate").find_elements_by_css_selector("span.u_cbox_num_page")
                        for j in range(len(pages)):
                            if pages[j].find_element_by_xpath("..").tag_name == "strong":
                                if int(pages[j].text) % 10 == 0:
                                    next_page_button = driver.find_element_by_class_name("u_cbox_next")
                                    next_page_button.click()
                                else:
                                    pages[j + 1].click()
                                break
            except:
                driver.back()

        pages = driver.find_element_by_class_name("paginate").find_elements_by_tag_name("span")
        for i in range(len(pages)):
            if pages[i].get_attribute("class") == "on":
                if int(pages[i].text) % 10 == 0:
                    next_page_button = driver.find_element_by_class_name("pg_next")
                    next_page_button.click()
                else:
                    pages[i + 1].click()
                break
except:
    print("EXECUTION COMPLETE")





# # # Step 9- Save the results as a CSV file
# # #save to dataframe
# # df = pd.DataFrame({'Subject':subj, 'Date':date})
#
# # #export as csv file
# # df.to_csv('webtoons_tested_comments.csv')
