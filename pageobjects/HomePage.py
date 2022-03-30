import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.ReleasePage import ReleasePage
from utilities.browserUtilis import BrowserUtilities
from selenium.webdriver.common.by import By


class HomePage:
    # ---------------------------locator identifier----------------------------

    tag_new_id = "newRequestText"
    text_search_xpath = "//*[@class='field form-control']"
    link_v7_task_id = "node-SBM_PROJECT-project_465-link"
    dropdown_applicationGroup_class = "caretCustom"
    textbox_search_xpath = "//input[@class='search-query form-control']"
    link_v4application_xpath = "//span[@class='text s_string']"
    dropdown_look_in_xpath = "//*[@id='j_lookInSelect']"

    button_ok_id = "formbtns_ok"
    button_search_id = "search-icon-btn"
    button_search_type_id = "searchTypeLink"
    text_search_type_id = "prependedDropdownButton"
    button_search_submit_id = "btnSearchSubmit"

    def __init__(self, driver):
        self.driver = driver
        self.bu = BrowserUtilities(driver)
        self.rp = ReleasePage(driver)

    # author : ankush
    # since : 2021-12-02
    # this method is to click +New
    # argument :
    # return :
    def click_new(self):
        self.bu.click((By.ID, self.tag_new_id))

    # author : venugopal
    # since : 2021-08-09
    # this method is to click browse
    # argument :
    # return :
    def click_browse(self):
        self.bu.click((By.LINK_TEXT, "Browse"))

    # author : venugopal
    # since : 2021-08-09
    # this method is set Search
    # argument : search
    # return :
    def set_search(self, search):
        self.bu.send_keys((By.XPATH, self.text_search_xpath), search)

    # author : ankush
    # since : 2021-08-8
    # this method is  Search Project
    # argument : search
    # return :
    def search_project(self, project_name):
        self.click_new()
        self.click_browse()
        self.bu.select(By.XPATH, self.dropdown_look_in_xpath, "All Projects")
        self.set_search(project_name)
        WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.ID, self.link_v7_task_id))))
        if project_name == "V7 Release Administration":
            self.bu.click((By.ID, self.link_v7_task_id))
        self.driver.switch_to.frame("issuedetails-frame-iframe")

    # author : ankush
    # since : 2021-12-07
    # this method is to click Application group drop down button
    # argument :
    # return :
    def search_application(self, application_name):
        self.bu.click((By.CLASS_NAME, self.dropdown_applicationGroup_class))
        self.bu.send_keys((By.XPATH, self.textbox_search_xpath), application_name)
        if application_name == "V4..V8 Admin":
            WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.link_v4application_xpath))))
            self.bu.click((By.XPATH, self.link_v4application_xpath))
        else:
            assert False, "Invalid argument" + application_name

    # author : ankush
    # since : 2022-01-17
    # this method is click Search
    # argument : search
    # return :
    def click_search_for_item_and_reports(self):
        self.bu.click((By.ID, self.button_search_id))

    # author : ankush
    # since : 2022-01-18
    # this method is select search type
    # argument : search_type
    # return :
    def select_search_type(self, search_type):
        self.bu.click((By.ID, self.button_search_type_id))
        if search_type == "Keyword":
            self.bu.click((By.LINK_TEXT, "Keyword"))
        elif search_type == "ID":
            self.bu.click((By.LINK_TEXT, "ID"))
        elif search_type == "Regex":
            self.bu.click((By.LINK_TEXT, "Regex"))
        else:
            assert False, "Invalid argument"+search_type

    # author : ankush
    # since : 2022-01-19
    # this method is set Search
    # argument : search
    # return :
    def set_search_type(self, search_parameter):
        self.bu.send_keys((By.ID, self.text_search_type_id), search_parameter)

    # author : ankush
    # since : 2022-01-19
    # this method is click Search Submit
    # argument :
    # return :
    def click_search_submit(self):
        self.bu.click((By.ID, self.button_search_submit_id))

    # author : ankush
    # since : 2022-01-19
    # this method is to search and open the task from all items
    # argument : item_id
    # return :
    def search_and_open_the_release_from_all_items(self, item_id):
        self.click_search_for_item_and_reports()
        self.select_search_type("ID")
        self.set_search_type(item_id)
        self.click_search_submit()
        WebDriverWait(self.driver, 60).until((EC.visibility_of_element_located((By.LINK_TEXT, item_id))))
        self.bu.click((By.LINK_TEXT, item_id))

    # author : ankush
    # since : 2022-01-27
    # this method is to logout and again login as v8 user
    # argument : release_id
    # return :
    def login_again_and_search_release(self, username, password, release_id):
        time.sleep(5)
        self.rp.click_close_icon()
        self.bu.logout_application()
        self.bu.login_application(username, password)
        time.sleep(5)
        self.search_application("V4..V8 Admin")
        self.search_and_open_the_release_from_all_items(release_id)
        if self.bu.is_displayed((By.CLASS_NAME, "highlighter")):
            text = self.bu.get_text((By.CLASS_NAME, "highlighter"))
            return text
        else:
            assert False, "confirmed release displayed. unsuccessful"

