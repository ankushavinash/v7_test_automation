from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen
from flaky import flaky


@flaky(max_runs=3, min_passes=1)
class TestLoginToV7Dashboard:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_001_login_to_v7_dashboard(self, setup):
        self.logger.info("********Login to V7 Release Administration : started********")

        # Setup
        driver = setup[0]
        test_data_path = setup[2]
        hp = HomePage(driver)
        bu = BrowserUtilities(driver)

        # Test data setup
        application = "V4..V8 Admin"
        normal_user = str(xlUtilis.read_data(test_data_path, 'Login', 2, 2))
        password = str(xlUtilis.read_data(test_data_path, 'Login', 2, 3))
        bu.login_application(normal_user, password)

        # Search for V7 Release Application
        hp.search_application(application)

        # validation of V7 Release Application Dashboard
        if bu.is_displayed((By.ID, "j_projLPCaption")):
            text = bu.get_text((By.ID, "j_projLPCaption"))
            self.logger.info("******001_login_to_v7_dashboard successful. Dashboard info : " + text + "*******")
            assert True, "login_to_v7_dashboard successful. Dashboard info : " + text
        else:
            self.logger.info("******create release unsuccessful*******")
            assert False, "001_login_to_v7_dashboard unsuccessful. Dashboard not displayed"

        self.logger.info("*****test_001_login_to_v7_dashboard  : passed*******")
        self.logger.info("*****test_001_login_to_v7_dashboard  : completed ********")




