import getpass
import time
import win32con
import win32gui
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import datetime


class BrowserUtilities:
    # --------------------------------locator identifier------------------------
    text_login_id_id = "authUID"
    text_password_id = "authPWD"
    button_sign_in_id = "logonButton"
    image_header_id = "header-logo_image"
    image_sbm_login_page_id = "solution_name_icon"
    button_user_role_id = "header_user_avatar"
    link_logout_xpath = "//a[contains(text(),'Sign Out')]"

    # -------------------------------object initialization----------------------
    def __init__(self, driver):
        self.driver = driver

    # author : venugopal
    # since : 2021-08-10
    # this function is to launch application
    # argument : driver, url
    # return :
    def launch_application(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, 30).until(EC.title_is("Solutions Business Manager"))
            WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.ID, self.button_sign_in_id))))
        except TimeoutException:
            assert False, "Launch application unsuccessful"

    # author : ankush
    # since : 2021-12-01
    # this method is to click login to application
    # argument :
    # return :
    def login_application(self, login_id, password):
        BrowserUtilities.send_keys(self, (By.ID, self.text_login_id_id), login_id)
        BrowserUtilities.send_keys(self, (By.ID, self.text_password_id), password)
        BrowserUtilities.click(self, (By.ID, self.button_sign_in_id))
        by_locator = (By.ID, self.image_header_id)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                assert True, "Login successful"
        except TimeoutException:
            assert False, "Login unsuccessful"

    # author : ankush
    # since : 2022-01-27
    # this method is to click logout
    # argument :
    # return :
    def logout_application(self):
        BrowserUtilities.click(self, (By.ID, self.button_user_role_id))
        BrowserUtilities.click(self, (By.XPATH, self.link_logout_xpath))
        by_locator = (By.ID, self.image_sbm_login_page_id)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                assert True, "Logout successful"
        except TimeoutException:
            assert False, "Logout unsuccessful"

    # author : venugopal
    # since : 2021-08-10
    # this generic used to perform click
    # argument : locator of the element
    # return :
    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator)).click()
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        except ElementClickInterceptedException:
            assert False, "Locator " + str(by_locator) + "not click able"

    # author : venugopal
    # since : 2021-08-10
    # this generic used to perform set
    # argument : locator of the element
    # return :
    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).clear()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"

    # author : venugopal
    # since : 2021-08-10
    # this generic used to verify selection of element
    # argument : locator of the element
    # return : true / false
    def is_selected(self, by_locator):
        try:
            status = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).is_selected()
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        else:
            return bool(status)

    # author : venugopal
    # since : 2021-08-10
    # this generic used to verify display of element
    # argument : locator of the element
    # return : true / false
    def is_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
            status = element.is_displayed()
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        else:
            return bool(status)

    # author : venugopal
    # since : 2021-08-10
    # this generic used to verify enable of element
    # argument : locator of the element
    # return : true / false
    def is_enabled(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
            status = element.is_enabled()
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        else:
            return bool(status)

    # author : venugopal
    # since : 22021-08-10
    # this generic used to clear text
    # argument : locator of the element
    # return :
    def clear_text(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).clear()
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"

    # author : venugopal
    # since : 2021-08-10
    # this generic used to clear text
    # argument : locator of the element
    # return :
    def get_text(self, by_locator):
        try:
            text = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).text
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        else:
            return text.strip()

    # author : venugopal
    # since : 2021-08-25
    # this method is to switch to frame
    # return :
    def switch_to_frame(self, frame):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.driver.switch_to.frame(frame)

    # author : venugopal
    # since : 2021-08-10
    # this generic used to verify not display of element
    # argument : locator of the element
    # return : true / false
    def is_not_displayed(self, by, locator):
        try:
            status = not (self.driver.find_element(by, locator).is_displayed())
        except NoSuchElementException:
            status = True
        return bool(status)

    # author : venugopal
    # since : 2021-08-10
    # this generic method used to upload file
    # argument : file_path
    # return :
    @staticmethod
    def file_upload(file_path):
        time.sleep(5)
        dialog = win32gui.FindWindow('#32770', u'File Upload')  # Dialog
        combobox_ex_32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        combo_box = win32gui.FindWindowEx(combobox_ex_32, 0, 'ComboBox', None)
        edit = win32gui.FindWindowEx(combo_box, 0, 'Edit', None)
        # The above three sentences look for objects in turn until they find the handle of the input box Edit object
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # ButtonButton
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None,
                             file_path)  # Enter the absolute address into the input box
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    # author : venugopal
    # since : 2021-08-10
    # this generic method used get parent path
    # argument : file_path
    # return :
    @staticmethod
    def get_parent_path():
        return str(Path(__file__).parent.parent)

    # author : venugopal
    # since : 2021-08-10
    # this generic used to clear text
    # argument : locator of the element
    # return :
    def get_selected_text(self, by, locator):
        # BrowserUtilities.wait_for_spinner_to_vanish(self)
        try:
            select = Select(self.driver.find_element(by, locator))
            selected_text = select.first_selected_option.text
        except TimeoutException:
            assert False, "Locator " + str(locator) + "not found"
        else:
            return str(selected_text)

    # author : venugopal
    # since : 2021-08-10
    # this method is to click refresh
    # argument :
    # return :
    def refresh_browser(self):
        self.driver.refresh()
        #WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_user_role_xpath))))
        time.sleep(20)

    # author : venugopal
    # since : 2021-08-10
    # this method is to select drop down
    # argument : by , locator and value
    # return :
    def select(self, by, locator, value):
        by_locator = (by, locator)
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))
            Select(self.driver.find_element(by, locator)).select_by_visible_text(value)
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        except ElementClickInterceptedException:
            assert False, "Locator " + str(by_locator) + "not click able"

    # author : venugopal
    # since : 2021-08-10
    # this method is get random
    # argument :
    # return : number
    @staticmethod
    def generate_random_number():
        number = datetime.datetime.now()
        random_number = number.strftime("%m%d%Y%H%M%S")
        return str(random_number)

    # author : venugopal
    # since : 2021-08-10
    # this method is get username
    # argument :
    # return : username
    @staticmethod
    def get_user_name():
        user_name = getpass.getuser()
        return user_name

    # author : venugopal
    # since : 2021-08-10
    # this method is get attribute value of an element
    # argument :
    # return :
    def get_attribute_value(self, by_locator, attribute_name):
        try:
            value = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)) \
                .get_attribute(attribute_name)
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        else:
            return value.strip()

    # author : venugopal
    # since : 2021-08-10
    # this method is get rows count of the table
    # argument :
    # return : row_count
    def get_no_of_rows_of_table(self, locator):
        row_count = len(self.driver.find_elements_by_xpath(locator))
        return row_count

    # author : venugopal
    # since : 2021-08-10
    # this method is get column count of the table
    # argument :
    # return : column_count
    def get_no_of_columns_of_table(self, locator):
        column_count = len(self.driver.find_elements_by_xpath(locator))
        return column_count

    # author : venugopal
    # since : 2021-08-10
    # this method is switch to view frame
    # argument :
    # return :
    def switch_to_view_frame(self):
        self.driver.switch_to.frame("view")

    # author : venugopal
    # since : 2021-08-10
    # this method is switch to view frame
    # argument :
    # return :
    def switch_to_buttons_frame(self):
        self.driver.switch_to.frame("buttons")

    # author : venugopal
    # since : 2021-08-10
    # this method is switch to view frame
    # argument :
    # return :
    def switch_to_issuedetails_frame(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("issuedetails-frame-iframe")

    # author : venugopal
    # since : 2021-08-10
    # this method is switch to view frame
    # argument :
    # return :
    def accept_alert(self):
        WebDriverWait(self.driver, 30).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    # author : venugopal
    # since : 2021-08-10
    # this method is to deselect drop down
    # argument : by , locator
    # return :
    def deselect(self, by, locator):
        by_locator = (by, locator)
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))
            Select(self.driver.find_element(by, locator)).deselect_all()
        except TimeoutException:
            assert False, "Locator " + str(by_locator) + "not found"
        except ElementClickInterceptedException:
            assert False, "Locator " + str(by_locator) + "not click able"

    # author : ankush
    # since : 2022-01-117
    # this method is to switch to child window
    # argument : parent_window
    # return :
    def switch_to_child_window(self, parent_window):
        child_windows = self.driver.window_handles
        for child in child_windows:
            if parent_window != child:
                self.driver.switch_to.window(child)
            else:
                assert "Window not found"
