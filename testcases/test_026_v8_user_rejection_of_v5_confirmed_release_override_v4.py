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
class Test_026:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_026_v8_user_rejection_of_v5_confirmed_release_override_v4(self, setup):
        self.logger.info("***test_026_v8_user_rejection_of_v5_confirmed_release_override_v4 : started****")

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
        internal_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 2))
        release_letter_comment = str(xlUtilis.read_data(test_data_path, 'tc_004', 2, 1))
        v8_user = str(xlUtilis.read_data(test_data_path, 'Login', 7, 2))
        v8_password = str(xlUtilis.read_data(test_data_path, 'Login', 7, 3))
        v5_user = str(xlUtilis.read_data(test_data_path, 'Login', 4, 2))
        v5_password = str(xlUtilis.read_data(test_data_path, 'Login', 4, 3))
        bu.login_application(v5_user, v5_password)
        main_window = driver.current_window_handle

        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("*****create Release successful. Release ID: " + release_id + "********")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("******akv variant selected. Variant name: " + akv_variant + "*********")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("********a2l file selected. A2l File name : " + a2l_file + " **********")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful : Displayed : " + precheck_data + "**********")
        import_akv_confirmation = rp.click_import_akv_from_care_and_start_confirmation_()
        self.logger.info("********import AKV from care is successful : " + import_akv_confirmation + "***********")
        v5_confirm_release = rp.user_confirmation_as_v5_user_override_v4()
        driver.switch_to.window(main_window)
        self.logger.info("*****confirm release as v5 user successful : " + v5_confirm_release + "*******")
        # Do logout and login again as V8 user and search for v4 confirmed release
        v5_confirmed_release_id = hp.login_again_and_search_release(v8_user, v8_password, release_id)
        self.logger.info("*******V5 confirmed release displayed. Release id : " + v5_confirmed_release_id + " *******")

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

        self.logger.info("******test_026_v8_user_rejection_of_v5_confirmed_release_override_v4 : passed******")
        self.logger.info("******test_026_v8_user_rejection_of_v5_confirmed_release_override_v4 : completed ******")




