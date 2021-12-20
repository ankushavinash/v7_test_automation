import time

from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


class TestCareAKVVariant:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_005_care_akv_variant(self, setup):
        self.logger.info("********test_005_care akv import to release : started********")

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

        rp.select_care_akv_variant_for_a2l_data(care_akv_varient)
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
        rp.upload_a2l_data()
        #driver.switch_to_alert().accept()
        time.sleep(8)
        #################Valiation for comment and a2l data###################
        s = driver.find_element_by_xpath("//*[@id='a2lged']/table/tbody/tr[3]/td[2]").text

        rp.click_workarea()
        self.logger.info("*****Care AKV Variant release*********")
        rp.click_care_akv_varient()
        rp.select_care_group(care_group)
        rp.select_care_akv_varient(care_akv_varient)
        rp.click_ok()

        self.logger.info("*****Select A2L Data*********")
        driver.find_element_by_xpath("//*[@id='Button19']").click()
        self.logger.info(s)


        # self.logger.info("-------------------Click on Upload A2L button-----------------------")
        # root_path = str(Path(__file__).parent.parent)
        # file_path = root_path + "\\testdata\\csvTestData.csv"
        #
        # #C:\Users\anavina\PycharmProjects\v7_test_automation\testdata\csvTestData.csv
        # self.logger.info(file_path)
        # self.bu.file_upload(file_path)
        #

        #
        #
        # driver.find_element_by_xpath("//*[@id='mrx2table']/tbody/tr[1]/th[2]/div/input").send_keys("Test")





