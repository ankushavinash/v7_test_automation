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

    def test_057_reimport_a2l(self, setup):
        self.logger.info("********test_057_reimport_a2l : started********")

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
        bu.login_application(normal_user, password)
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("******akv variant selected. Variant name: " + akv_variant + " *****")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("********a2l file selected. A2l File name : " + a2l_file + "*****************")
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful. Displayed : " + precheck_data + "*****************")
        rp.click_import_akv_from_care_and_start_confirmation_()

        # click on Reimport a2l and read akv from care
        driver.find_element_by_id("Button15").click()

        #rp.click_child_confirmation()

        # validation of Distribution report visibility
        bu.switch_to_frame("3fd7565f-0120-4acc-a488-544ca02979b7")
        if bu.is_displayed((By.XPATH, "//*[@id='reporttitleCell']")):
            text = bu.get_text((By.XPATH, "//*[@id='reporttitleCell']"))
            self.logger.info("****distribution report visibility successful : " + "Pass" + "*****")
            assert True, "distribution report visibility successful : " + text
        else:
            self.logger.info("******distribution report visibility unsuccessful*******")
            assert False, "distribution report visibility unsuccessful."

        self.logger.info("*****test_057_reimport_a2l : passed*******")
        self.logger.info("*****test_057_reimport_a2l : completed *******")
