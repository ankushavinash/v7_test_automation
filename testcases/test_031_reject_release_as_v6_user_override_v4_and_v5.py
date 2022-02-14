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
class TestRejectReleaseAsV6UserOverrideV4AndV5:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_031_reject_release_as_v6_user_override_v4_and_v5(self, setup):
        self.logger.info("********test_031_reject_release_as_v6_user_override_v4_and_v5 : started********")

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
        v6_user = str(xlUtilis.read_data(test_data_path, 'Login', 5, 2))
        v6_password = str(xlUtilis.read_data(test_data_path, 'Login', 5, 3))
        bu.login_application(v6_user, v6_password)

        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("*******akv variant selected. Variant name: " + akv_variant + "*********")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("******a2l file selected. A2l File name : " + a2l_file + "*********")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("*******precheck confirmation successful : Displayed : " + precheck_data + "**********")
        import_akv_confirmation = rp.click_import_akv_from_care_and_start_confirmation_()
        self.logger.info("*******import AKV from care is successful : " + import_akv_confirmation + "**********")

        # click on child confirmation
        rp.click_child_confirmation()
        # click on user confirmation record
        rp.click_user_confirmation_project_v6_user()
        # click confirmation button
        rp.click_confirmation_or_reject_button()
        # click on part module reject button as v5 user
        rp.reject_part_modules_as_v6_user_override_v4_and_v5()
        # click OK
        rp.click_ok()

        # validation
        if bu.is_displayed((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[8]/p[2]")):
            text = bu.get_text((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[8]/p[2]"))
            self.logger.info("******reject release as v6 user successful : " + text + "*******")
            assert True, "reject release as v6 user successful : " + text
        else:
            self.logger.info("******reject release as v6 user unsuccessful*******")
            assert False, "reject release as v6 user unsuccessful."

        self.logger.info("******test_031_reject_release_as_v6_user_override_v4_and_v5  : passed*******")
        self.logger.info("******test_031_reject_release_as_v6_user_override_v4_and_v5  : completed ********")




