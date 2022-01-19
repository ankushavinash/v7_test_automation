import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


class TestV8UserConfirmationOfV4ConfirmedRelease:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_018_v8_user_confirmation_of_v4_confirmed_release(self, setup):
        self.logger.info("********test_018_v8_user_confirmation_of_v4_confirmed_release : started********")

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
        care_group = str(xlUtilis.read_data(test_data_path, 'tc_008', 2, 1))
        care_akv_variant = str(xlUtilis.read_data(test_data_path, 'tc_008', 2, 2))
        a2l_file_name = str(xlUtilis.read_data(test_data_path, 'tc_011', 2, 1))
        release_letter_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 1))
        internal_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 2))
        v4_approved_release_id = str(xlUtilis.read_data(test_data_path, 'release_id', 3, 2))
        v8_user = str(xlUtilis.read_data(test_data_path, 'Login', 7, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 7, 3))
        bu.login_application(v8_user, password)
        #main_window = driver.current_window_handle

        # # click on search for items and reports
        # hp.click_search_for_item_and_reports()
        #
        # # click on search type
        # hp.select_search_type("ID")
        #
        # # Enter ID to search field
        # hp.set_search_type(v4_approved_release_id)
        #
        # # click search submit
        # hp.click_search_submit()
        #
        hp.search_and_open_the_release_from_all_items(v4_approved_release_id)







        # # validation
        # if bu.is_displayed((By.XPATH, "//*[@id='schdata']/tbody/tr/td[12]//tr[2]")):
        #     text = bu.get_text((By.XPATH, "//*[@id='schdata']/tbody/tr/td[12]//tr[2]"))
        #     self.logger.info("**********Discard release successful. Status : " + text + "**************")
        #     assert True, "Discard release successful. Status : " + text
        # else:
        #     self.logger.info("*********Discard release unsuccessful***********")
        #     assert False, "Discard release unsuccessful. Inactive not displayed"

        self.logger.info("********test_019_discard_v4_confirmed_release_as_v4_user : passed*******")
        self.logger.info("*********test_019_discard_v4_confirmed_release_as_v4_user : completed ********")




