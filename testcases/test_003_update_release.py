from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
from flaky import flaky


@flaky(max_runs=3, min_passes=1)
class TestUpdateRelease:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_003_update_release(self, setup):
        self.logger.info("********test_003_update_release : started********")

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
        new_title = str(xlUtilis.read_data(test_data_path, 'tc_003', 2, 1))
        new_description = str(xlUtilis.read_data(test_data_path, 'tc_003', 2, 2))
        new_date = str(xlUtilis.read_data(test_data_path, 'tc_003', 2, 3))
        new_v8 = str(xlUtilis.read_data(test_data_path, 'tc_003', 2, 4))
        new_project_write_access = str(xlUtilis.read_data(test_data_path, 'tc_003', 2, 5))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 3, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")

        # Click on update button to update the Release information
        self.logger.info("****************update release**********************")
        # Click on update button to update the Release information
        rp.click_update()
        # Update the Release details
        rp.update_release(new_title, new_description, new_date, new_v8, new_project_write_access)
        #  Click ok to confirm update the release details
        rp.click_ok()
        # Validation for release update
        if bu.is_displayed((By.ID, 'itemID')):
            text = bu.get_text((By.ID, 'itemID'))
            self.logger.info("******Update release successful. Release ID : " + text + "*******")
            assert True, "Release Update successful. Release ID : " + text
        else:
            self.logger.info("******Update release unsuccessful*******")
            assert False, "Release Update unsuccessful. Task ID not displayed"

        self.logger.info("*****test_003_update_release  : passed*******")
        self.logger.info("*****test_003_update_release : completed ********")






