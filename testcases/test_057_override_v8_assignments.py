import pytest
from flaky import flaky
from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


@pytest.mark.regression
#@flaky(max_runs=3, min_passes=1)
class Test_057:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_057_override_v8_assignments(self, setup):
        self.logger.info("********test_057_override_v8_assignments : started********")

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
        care_group = str(xlUtilis.read_data(test_data_path, 'tc_056', 2, 1))
        care_akv_variant = str(xlUtilis.read_data(test_data_path, 'tc_056', 2, 2))
        a2l_file_name = str(xlUtilis.read_data(test_data_path, 'tc_056', 2, 3))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("******akv variant selected. Variant name: " + akv_variant + " *****")
        a2l_file = rp.select_a2l_data_without_q_group(a2l_file_name)
        self.logger.info("********a2l file selected. A2l File name : " + a2l_file + "*****************")

        # click precheck care and a2l data button
        rp.click_precheck_care_and_a2l_data()

        # override V8 assignment
        rp.override_v8_assignment_and_start_confirmation()

        # validation successful override of V8
        if bu.is_displayed((By.ID, "F11170")):
            text = bu.get_text((By.ID, "F11170"))
            self.logger.info("****V8 override successful : " + text + "*****")
            assert True, "V8 override successful : " + text
        else:
            self.logger.info("******V8 override unsuccessful*******")
            assert False, "V8 override unsuccessful."

        self.logger.info("*****test_057_override_v8_assignments : passed*******")
        self.logger.info("*****test_057_override_v8_assignments : completed *******")
