from selenium.webdriver.common.by import By

from utilities.browserUtilis import BrowserUtilities


class V7LandingPage:
    # ---------------------------locator identifier----------------------------

    link_reports_xpath = "//div[text()='Reports']"

    def __init__(self, driver):
        self.driver = driver
        self.bu = BrowserUtilities(driver)

    # author : ankush
    # since : 2021-12-10
    # this method is click on reports link
    # argument :
    # return :
    def click_reports(self):
        self.bu.click((By.XPATH, self.link_reports_xpath))

