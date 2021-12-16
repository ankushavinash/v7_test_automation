import time

from flaky import flaky
from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.customLogger import LogGen
from utilities.browserUtilis import BrowserUtilities


#@flaky()
class TestCreateRelease:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_002_create_release(self, setup):
        self.logger.info("********test_001_create_release : started********")

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

        self.logger.info("*****create release*********")

        hp.search_project(project)
        rp.fill_all_information(title, description, date, v8, project_write_access)

        #####################Step by Step################################
        # rp.set_title(title)
        # rp.set_description(description)
        # rp.set_release_date(date)
        # rp.select_v8(v8)
        # rp.select_project_write_access(project_write_access)
        #################################################################

        rp.click_ok()

        if bu.is_displayed((By.ID, 'itemID')):
            text = bu.get_text((By.ID, 'itemID'))
            self.logger.info("******create release successful. Release ID : " + text + "*******")
            assert True, "Release creation successful. Release ID : " + text
        else:
            self.logger.info("******create release unsuccessful*******")
            assert False, "Release creation unsuccessful. Task ID not displayed"

        self.logger.info("*****test_002_create_release  : passed*******")
        self.logger.info("*****test_002_create_release : completed ********")





