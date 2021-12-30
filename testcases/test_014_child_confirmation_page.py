from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


class TestUploadDataChildConfirmation:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_014_upload_data_child_confirmation(self, setup):
        self.logger.info("********test_010_care akv variant to release : started********")

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
        a2l_file_name = str(xlUtilis.read_data(test_data_path, 'tc_009', 2, 1))
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")
        akv_variant = rp.set_care_akv_variant(care_group, care_akv_variant)
        self.logger.info("********care akv variant selection successful. Variant name: " + akv_variant + "************")
        a2l_file = rp.select_a2l_data(a2l_file_name)
        self.logger.info("********a2l file selection successful. A2l File name : " + a2l_file + "*****************")

        # Pre-check care and a2l data
        rp.click_precheck_care_and_a2l_data()
        # Pre-check validation of selected a2l file
        if bu.is_displayed((By.XPATH, "//*[@id='v7rpcc']/p")):
            text = bu.get_text((By.XPATH, "//*[@id='v7rpcc']/p"))
            self.logger.info(
                "******a2l file is selection successful. Confirmation message displayed : " + text + "*******")
            assert True, "a2l file selection successful. Confirmation message displayed : " + text
        else:
            self.logger.info("******a2l file is selected unsuccessful*******")
            assert False, "a2l file selection unsuccessful. a2l data is not displayed"

        rp.click_ok()

        # click on start confirmation
        driver.find_element_by_xpath("//*[@id='Button14']").click()
        rp.click_ok()
        driver.find_element_by_xpath("//*[@id='Button14']").click()
        driver.find_element_by_id("SELECT_F13842").click()
        rp.click_ok()

        # validation
        text = driver.find_element_by_xpath("//*[@id='F11159.wrapper']/table/tbody/tr/td[1]").text

        driver.find_element_by_link_text("Child Confirmations").click()

        driver.find_element_by_xpath("//*[@id='ReportOutput']/tbody/tr[3]/td[2]/span/a").click()