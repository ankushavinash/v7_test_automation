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
class Test_049:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_049_reject_module_as_v5_user(self, setup):
        self.logger.info("********test_049_reject_module_as_v5_user : started********")

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
        reject_comment_v5_user = str(xlUtilis.read_data(test_data_path, 'tc_049', 2, 1))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        v4_user = str(xlUtilis.read_data(test_data_path, 'Login', 3, 2))
        v4_password = str(xlUtilis.read_data(test_data_path, 'Login', 3, 3))
        v5_user = str(xlUtilis.read_data(test_data_path, 'Login', 4, 2))
        v5_password = str(xlUtilis.read_data(test_data_path, 'Login', 4, 3))
        bu.login_application(normal_user, password)
        main_window = driver.current_window_handle

        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("********akv variant selected. Variant name: " + akv_variant + "***********")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("********a2l file selected. A2l File name : " + a2l_file + "***********")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful : Displayed : " + precheck_data + "**********")
        import_akv_confirmation = rp.click_import_akv_from_care_and_start_confirmation_()
        self.logger.info("********import AKV from care is successful : " + import_akv_confirmation + "************")
        hp.login_again_and_search_release(v4_user, v4_password, release_id)
        confirm_module_as_v4 = rp.module_confirmation_as_v4_user(main_window)
        self.logger.info("******confirm module as v4 user successful. status : " + confirm_module_as_v4 + "*******")
        self.logger.info("**********Login as V5 user : " + v5_user + "***********")
        driver.switch_to.window(main_window)
        hp.login_again_and_search_release(v5_user, v5_password, release_id)
        driver.switch_to.frame("issuedetails-frame-iframe")
        self.logger.info("*******Search for v4 confirmed module. Release ID: " + release_id + " *********")

        # click on child confirmation
        rp.click_child_confirmation()
        # click on module confirmation as v5 user
        rp.click_module_confirmation()
        # click on reject button as V4 user and enter comment to reject module
        rp.click_reject_as_v5_user(reject_comment_v5_user, main_window)
        # click on Ok to reject the release
        rp.click_ok()

        # validation
        if bu.is_displayed((By.ID, "F11197")):
            text = bu.get_text((By.ID, "F11197"))
            self.logger.info("******reject module as v5 user successful. status : " + text + "*******")
            assert True, "reject module as v5 user successful. status : " + text
        else:
            self.logger.info("******reject module as v6 user unsuccessful*******")
            assert False, "reject module as v5 user unsuccessful."

        self.logger.info("********test_049_reject_module_as_v5_user  : passed*******")
        self.logger.info("*********test_049_reject_module_as_v5_user  : completed ********")




