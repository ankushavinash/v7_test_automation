from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
from flaky import flaky


@flaky()
class TestReleaseCsvImport:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_015_release_csv_import(self, setup):
        self.logger.info("********test_005_release_csv_import : started********")

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
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful.Release ID: " + release_id + " ***************")

        self.logger.info("*******************Select Care AKV Vareint for a2l Data************************")
        rp.select_care_akv_varient_for_a2l_data(care_akv_varient)
        rp.click_ok()

        if bu.is_displayed((By.XPATH, "//*[@id='F14155']")):
            text = bu.get_text((By.XPATH, "//*[@id='F14155']"))
            self.logger.info("******015_care_akv_varient_for_a2l_data : " + text + "*******")
            assert True, "015_care_akv_varient_for_a2l_data : " + text
        else:
            self.logger.info("******015_care_akv_vareint_for_a2l_data unsuccessful*******")
            assert False, "015_care_akv_varient_for_a2l_data unsuccessful. AKV Varient not selected"

        self.logger.info("*****test_015_care_akv_vareint_for_a2l_data  : passed*******")
        self.logger.info("*****test_015_care_akv_vareint_for_a2l_data  : completed ********")