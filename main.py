from selenium import webdriver

chrome_driver = "C:\\********************"
driver = webdriver.Chrome(executable_path=chrome_driver)  # opens a web driver for Chrome

# driver.get("https://amazon.com")  # gets the web driver to open a web page
# driver.get("https://www.amazon.ca/Instant-Pot-Plus-Programmable-Pressure/dp/B075CYMYK6/ref=sr_1_1?dchild=1&keywords"
#            "=Instant+Pot+Ultra+60+Ultra+6+Qt+10-in-1+Multi-+Use+Programmable+Pressure+Cooker%2C+Slow+Cooker%2C+Rice"
#            "+Cooker%2C+Yogurt+Maker%2C+Cake+Maker%2C+Egg+Cooker%2C+Saut%C3%A9%2C+and+more%2C+Stainless+Steel%2FBlack"
#            "&qid=1617909614&sr=8-1")

# driver.close()  # closes a single tab

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q)
# print(search_bar.get_attribute("placeholder))

driver.get("https://www.python.org/")

events_dates = driver.find_elements_by_css_selector(".event-widget time")
events_titles = driver.find_elements_by_css_selector(".event-widget li a")
events_dict = {}


for event in events_dates:
    print(event.text)

for event_title in events_titles:
    print(event_title.text)

for i in range(0, 5):
    events_dict[i] = {'time': events_dates[i].text, 'name': events_titles[i].text}

print(events_dict)



driver.quit()  # closes the entire browser
