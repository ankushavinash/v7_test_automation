import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
# ---------------------------------------------------------------------------------- #
#   Precondition: test_016 must be executed before test_020                          #
#   Note: Release must be created and confirmed by V4 before V8 rejection            #
from testcases.support import TestConfirmationReleaseAsV4User
#   Above line will help in create and confirm release as v4 user                    #
# ---------------------------------------------------------------------------------- #


class TestV8UserRejectionOfV4ConfirmedRelease:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_020_v8_user_rejection_of_v4_confirmed_release(self, setup):
        self.logger.info("*******test_020_v8_user_rejection_of_v4_confirmed_release : started*******")

        # Setup
        driver = setup[0]
        test_data_path = setup[2]
        hp = HomePage(driver)
        rp = ReleasePage(driver)
        bu = BrowserUtilities(driver)

        # Test data setup
        v4_approved_release_id = str(xlUtilis.read_data(test_data_path, 'release_id', 3, 2))
        release_letter_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 1))
        internal_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 2))
        v8_user = str(xlUtilis.read_data(test_data_path, 'Login', 7, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 7, 3))
        bu.login_application(v8_user, password)

        # search for V4 approved release
        hp.search_and_open_the_release_from_all_items(v4_approved_release_id)

        # reject release as V8 user override pending confirmation
        rp.reject_release_as_v8_user(internal_comment, release_letter_comment)

        # validation
        driver.switch_to.frame("schFrame")
        if bu.is_displayed((By.XPATH, "//*[@id='schdata']//td[12]//tbody/tr[2]//b")):
            text = bu.get_text((By.XPATH, "//*[@id='schdata']//td[12]//tbody/tr[2]//b"))
            self.logger.info("*******V8 user rejection successful. Status : " + text + "**********")
            assert True, "V8 user rejection successful. Status : " + text
        else:
            self.logger.info("*******V8 user rejection of release unsuccessful*********")
            assert False, "V8 user rejection of release unsuccessful. Release is not confirmed"

        self.logger.info("******test_020_v8_user_rejection_of_v4_confirmed_release : passed******")
        self.logger.info("******test_020_v8_user_rejection_of_v4_confirmed_release : completed ******")




