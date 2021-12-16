from datetime import time

from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.customLogger import LogGen
from utilities.browserUtilis import BrowserUtilities
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pageobjects.ReleasePage import ReleasePage
from msedge.selenium_tools import EdgeOptions, Edge
from pathlib import Path

root_path = str(Path(__file__).parent.parent)
file = "\\testdata\\upload_test_automation.a2l"
file_path = root_path + file
print(file_path)
# driver = Edge(executable_path='C:\\Users\\anavina\\PycharmProjects\\v7_test_automation\\utilities\\driver\\msedgedriver.exe')
# driver.get("https://smtcat0007prj.rd.corpintra.net/workcenter/")
#
# rp = ReleasePage(driver)
# lp = HomePage(driver)
# project = "V7 Release Administration"
# title = "V7"
# description = "v7 description"
# date = "12/08/2021"
# v8 = "ANAVINA"

# Test data setup
#
#driver.switch_to.frame("issuedetails-frame-iframe")
# driver.switch_to.frame("//*[@id='issuedetails-frame']")
#
#driver.find_element_by_id("F11160").send_keys("abcd")
# driver.find_element_by_xpath("//*[@id='F13445']").send_keys("12/08/2021")
#
# driver.find_element_by_id("F11160").send_keys("abc")
# driver.find_element_by_xpath("//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[2]").send_keys("ANAVINA")
# driver.find_element_by_xpath("//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[1]").click()
# driver.find_element_by_id("F12646_LEFT").is_selected()
# driver.find_element_by_xpath("//*[@id='F12646.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a").click()

# root_path = str(Path(__file__).parent.parent)
# excel_path = "\\TestData\\" + "testData_mirror.xlsx"
#
# print(root_path+excel_path)
#

#C:\Users\anavina\PycharmProjects\v7_test_automation\testdata\csvTestData.csv

#driver.find_element((By.XPATH, "//input[@class='frmTxa ControlStyle TxaCtrl']")).send_keys("12/08/2021")

#driver.find_element_by_id("F11160").send_keys("abcd")
# # rp.set_title(title)
# # rp.set_description(description)
# rp.set_release_date(date)
# rp.select_v8(v8)
# time.sleep(7)
#rp.click_ok()
# driver.find_element_by_id("a2luploadcomment").send_keys("comment")
# driver.find_element_by_xpath("//*[@id='52d5fc10-c876-4ba2-a7b6-1f44133dd5a9']/div[3]/input[2]").send_keys("C:\\Users\\anavina\\PycharmProjects\\v7_test_automation\\testdata\\upload_test_automation.a2l")
# print("-------------------Click on Upload A2L button-----------------------")
# print("-------------------Click on Upload A2L button-----------------------")
#



