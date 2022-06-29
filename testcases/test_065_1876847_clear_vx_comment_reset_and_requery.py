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
class Test_065:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_065_clear_vx_comment_reset_and_requery(self, setup):
        self.logger.info("********test_065_clear_vx_comment_reset_and_requery : started********")

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
        reject_comment_v4_user = str(xlUtilis.read_data(test_data_path, 'tc_047', 2, 1))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        v4_user = str(xlUtilis.read_data(test_data_path, 'Login', 3, 2))
        v4_password = str(xlUtilis.read_data(test_data_path, 'Login', 3, 3))
        v5_user = str(xlUtilis.read_data(test_data_path, 'Login', 4, 2))
        v5_password = str(xlUtilis.read_data(test_data_path, 'Login', 4, 3))
        reject_comment_v5_user = str(xlUtilis.read_data(test_data_path, 'tc_049', 2, 1))
        v6_user = str(xlUtilis.read_data(test_data_path, 'Login', 5, 2))
        v6_password = str(xlUtilis.read_data(test_data_path, 'Login', 5, 3))
        reject_comment_v6_user = str(xlUtilis.read_data(test_data_path, 'tc_051', 2, 1))
        v7_user = str(xlUtilis.read_data(test_data_path, 'Login', 6, 2))
        v7_password = str(xlUtilis.read_data(test_data_path, 'Login', 6, 3))
        reject_comment_v7_user = str(xlUtilis.read_data(test_data_path, 'tc_053', 2, 1))
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
        self.logger.info("********a2l file selected. A2l File name : " + a2l_file + "***********")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful : Displayed : " + precheck_data + "*****************")
        import_akv_confirmation = rp.click_import_akv_from_care_and_start_confirmation_()
        self.logger.info("********import AKV from care is successful : " + import_akv_confirmation + "*****************")

        # login and reject v4 module as v4 user
        hp.login_again_and_search_release(v4_user, v4_password, release_id)
        rp.reject_as_v4_user(reject_comment_v4_user, main_window)
        driver.switch_to.window(main_window)
        # login and reject module as v5 user
        hp.login_again_and_search_release(v5_user, v5_password, release_id)
        rp.reject_as_v5_user(reject_comment_v5_user, main_window)
        driver.switch_to.window(main_window)
        # login and reject module as v6 user
        hp.login_again_and_search_release(v6_user, v6_password, release_id)
        rp.reject_as_v6_user(reject_comment_v6_user, main_window)
        driver.switch_to.window(main_window)
        # login and reject module as v7 user
        hp.login_again_and_search_release(v7_user, v7_password, release_id)
        rp.reject_as_v7_user(reject_comment_v7_user, main_window)
        driver.switch_to.window(main_window)
        # login as admin user
        hp.login_again_and_search_release(admin_user, admin_password, release_id)
        # clear comment for different user by reset and requery button
        rp.click_reset_and_requery(main_window)

        # validation
        driver.switch_to.frame("ViewFrame")
        if bu.is_displayed((By.ID, "F11197")):
            text = bu.get_text((By.ID, "F11197"))
            self.logger.info("******reset and requery successful. state : " + text + "*******")
            assert True, "reset and requery successful. state : " + text
        else:
            self.logger.info("******reset and requery unsuccessful*******")
            assert False, "reset and requery unsuccessful."

        self.logger.info("********test_065_clear_vx_comment_reset_and_requery  : passed*******")
        self.logger.info("*********test_065_clear_vx_comment_reset_and_requery  : completed ********")


#
#