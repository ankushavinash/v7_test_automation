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
class Test_029:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_029_v5_user_rejection_of_v4_confirmed_release(self, setup):
        self.logger.info("**********test_029_v5_user_rejection_of_v4_confirmed_release : started**********")

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
        v4_user = str(xlUtilis.read_data(test_data_path, 'Login', 3, 2))
        v4_password = str(xlUtilis.read_data(test_data_path, 'Login', 3, 3))
        v5_user = str(xlUtilis.read_data(test_data_path, 'Login', 4, 2))
        v5_password = str(xlUtilis.read_data(test_data_path, 'Login', 4, 3))
        bu.login_application(v4_user, v4_password)
        main_window = driver.current_window_handle

        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("*******akv variant selected. Variant name: " + akv_variant + "**********")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("********a2l file selected. A2l File name : " + a2l_file + " **********")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful : Displayed : " + precheck_data + "**********")
        import_akv_confirmation = rp.click_import_akv_from_care_and_start_confirmation_()
        self.logger.info("********import AKV from care is successful : " + import_akv_confirmation + "*****************")
        # V4 user confirmation of release
        v4_confirm_release = rp.user_confirmation_as_v4_user()
        driver.switch_to.window(main_window)
        self.logger.info("*******confirm release as v4 user successful : " + v4_confirm_release + "*********")

        # login again as V5 user
        hp.login_again_and_search_release(v5_user, v5_password, release_id)
        driver.switch_to.frame("issuedetails-frame")
        self.logger.info("********Login again as V5 user and search release: " + release_id + "********")
        # Click on child Confirmation
        rp.click_child_confirmation()
        # Click on user confirmation project v5 user
        rp.click_user_confirmation_project_v5_user()
        self.logger.info("*************Click on user confirmation of project as v5 user **************")
        # click on confirm or reject button
        rp.click_confirmation_or_reject_button()
        # Click on confirm button for confirmation of part modules as v5 user
        rp.reject_part_modules_as_v5_user()
        # click on Ok to confirm the changes
        rp.click_ok()

        # validation
        if bu.is_displayed((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[7]/p[2]")):
            text = bu.get_text((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[7]/p[2]"))
            v5_user_validation = text.replace("[v7_automation_v5_user]", "").strip()
            self.logger.info("*****reject release as v5 user successful : " + v5_user_validation + "******")
            assert True, "reject release as v5 user successful : " + v5_user_validation
        else:
            self.logger.info("******reject release as v5 user unsuccessful*******")
            assert False, "reject release as v5 user unsuccessful."

        self.logger.info("*********test_029_v5_user_rejection_of_v4_confirmed_release : passed*******")
        self.logger.info("*********test_029_v5_user_rejection_of_v4_confirmed_release : completed ********")




