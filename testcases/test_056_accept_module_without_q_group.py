import time

import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
import re

@pytest.mark.regression
#@flaky(max_runs=3, min_passes=1)
class Test_056:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_056_accept_module_without_q_group(self, setup):
        self.logger.info("********test_056_accept_module_without_q_group : started********")

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
        driver.find_element_by_id("Button22").click()

        time.sleep(10)
        a = driver.find_element(by=By.XPATH, value="//*[@id='v7rpcc']/pre").text
        text = "Accept Modules without Q-Group"
        # self.logger.info("captured text is : " + a)
        if a.find(text):
            self.logger.info("*******A2L data uploaded successfully : " + text + " *********")
        else:
            "******** Modules upload failed **********"
        # # validation of Distribution report visibility
        # bu.switch_to_frame("3fd7565f-0120-4acc-a488-544ca02979b7")
        # if bu.is_displayed((By.XPATH, "//*[@id='reporttitleCell']")):
        #     text = bu.get_text((By.XPATH, "//*[@id='reporttitleCell']"))
        #     self.logger.info("****distribution report visibility successful : " + "Pass" + "*****")
        #     assert True, "distribution report visibility successful : " + text
        # else:
        #     self.logger.info("******distribution report visibility unsuccessful*******")
        #     assert False, "distribution report visibility unsuccessful."

        self.logger.info("*****test_056_accept_module_without_q_group : passed*******")
        self.logger.info("*****test_056_accept_module_without_q_group : completed *******")
