from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
from pathlib import Path
from flaky import flaky


@flaky()
class TestUploadA2LData:
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
        upload_comment = str(xlUtilis.read_data(test_data_path, 'tc_016', 2, 1))
        a2l_file_name = str(xlUtilis.read_data(test_data_path, 'tc_016', 2, 2))
        root_path = str(Path(__file__).parent.parent)
        file_path = "\\testdata\\upload_test_automation.a2l"
        a2l_file = root_path + file_path
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful.Release ID: " + release_id + " ***************")

        # Select care akv varient for a2l data
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
        rp.set_comment(upload_comment)

        self.logger.info("*******************Upload a2l Data************************")
        rp.upload_a2l_data(a2l_file)

        # Upload Comment validation
        upload_text = bu.get_text((By.XPATH, "//*[@id='a2lged']/table/tbody/tr[3]/td[2]"))
        if upload_text == upload_comment:
            self.logger.info("******Comment validation success : " + upload_text + "*******")
            assert True, "Comment added successful. Comment : " + upload_comment
        else:
            self.logger.info("******Comment Validation Failed*******")
            assert False, "Comment addition unsuccessful. Comment not added"

        self.logger.info("*****Comment addition  : passed*******")
        self.logger.info("*****comment addition  : completed ********")

        # A2L file upload validation
        current_a2l_file_name = bu.get_text((By.LINK_TEXT, "upload_test_automation.a2l"))
        if current_a2l_file_name == a2l_file_name:
            self.logger.info("******016_upload_a2l_data successful. File name : " + current_a2l_file_name + "*******")
            assert True, "016_upload_a2l_data successful. File name : " + current_a2l_file_name
        else:
            self.logger.info("******upload a2l data unsuccessful*******")
            assert False, "test_016_upload_a2l_data unsuccessful. a2l file not uploaded"

        self.logger.info("*****test_016_upload_a2l_data  : passed*******")
        self.logger.info("*****test_016_upload_a2l_data  : completed ********")




