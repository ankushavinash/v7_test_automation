from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
from flaky import flaky


@flaky(max_runs=3, min_passes=1)
class TestSelectCareAkvVariantForA2lData:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_008_select_care_akv_variant_for_a2l_data(self, setup):
        self.logger.info("********test_008_select_care_akv_variant_for_a2l_data : started********")

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
        care_akv_variant = str(xlUtilis.read_data(test_data_path, 'tc_006', 2, 2))
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 3, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")

        self.logger.info("*******************Select Care AKV Variant for a2l Data************************")
        # select care akv variant for a2l data
        rp.select_care_akv_variant_for_a2l_data(care_akv_variant)
        # Click on ok to select care akv variant for a2l data
        rp.click_ok()

        # Validation for Care akv variant selection
        if bu.is_displayed((By.XPATH, "//*[@id='F14155']")):
            text = bu.get_text((By.XPATH, "//*[@id='F14155']"))
            self.logger.info("******select_care_akv_variant_for_a2l_data : " + text + "*******")
            assert True, "select_care_akv_variant_for_a2l_data : " + text
        else:
            self.logger.info("******select_care_akv_variant_for_a2l_data unsuccessful*******")
            assert False, "select_care_akv_variant_for_a2l_data unsuccessful. AKV Variant not selected"

        self.logger.info("*****test_008_select_care_akv_variant_for_a2l_data  : passed*******")
        self.logger.info("*****test_008_select_care_akv_variant_for_a2l_data  : completed ********")