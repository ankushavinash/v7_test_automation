import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen

# ---------------------------------------------------------------------------------- #
# Precondition: test_002 must be executed before test_015                        #
# Note: Release must be created before searching of created release              #
from testcases.support import TestCreateRelease
# Above line will create release
# ---------------------------------------------------------------------------------- #


@pytest.mark.regression
@flaky(max_runs=3, min_passes=1)
class TestSearchForCreatedRelease:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_015_search_for_created_release(self, setup):
        self.logger.info("********test_015_search_for_created_release : started********")

        # Setup
        driver = setup[0]
        test_data_path = setup[2]
        hp = HomePage(driver)
        bu = BrowserUtilities(driver)

        # Test data setup
        release_id = str(xlUtilis.read_data(test_data_path, 'release_id', 2, 2))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)

        # click on search for items and reports
        hp.click_search_for_item_and_reports()
        # click on search type
        hp.select_search_type("ID")
        # Enter ID to search field
        hp.set_search_type(release_id)
        # click search submit
        hp.click_search_submit()

        # validation
        if bu.is_displayed((By.CLASS_NAME, "highlighter")):
            text = bu.get_text((By.CLASS_NAME, "highlighter"))
            self.logger.info("********Search for release successful. Displayed Release ID : " + text + "**************")
            assert True, "Search for release successful. Displayed Release ID : " + text
        else:
            self.logger.info("*********Search for release unsuccessful***********")
            assert False, "Search for release unsuccessful. Release ID not displayed"

        self.logger.info("********test_015_search_for_created_release : passed*******")
        self.logger.info("*********test_015_search_for_created_release : completed ********")




