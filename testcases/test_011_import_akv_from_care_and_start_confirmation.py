from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


class TestImportAkvFromCareAndStartConfirmation:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_011_import_akv_from_care_and_start_confirmation(self, setup):
        self.logger.info("********test_011_import_akv_from_care_and_start_confirmation_to_release : started********")

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
        precheck_data = rp.click_precheck_care_a2l_data()
        self.logger.info("********precheck confirmation successful : " + precheck_data + "*****************")

        # click on import AKV from care and start confirmation
        rp.click_import_akv_from_care_and_start_confirmation_override_v8()

        # Validation for successful import akv from care and start confirmation
        if bu.is_displayed((By.XPATH, "//*[@id='F11159.wrapper']/table/tbody/tr/td[1]")):
            text = bu.get_text((By.XPATH, "//*[@id='F11159.wrapper']/table/tbody/tr/td[1]"))
            self.logger.info("******011_import AKV from care is successful : " + text + "*******")
            assert True, "011_import AKV from care is successful : " + text
        else:
            self.logger.info("******011_import AKV from care is unsuccessful*******")
            assert False, "011_import AKV from care is unsuccessful. import unsuccessful"

        self.logger.info("*****test_011_import_akv_from_care_and_start_confirmation_to_release : passed*******")
        self.logger.info("*****test_011_import_akv_from_care_and_start_confirmation_to_release : completed ********")