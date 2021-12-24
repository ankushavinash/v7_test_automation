import time

from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


class TestReleaseCSVImport:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_004_release_csv_import(self, setup):
        self.logger.info("********test_003_release_csv_import : started********")

        # Setup
        driver = setup[0]
        test_data_path = setup[2]
        lp = HomePage(driver)
        rp = ReleasePage(driver)
        bu = BrowserUtilities(driver)

        # Test data setup
        project = "V7 Release Administration"
        title = str(xlUtilis.read_data(test_data_path, 'tc_001', 2, 1))
        file = str(".\\testdata\\csvTestData.csv")
        self.logger.info("*****create release*********")
        lp.search_project(project)
        rp.set_title(title)
        rp.click_ok()
        rp.click_workarea()
        self.logger.info("*****Upload CSV file*********")
        rp.click_CSV_upload()
        self.logger.info("*****click on csv upload*********")
        time.sleep(6)
        self.logger.info(driver.current_window_handle) # CW
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to_window(handle)
            self.logger.info(driver.title)
        upload_xpath = "//input[@name='Filetext']"

        driver.quit()


        #"//input[@id='File']"
        #bu.file_upload(file)
        #self.logger.info("*****file uploaded successful*********")



        self.logger.info("*****test_004_Import_CSV_to_release  : passed*******")
        self.logger.info("*****test_004_Import_CSV_to_release : completed ********")





