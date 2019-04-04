from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="C:/Users/LAL KRISHNA/PycharmProjects/AutomationTraining03Apr2019/drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_id("email").send_keys("my_username")
driver.find_element_by_id("pass").send_keys("my_password")
driver.find_element_by_id("loginbutton").click()                    # Working
