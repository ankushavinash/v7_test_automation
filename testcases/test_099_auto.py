import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.customLogger import LogGen
from utilities.browserUtilis import BrowserUtilities
from utilities.xlUtilis import *
from flaky import flaky
from selenium.webdriver.support import expected_conditions as EC


class TestCreateRelease:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_099_create_release(self, setup):
        self.logger.info("********test_002_create_release : started********")

        # Setup
        driver = setup[0]
        test_data_path = setup[2]
        hp = HomePage(driver)
        rp = ReleasePage(driver)
        bu = BrowserUtilities(driver)

        # Test data setup
        project = "V7 Release Administration"
        title = str(xlUtilis.read_data(test_data_path, 'Basic_Information_Release', 2, 1))
        description = str(xlUtilis.read_data(test_data_path, 'Basic_Information_Release', 2, 2))
        date = str(xlUtilis.read_data(test_data_path, 'Basic_Information_Release', 2, 3))
        v8 = str(xlUtilis.read_data(test_data_path, 'Basic_Information_Release', 2, 4))
        project_write_access = str(xlUtilis.read_data(test_data_path, 'Basic_Information_Release', 2, 5))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)

        self.logger.info("*****create release*********")

        # Search for project
        hp.search_project(project)
        # Fill all the details to create Release
        rp.fill_all_information(title, description, date, v8, project_write_access)
        # Click on OK to create Release
        rp.click_ok()

        release_id = driver.find_element_by_id("issue_id").get_attribute("value")
        xlUtilis.write_data(test_data_path, 'release_id', 2, 1, release_id)


        # hp.click_search_for_item_and_reports()
        # hp.select_search_type("ID")
        # hp.set_search_type(text)
        #hp.click_search_submit()

        # if bu.is_displayed((By.ID, 'itemID')):
        #     text = bu.get_text((By.ID, 'itemID'))
        #     self.logger.info("******create release successful. Release ID : " + text + "*******")
        #     assert True, "Release creation successful. Release ID : " + text
        # else:
        #     self.logger.info("******create release unsuccessful*******")
        #     assert False, "Release creation unsuccessful. Task ID not displayed"

        self.logger.info("*****test_002_create_release  : passed*******")
        self.logger.info("*****test_002_create_release : completed ********")






