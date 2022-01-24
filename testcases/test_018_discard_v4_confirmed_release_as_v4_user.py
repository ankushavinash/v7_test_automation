import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


@pytest.mark.smoke
@pytest.mark.regression
@flaky(max_runs=3, min_passes=1)
class TestDiscardV4ConfirmedReleaseAsV4User:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_018_discard_v4_confirmed_release_as_v4_user(self, setup):
        self.logger.info("********test_018_discard_v4_confirmed_release_as_v4_user : started********")

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
        v4_user = str(xlUtilis.read_data(test_data_path, 'Login', 3, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 3, 3))
        bu.login_application(v4_user, password)
        main_window = driver.current_window_handle
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("********care akv variant selection successful. Variant name: " + akv_variant + "************")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("********a2l file selection successful. A2l File name : " + a2l_file + "*****************")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful : Displayed : " + precheck_data + "*****************")
        import_akv_confirmation = rp.click_import_akv_from_care_and_start_confirmation_val()
        self.logger.info("********import AKV from care is successful : " + import_akv_confirmation + "*****************")
        v4_confirm_release = rp.confirm_release_as_v4_user()
        driver.switch_to.window(main_window)
        driver.switch_to.frame("issuedetails-frame")
        self.logger.info("*********confirm release as v4 user successful : " + v4_confirm_release + "****************")

        # click discard complete confirmation and add comment
        rp.discard_complete_confirmation(release_letter_comment, internal_comment)

        # Discard validation
        driver.switch_to_frame("schFrame")
        if bu.is_displayed((By.XPATH, "//*[@id='schdata']/tbody/tr/td[12]//tr[2]")):
            text = bu.get_text((By.XPATH, "//*[@id='schdata']/tbody/tr/td[12]//tr[2]"))
            self.logger.info("**********Discard release successful. Status : " + text + "**************")
            assert True, "Discard release successful. Status : " + text
        else:
            self.logger.info("*********Discard release unsuccessful***********")
            assert False, "Discard release unsuccessful. Inactive not displayed"

        self.logger.info("********test_018_discard_v4_confirmed_release_as_v4_user : passed*******")
        self.logger.info("*********test_018_discard_v4_confirmed_release_as_v4_user : completed ********")



