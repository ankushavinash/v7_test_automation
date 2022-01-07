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

    def __init__(self, driver):
        self.driver = driver
        self.bu = BrowserUtilities(driver)

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
            self.bu.click((By.XPATH, self.link_v4application_xpath))
        else:
            assert False, "Invalid argument" + application_name



