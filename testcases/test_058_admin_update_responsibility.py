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
class Test_058:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_058_admin_update_responsibility(self, setup):
        self.logger.info("********test_058_admin_update_responsibility : started********")

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
        driver.switch_to.frame("issuedetails-frame")
        rp.click_child_confirmation()
        driver.switch_to.frame("d40aa4b3-f81d-4f82-b8bf-af6b57d91fa1")
        link_first_part_module_xpath = "//a[@title='A0 (1.0.0)']"
        bu.click((By.XPATH, link_first_part_module_xpath))
        # switch window
        bu.switch_to_child_window(main_window)
        # click on admin update responsibility
        rp.click_admin_update_responsibility()
        v4_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        v5_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        v6_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        v7_primary_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        v4_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        v5_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        v6_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))
        v7_fallback_user = str(xlUtilis.read_data(test_data_path, 'tc_058', 2, 1))


        v4_primary = "v7_automation_v8_user [v7_automation_v8_user]"
        v5_primary = "v7_automation_v8_user [v7_automation_v8_user]"
        v6_primary = "v7_automation_v8_user [v7_automation_v8_user]"
        v7_primary = "v7_automation_v8_user [v7_automation_v8_user]"
        v4_fallback = "v7_automation_v8_user [v7_automation_v8_user]"
        v5_fallback = "v7_automation_v8_user [v7_automation_v8_user]"
        v6_fallback = "v7_automation_v8_user [v7_automation_v8_user]"
        v7_fallback = "v7_automation_v8_user [v7_automation_v8_user]"
        rp.admin_update_of_all_primary_and_fallback_user(v4_primary, v5_primary, v6_primary, v7_primary, v4_fallback, v5_fallback, v6_fallback, v7_fallback)
        driver.switch_to.window(main_window)
        driver.switch_to.frame("issuedetails-frame")
        driver.find_element_by_id("refresh_view").click()
        "//table[@id='ReportOutput']/tbody//span[contains(text(), 'v7_automation_v4_user')]/../../td[2]//a"

        # Validation for successful selection of primary and fallback user
        # if bu.is_displayed((By.ID, "F11170")):
        #     text = bu.get_text((By.ID, "F11170"))
        #     self.logger.info("******import AKV from care is successful. Displayed : " + text + "*******")
        #     assert True, "import AKV from care is successful : " + text
        # else:
        #     self.logger.info("******013_import AKV from care is unsuccessful*******")
        #     assert False, "013_import AKV from care is unsuccessful. import unsuccessful"

        self.logger.info("*****test_058_admin_update_responsibility : passed*******")
        self.logger.info("*****test_058_admin_update_responsibility : completed ********")