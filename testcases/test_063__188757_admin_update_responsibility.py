import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


# @pytest.mark.smoke
# @pytest.mark.regression
# @flaky(max_runs=3, min_passes=1)
class Test_063:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_063_admin_update_responsibility(self, setup):
        self.logger.info("********test_063_admin_update_responsibility : started********")

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
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        admin_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        admin_password = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 2))
        v4_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 3))
        v5_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 4))
        v6_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 5))
        v7_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 6))
        v4_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 7))
        v5_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 8))
        v6_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 9))
        v7_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 10))
        bu.login_application(normal_user, password)
        main_window = driver.current_window_handle

        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("********akv variant selected. Variant name: " + akv_variant + "***********")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("********a2l file selected. A2l File name : " + a2l_file + "*****************")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful. Displayed : " + precheck_data + "*****************")
        rp.click_import_akv_from_care_and_start_confirmation()

        # logout and login as admin and search the release
        hp.login_again_and_search_release(admin_user, admin_password, release_id)
        self.logger.info("********Login as Admin : " + admin_user + "************")
        # select first module for updating admin update responsibility
        rp.select_first_module_for_admin_update_responsibility()
        bu.switch_to_child_window(main_window)
        # click on admin update responsibility
        rp.click_admin_update_responsibility()
        # fill all primary and fallback user
        rp.admin_update_of_all_primary_and_fallback_user(v4_primary_user, v5_primary_user, v6_primary_user,
                      v7_primary_user, v4_fallback_user, v5_fallback_user, v6_fallback_user, v7_fallback_user)
        driver.switch_to.window(main_window)
        # click refresh to view the changes
        rp.click_refresh()

        # Validation for successful selection of primary and fallback user
        driver.switch_to.frame("4ea6d89b-d573-4aa9-bfe5-1209284765c4")
        if bu.is_displayed((By.XPATH, "//*[@id='ReportOutput']/tbody/tr[9]/td[3]/span")):
            text = bu.get_text((By.XPATH, "//*[@id='ReportOutput']/tbody/tr[9]/td[3]/span"))
            v7_update_user_validation = text.replace("[v7_automation_v8_user]", "").strip()
            self.logger.info("***Admin update responsibility successful. Displayed added User : " + v7_update_user_validation + "*****")
            assert True, "Admin update responsibility successful : " + v7_update_user_validation
        else:
            self.logger.info("******063_Admin update responsibility unsuccessful*******")
            assert False, "063_Admin update responsibility unsuccessful. update failed"

        self.logger.info("*****test_063_admin_update_responsibility : passed*******")
        self.logger.info("*****test_063_admin_update_responsibility : completed ********")