from selenium.webdriver.common.by import By
from pathlib import Path
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


class TestCareAKVVariant:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_008_care_akv_variant(self, setup):
        self.logger.info("********test_008_care akv variant to release : started********")

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
        care_group = str(xlUtilis.read_data(test_data_path, 'tc_006', 2, 1))
        care_akv_variant = str(xlUtilis.read_data(test_data_path, 'tc_006', 2, 2))
        comment = str(xlUtilis.read_data(test_data_path, 'tc_007', 2, 1))
        root_path = str(Path(__file__).parent.parent)
        file_path = "\\testdata\\upload_test_automation.a2l"
        a2l_file = root_path + file_path
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")

        self.logger.info("*****Care AKV Variant to release*********")
        rp.click_care_akv_variant()
        # select care group : TEST
        rp.select_care_group(care_group)
        # select care akv variant : TEST AKV Variant _kraoliv_
        rp.select_care_akv_variant(care_akv_variant)
        # click on OK
        rp.click_ok()
        # care akv variant validation
        if bu.is_displayed((By.XPATH, "//*[@id='F13688']")):
            text = bu.get_text((By.XPATH, "//*[@id='F13688']"))
            self.logger.info("******Care AKV Variant selected. : " + text + "*******")
            assert True, "Care AKV Variant selection successful. : " + text
        else:
            self.logger.info("******Care AKV Variant selected unsuccessful*******")
            assert False, "Care AKV Variant selection unsuccessful. Care AKV Variant is not displayed"

        self.logger.info("*****test_008_care_akv_variant  : passed*******")
        self.logger.info("*****test_008_care_akv_variant : completed ********")