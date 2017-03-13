# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome()
# driver.get("http://www.x-tl.com")
# print driver.title
# driver.quit()

# browser = webdriver.Firefox() # Get local session of firefox
# browser.get("http://www.x-tl.com") # Load page
# assert "Yahoo!" in browser.title
# elem = browser.find_element_by_name("p") # Find the query box
# elem.send_keys("seleniumhq" + Keys.RETURN)
# time.sleep(0.2) # Let the page load, will be added to the API
# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
# except NoSuchElementException:
#     assert 0, "can't find seleniumhq"
# # browser.close()
# from splinter import Browser
# import time
#
# b = Browser(driver_name="chrome")
# b.visit("http://www.sina.com.cn")