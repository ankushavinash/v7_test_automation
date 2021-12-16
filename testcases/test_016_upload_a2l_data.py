import time

from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen

class TestCareAKVforA2LData:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_016_upload_a2l_data(self, setup):
        self.logger.info("********test_016_upload_a2l_data : started********")

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
        care_group = str(xlUtilis.read_data(test_data_path, 'tc_005', 2, 1))
        care_akv_varient = str(xlUtilis.read_data(test_data_path, 'tc_005', 2, 2))
        comment = str(xlUtilis.read_data(test_data_path, 'tc_016', 2, 1))
        hp.search_project(project)
        rp.fill_all_information(title, description, date, v8, project_write_access)
        rp.click_ok()

        rp.select_care_akv_varient_for_a2l_data(care_akv_varient)
        rp.click_ok()
        if bu.is_displayed((By.XPATH, "//*[@id='F14155']")):
            text = bu.get_text((By.XPATH, "//*[@id='F14155']"))
            self.logger.info("******015_care_akv_varient_for_a2l_data : " + text + "*******")
            assert True, "015_care_akv_varient_for_a2l_data : " + text
        else:
            self.logger.info("******015_care_akv_vareint_for_a2l_data unsuccessful*******")
            assert False, "015_care_akv_varient_for_a2l_data unsuccessful. AKV Varient not selected"

        self.logger.info("*******************Add Upload Comment************************")
        rp.set_comment(comment)


        self.logger.info("*******************Upload a2l Data************************")
        root_path = str(Path(__file__).parent.parent)
        file = "C:\\Users\\anavina\\PycharmProjects\\v7_test_automation\\testdata\\t07.a2l"
        rp.upload_a2l_data()
        time.sleep(8)
        rp.click_workarea()


