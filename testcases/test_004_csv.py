import time

from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.ReleasePage import ReleasePage
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.customLogger import LogGen


class TestReleaseCSVImport:
    # log variable instantiation
    logger = LogGen.loggen()

    def test_004_release_csv_import(self, setup):
        self.logger.info("********test_003_release_csv_import : started********")

        # Setup
        driver = setup[0]
        test_data_path = setup[2]
        lp = HomePage(driver)
        rp = ReleasePage(driver)
        bu = BrowserUtilities(driver)

        # Test data setup
        project = "V7 Release Administration"
        title = str(xlUtilis.read_data(test_data_path, 'tc_001', 2, 1))
        file = str(".\\testdata\\csvTestData.csv")
        self.logger.info("*****create release*********")
        lp.search_project(project)
        rp.set_title(title)
        rp.click_ok()
        if driver.find_element_by_xpath("//a[text()='Workarea']").is_selected():
            pass
        else:
           driver.find_element_by_xpath("//a[text()='Workarea']").click()

        #rp.click_workarea()
        self.logger.info("*****Upload CSV file*********")

        parent_widnow = driver.current_window_handle
        print("Parent window name is : ", parent_widnow)
        print("Main window title : ", driver.title)
        rp.click_CSV_upload()
        print("*****click on csv upload*********")
        time.sleep(6)

        child_windows = driver.window_handles
        print("Print all window : ",  type(child_windows))

        for child in child_windows:
            print(child)
            if parent_widnow != child:
                driver.switch_to.window(child)
                time.sleep(3)
                if driver.find_element_by_xpath("//*[@id='Title']").is_displayed():
                    driver.find_element_by_xpath("//*[@id='Title']").send_keys("Automation Upload test")
                else:
                    driver.quit()
                # driver.switch_to.frame("utiltop")
                # #print("title is: ", driver.title)
                # driver.find_element_by_xpath("//*[@id='Title']").send_keys("Automation Upload test")



        # self.logger.info(driver.current_window_handle) # CW
        # handles = driver.window_handles
        # for handle in handles:
        #     driver.switch_to.window(handle)
        #     #driver.switch_to_window(handle)
        #     self.logger.info(driver.title)
        #     driver.find_element_by_class_name("frmTxt").send_keys("Automation Upload test")
        #     upload_xpath = "//input[@name='Filetext']"
        #     driver.find_element_by_xpath(upload_xpath).send_keys("C:\\Users\\anavina\\PycharmProjects\\v7_test_automation\\testdata\\csvTestData.csv")
        # time.sleep(10)

        #driver.quit()


        #"//input[@id='File']"
        #bu.file_upload(file)
        #self.logger.info("*****file uploaded successful*********")



        self.logger.info("*****test_004_Import_CSV_to_release  : passed*******")
        self.logger.info("*****test_004_Import_CSV_to_release : completed ********")





