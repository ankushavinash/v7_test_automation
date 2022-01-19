import pytest
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
from flaky import flaky


@pytest.mark.smoke
@pytest.mark.regression
@flaky(max_runs=3, min_passes=1)
class TestDiscardReleaseInPreparationState:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_004_discard_release_in_preparation_state(self, setup):
        self.logger.info("********test_004_discard_release_in_preparation_state : started********")

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
        release_letter_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 1))
        internal_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 2))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")

        # click on Discard Button
        rp.click_discard()
        # Enter release letter comment
        rp.set_release_letter_comment(release_letter_comment)
        # Enter internal comment
        rp.set_internal_comment(internal_comment)
        # click on ok
        rp.click_ok()

        # Discard validation
        driver.switch_to_frame("schFrame")
        if bu.is_displayed((By.XPATH, "//*[@id='schdata']/tbody/tr/td[8]/table//tr[2]/td/b")):
            text = bu.get_text((By.XPATH, "//*[@id='schdata']/tbody/tr/td[8]/table//tr[2]/td/b"))
            self.logger.info("**********Discard release successful. Status : " + text + "**************")
            assert True, "Discard release successful. Status : " + text
        else:
            self.logger.info("*********Discard release unsuccessful***********")
            assert False, "Discard release unsuccessful. Inactive not displayed"

        self.logger.info("*****test_004_discard_release_in_preparation_state  : passed*******")
        self.logger.info("*****test_004_discard_release_in_preparation_state : completed ********")
