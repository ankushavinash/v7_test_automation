import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


# @pytest.mark.regression
# @flaky(max_runs=3, min_passes=1)
class Test_011:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_011_select_a2l_data(self, setup):
        self.logger.info("********test_011_select_a2l data : started********")

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

        self.logger.info("*****Select A2L Data*********")
        # click on select a2l data
        rp.click_a2l_data()
        # click on checkbox
        rp.select_a2l_data_from_list(a2l_file)
        # click on ok
        rp.click_ok()

        # validation of selected a2l file
        if bu.is_displayed((By.XPATH, "//*[@id='F14154']")):
            text = bu.get_text((By.XPATH, "//*[@id='F14154']"))
            self.logger.info("******a2l file is selection successful. File name : " + text + "*******")
            assert True, "a2l file selection successful. file name : " + text
        else:
            self.logger.info("******a2l file selection unsuccessful*******")
            assert False, "a2l file selection unsuccessful. a2l file is not displayed"

        self.logger.info("*****test_011_select_a2l_data  : passed*******")
        self.logger.info("*****test_011_select_a2l_data : completed ********")
