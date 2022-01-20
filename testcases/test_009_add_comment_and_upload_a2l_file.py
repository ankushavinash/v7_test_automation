import pytest
from flaky import flaky
from selenium.webdriver.common.by import By
from pathlib import Path
from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


@pytest.mark.regression
@flaky(max_runs=3, min_passes=1)
class TestAddCommentAndUploadA2lFile:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_009_add_comment_and_upload_a2l_file(self, setup):
        self.logger.info("********test_009_Add comment and upload a2l data : started********")

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
        care_akv_variant = str(xlUtilis.read_data(test_data_path, 'tc_008', 2, 2))
        upload_comment = str(xlUtilis.read_data(test_data_path, 'tc_009', 2, 1))
        a2l_file_name = str(xlUtilis.read_data(test_data_path, 'tc_009', 2, 2))
        root_path = str(Path(__file__).parent.parent)
        file_path = "\\testdata\\upload_test_automation.a2l"
        a2l_file = root_path + file_path
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)
        hp.search_project(project)
        release_id = rp.create_release(title, description, date, v8, project_write_access)
        self.logger.info("***************create Release successful. Release ID: " + release_id + " ***************")

        # Select care akv variant for a2l data
        care_akv_variant_name = rp.search_and_select_care_akv_variant_for_a2l_data(care_akv_variant)
        self.logger.info("*********a2l data selected successful: AKV Variant name: " + care_akv_variant_name + "*******")

        # Add comment
        rp.set_comment(upload_comment)
        # Upload a2l file
        rp.upload_a2l_data(a2l_file)

        # Upload Comment validation
        upload_text = bu.get_text((By.XPATH, "//*[@id='a2lged']/table/tbody/tr[3]/td[2]"))
        if upload_text == upload_comment:
            self.logger.info("******Comment validation success : " + upload_text + "*******")
            assert True, "Comment added successful. Comment : " + upload_text
        else:
            self.logger.info("******Comment Validation Failed*******")
            assert False, "Comment addition unsuccessful. Comment not added"

        # A2L file upload validation
        current_a2l_file_name = bu.get_text((By.LINK_TEXT, "upload_test_automation.a2l"))
        if current_a2l_file_name == a2l_file_name:
            self.logger.info("******009_add_comment_and_upload_a2l_data successful. File name : "
                             + current_a2l_file_name + "*******")
            assert True, "009_add_comment_and_upload_a2l_data successful. File name : " + current_a2l_file_name
        else:
            self.logger.info("******add_comment_and_upload a2l data unsuccessful*******")
            assert False, "test_009_upload_a2l_data unsuccessful. a2l file not uploaded"

        self.logger.info("*****test_009_add_comment_and_upload_a2l_data  : passed*******")
        self.logger.info("*****test_009_add_comment_and_upload_a2l_data  : completed ********")





