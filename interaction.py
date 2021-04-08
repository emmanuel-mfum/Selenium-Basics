from selenium import webdriver
from selenium.webdriver.common.keys import Keys # necessary to import, if we want to send keys other than letters

chrome_driver = "C:\\*************************"
driver = webdriver.Chrome(executable_path=chrome_driver)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number_articles = driver.find_element_by_css_selector("#articlecount a")
# number_articles.click()  # will click on the link of the number of articles on the main page of Wikipedia

# all_portals = driver.find_element_by_link_text("All portals")  # find link by the text as it appears on the page
# all_portals.click()


# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Python")  # write stuff in the search bar on Wikipedia
# search_bar.send_keys(Keys.ENTER)  # presses the enter key aka return key

# print(number_articles.text)

driver.get("https://thawing-citadel-75545.herokuapp.com/")  # gets a website

first_name_input = driver.find_element_by_name("fName")  # find element with such name attribute
first_name_input.send_keys("Emmanuel")   # types inside that field the string specified
last_name_input = driver.find_element_by_name("lName")
last_name_input.send_keys("M")
email_input = driver.find_element_by_name("email")
email_input.send_keys("abc@gmail.com")
submit = driver.find_element_by_css_selector("form button")  # find and select the button on the page
submit.send_keys(Keys.ENTER)  # press enter



