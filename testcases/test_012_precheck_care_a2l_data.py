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
class Test_012:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_012_precheck_care_a2l_data(self, setup):
        self.logger.info("********test_012_precheck_care_a2l_data_to_release : started********")

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
        a2l_file = str(xlUtilis.read_data(test_data_path, 'tc_011', 2, 1))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)

        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("********akv variant selected. Variant name: " + akv_variant + "***********")
        a2l_file = rp.select_a2l_data(a2l_file)
        self.logger.info("********a2l file selection successful. A2l File name : " + a2l_file + "*****************")

        # Pre-check care and a2l data
        rp.click_precheck_care_and_a2l_data()

        # Pre-check validation of selected a2l file
        if bu.is_displayed((By.XPATH, "//*[@id='v7rpcc']/table/tbody/tr[1]/th[1]")):
            text = bu.get_text((By.XPATH, "//*[@id='v7rpcc']/table/tbody/tr[1]/th[1]"))
            self.logger.info(
                "******a2l file selection successful. Displayed : " + text + "*******")
            assert True, "a2l file selection successful. Displayed : " + text
        else:
            self.logger.info("******a2l file is selected unsuccessful*******")
            assert False, "a2l file selection unsuccessful. a2l data is not displayed"

        self.logger.info("*****test_012_precheck_care_a2l_data  : passed*******")
        self.logger.info("*****test_012_precheck_care_a2l_data : completed ********")
