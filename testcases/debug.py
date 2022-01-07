import time
from webbrowser import Chrome

from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.customLogger import LogGen
from utilities.browserUtilis import BrowserUtilities
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pageobjects.ReleasePage import ReleasePage
from utilities.browserUtilis import BrowserUtilities
from msedge.selenium_tools import EdgeOptions, Edge
from selenium import webdriver
from pathlib import Path


# root_path = str(Path(__file__).parent.parent)
# file = "\\testdata\\upload_test_automation.a2l"
# file_path = root_path + file
# print(file_path)
#driver = Edge(executable_path='C:\\Users\\anavina\\PycharmProjects\\v7_test_automation\\utilities\\driver\\msedgedriver.exe')
driver = webdriver.Chrome(executable_path='C:\\Users\\anavina\\PycharmProjects\\v7_test_automation\\utilities\\driver\\chromedriver.exe')
driver.get("https://smtcat0007prj.rd.corpintra.net/workcenter/")
# rp = ReleasePage(driver)
# hp = HomePage(driver)
# bu = BrowserUtilities(driver)
# #bu.login_application("anavina", "Password@12345")
# #hp.search_project("V7 Release Administration")
# # rp.set_title("test")
driver.switch_to.frame("issuedetails-frame")
driver.find_element_by_xpath("//*[@id='F13445']").send_keys("12/08/2021")
driver.find_element_by_id("F11160").send_keys("abc")


#rp.click_CSV_upload()
driver.find_element_by_xpath("//Button[text()='Upload & Attach AKV (.csv file)']").click()
parent_widnow = driver.current_window_handle
# print("Parent window name is : ", parent_widnow)
# print("Main window title : ", driver.title)
# rp.click_CSV_upload()
# print("*****click on csv upload*********")
# time.sleep(6)

child_windows = driver.window_handles
print("Print all window : ", type(child_windows))

for child in child_windows:
    print(child)
    if parent_widnow != child:
        driver.switch_to.window(child)
        driver.set_page_load_timeout(3)
        print("page loaded successfully")
        # driver.execute_script("window.stop();")
        # driver.maximize_window()
        time.sleep(3)
    else:
        print("Window not found")
        assert "Window not found"

# driver.find_element_by_xpath("//*[@id='Title']").is_displayed():
# driver.execute_script("window.stop();")
# driver.find_element_by_xpath("//*[@id='Title']").send_keys("Automation Upload test")
driver.switch_to.frame("utiltop")
#driver.switch_to.frame(driver.find_element_by_xpath(By.XPATH, "/html/frameset/frame[1]"))
print("title is: ", driver.title)

driver.find_element_by_xpath("//*[@id='Title']").send_keys("Automation Upload test")
print("end1")
print("end2")

# parent_widnow = driver.current_window_handle
# print("Parent window name is : ", parent_widnow)
# print("Main window title : ", driver.title)
# rp.click_CSV_upload()
# print("*****click on csv upload*********")
# time.sleep(6)
#
# child_windows = driver.window_handles
# print("Print all window : ", type(child_windows))
#
# for child in child_windows:
#     print(child)
#     if parent_widnow != child:
#         driver.switch_to.window(child)
#


#
# driver.find_element_by_xpath("//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[2]").send_keys("ANAVINA")
# driver.find_element_by_xpath("//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[1]").click()
# driver.find_element_by_id("F12646_LEFT").is_selected()
# driver.find_element_by_xpath("//*[@id='F12646.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a").click()

#C:\Users\anavina\PycharmProjects\v7_test_automation\testdata\csvTestData.csv

#driver.find_element((By.XPATH, "//input[@class='frmTxa ControlStyle TxaCtrl']")).send_keys("12/08/2021")

#driver.find_element_by_id("F11160").send_keys("abcd")
# # rp.set_title(title)
# # rp.set_description(description)
# rp.set_release_date(date)
# rp.select_v8(v8)
# time.sleep(7)
#
# driver.find_element_by_id("a2luploadcomment").send_keys("comment")
# driver.find_element_by_xpath("//*[@id='52d5fc10-c876-4ba2-a7b6-1f44133dd5a9']/div[3]/input[2]").send_keys("C:\\Users\\anavina\\PycharmProjects\\v7_test_automation\\testdata\\upload_test_automation.a2l")
# print("-------------------Click on Upload A2L button-----------------------")
# print("-------------------Click on Upload A2L button-----------------------")
#



