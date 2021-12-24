import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.browserUtilis import BrowserUtilities
from pathlib import Path


class ReleasePage:
    # ---------------------------locator identifier----------------------------
    text_title_id = "F11160"
    button_ok_id = "formbtns_ok"
    button_close_xpath = "//*[@id='issuedetails']/diFv[1]/div/button"
    button_cancel_xpath = "//input[@id='formbtns_cancel']"
    button_update_id = "TransitionId_4060"
    button_upload_xpath = "//Button[text()='Upload & Attach AKV (.csv file)']"
    link_workarea_xpath = "//a[text()='Workarea']"
    textbox_description_xpath = "//textarea[@id='F11203']"
    textbox_v8_release_date_xpath = "//*[@id='F13445']"
    textbox_v8_xpath = "//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[2]"
    button_search_v8_name_xpath =   "//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v8_user_id = "F12646_LEFT"
    button_select_v8_xpath = "//*[@id='F12646.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_project_write_access_user_xpath = "//*[@id='F12645.wrapper']/div/table/tbody/tr[1]/td/input[2]"
    button_search_project_write_access_user_xpath = "//*[@id='F12645.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_project_write_access_user_id = "F12645_LEFT"
    button_select_project_write_access_user_xpath = "//*[@id='F12645.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    button_care_akv_varient_xpath = "//*[@id='Button18']"
    dropdown_care_group_xpath = "//*[@id='F13691']"
    button_import_AKV_from_CSV_xpath = "//button[text()='Import AKV from CSV and Start Confirmation...']"
    textbox_search_care_akv_varient_xpath = "//*[@id='F13688.wrapper']/div/table/tbody/tr[1]/td/input[2]"
    button_search_care_akv_varient_class = "//*[@id='F13688.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    listbox_care_akv_varient_xpath = "//*[@id='F13688']"
    link_upload_a2l_data_linktext = "Upload A2L Data"
    button_care_akv_varient_for_a2l_data_xpath = "//*[@id='Button20']"
    textbox_search_care_akv_varient_for_a2l_data_xpath = "//*[@id='mrx2table']/tbody/tr[1]/th[3]/div/input"
    checkbox_care_akv_varient_for_a2l_data_xpath = "//*[@id='mrx2table']/tbody/tr[4]/td[1]/input"
    textbox_comment_id = "a2luploadcomment"
    a2l_file_upload_xpath = "//*[@id='52d5fc10-c876-4ba2-a7b6-1f44133dd5a9']/div[3]/input[2]"
    button_select_a2l_data_xpath = "//*[@id='Button19']"
    textbox_search_user_comment_xpath = "//*[@id='mrx2table']/tbody/tr[1]/th[3]/div/input"
    radiobutton_a2l_data_xpath = "//*[@id='mrx2table']/tbody/tr[2]/td[1]/input"
    button_precheck_care_and_a2l_data_xpath = "//*[@id='Button22']"

    def __init__(self, driver):
        self.driver = driver
        self.bu = BrowserUtilities(driver)

    # author : ankush
    # since : 2021-12-03
    # this method is to set tile
    # argument :
    # return :
    def set_title(self, title_name):
        self.bu.send_keys((By.ID, self.text_title_id), title_name)

    # author : ankush
    # since : 2021-12-03
    # this method is click ok
    # argument :
    # return :
    def click_ok(self):
        self.bu.click((By.ID, self.button_ok_id))

    # author : ankush
    # since : 2021-12-03
    # this method is to close
    # argument :
    # return :
    def click_close(self):
        self.bu.click((By.XPATH, self.button_close_xpath))
        self.driver.switch_to.parent_frame()

    # author : ankush
    # since : 2021-12-03
    # this method is to cancel
    # argument :
    # return :
    def click_cancel(self):
        self.bu.click((By.XPATH, self.button_cancel_xpath))

    # author : ankush
    # since : 2021-12-06
    # this method is to set tile
    # argument :
    # return :
    def click_update(self):
        self.bu.click((By.ID, self.button_update_id))

    # author : ankush
    # since : 2021-12-06
    # this method is to click on Upload button
    # argument :
    # return :
    def click_CSV_upload(self):
        self.bu.click((By.XPATH, self.button_upload_xpath))

    # author : ankush
    # since : 2021-12-06
    # this method is to click on Workarea link
    # argument :
    # return :
    def click_workarea(self):
        self.bu.click((By.XPATH, self.link_workarea_xpath))

    # author : ankush
    # since : 2021-12-06
    # this method is to set description
    # argument :
    # return :
    def set_description(self, description):
        self.bu.send_keys((By.XPATH, self.textbox_description_xpath), description)

    # author : ankush
    # since : 2021-12-07
    # this method is to set date
    # argument :
    # return :
    def set_release_date(self, date):
        self.bu.send_keys((By.XPATH, self.textbox_v8_release_date_xpath), date)

    # author : ankush
    # since : 2021-12-07
    # this method is select V8
    # argument : v8 user need to select
    # return :
    def select_v8(self, v8):
        self.bu.send_keys((By.XPATH, self.textbox_v8_xpath), v8)
        self.bu.click((By.XPATH, self.button_search_v8_name_xpath))
        self.bu.select(By.ID, self.dropdown_v8_user_id, v8)
        self.bu.click((By.XPATH, self.button_select_v8_xpath))

    # author : ankush
    # since : 2021-12-09
    # this method is select project write access user
    # argument : project write access user need to select
    # return :
    def select_project_write_access(self, project_write_access_user):
        self.bu.send_keys((By.XPATH, self.textbox_project_write_access_user_xpath), project_write_access_user)
        self.bu.click((By.XPATH, self.button_search_project_write_access_user_xpath))
        self.bu.select(By.ID, self.dropdown_project_write_access_user_id, project_write_access_user)
        self.bu.click((By.XPATH, self.button_select_project_write_access_user_xpath))

    # author : ankush
    # since : 2021-12-09
    # this method is use to create release with all fields
    # argument : title, description, date, v8 user, project write access user
    # return :
    def fill_all_information(self, title, description, date, v8_user, project_write_access_user):
        self.set_title(title)
        self.set_description(description)
        self.set_release_date(date)
        self.select_v8(v8_user)
        self.select_project_write_access(project_write_access_user)

    # author : ankush
    # since : 2021-12-16
    # this method is use to create release with all fields
    # argument : title, description, date, v8 user, project write access user
    # return :
    def create_release(self, title, description, date, v8_user, project_write_access_user):
        self.set_title(title)
        self.set_description(description)
        self.set_release_date(date)
        self.select_v8(v8_user)
        self.select_project_write_access(project_write_access_user)
        self.click_ok()
        if self.bu.is_displayed((By.ID, 'itemID')):
            text = self.bu.get_text((By.ID, 'itemID'))
            return text.replace(":", "").strip()
        else:
            assert False, "Release creation unsuccessful. Task ID not displayed"

    # author : ankush
    # since : 2021-12-16
    # this method is use to update release with all fields
    # argument : title, description, date, v8 user, project write access user
    # return :
    def update_release(self, new_title, new_description, new_date, new_v8_user, new_project_write_access_user):
        self.set_title(new_title)
        self.set_description(new_description)
        self.set_release_date(new_date)
        self.select_v8(new_v8_user)
        self.select_project_write_access(new_project_write_access_user)

    # author : ankush
    # since : 2021-12-09
    # this method is use to click care akv varient
    # argument : select care group from drop down
    # return :
    def click_care_akv_variant(self):
        self.click_workarea()
        self.bu.click((By.XPATH, self.button_care_akv_varient_xpath))

    # author : ankush
    # since : 2021-12-09
    # this method is use to select care Group
    # argument : select care group from drop down
    # return :
    def select_care_group(self, care_group):
        self.bu.select(By.XPATH, self.dropdown_care_group_xpath, care_group)

    # author : ankush
    # since : 2021-12-09
    # this method is select care akv varient
    # argument : select care akv varient
    # return :
    def select_care_akv_variant(self, care_akv_variant):
        self.bu.send_keys((By.XPATH, self.textbox_search_care_akv_varient_xpath), care_akv_variant)
        self.bu.click((By.XPATH, self.button_search_care_akv_varient_class))
        self.bu.select(By.XPATH, self.listbox_care_akv_varient_xpath, care_akv_variant)

    # author : ankush
    # since : 2021-12-15
    # this method is select care akv variant for a2l data
    # argument : select care akv variant for a2l data
    # return :
    def select_care_akv_variant_for_a2l_data(self, care_akv_variant):
        self.bu.click((By.LINK_TEXT, self.link_upload_a2l_data_linktext))
        self.bu.click((By.XPATH, self.button_care_akv_varient_for_a2l_data_xpath))
        self.bu.send_keys((By.XPATH, self.textbox_search_care_akv_varient_for_a2l_data_xpath), care_akv_variant)
        if self.bu.is_selected((By.XPATH, self.checkbox_care_akv_varient_for_a2l_data_xpath)):
            pass
        else:
            self.bu.click((By.XPATH, self.checkbox_care_akv_varient_for_a2l_data_xpath))

    # author : ankush
    # since : 2021-12-21
    # this method is select care akv variant for a2l data and click on ok
    # argument : select care akv variant for a2l data
    # return :
    def search_and_select_care_akv_variant_for_a2l_data(self, care_akv_variant):
        self.bu.click((By.LINK_TEXT, self.link_upload_a2l_data_linktext))
        self.bu.click((By.XPATH, self.button_care_akv_varient_for_a2l_data_xpath))
        self.bu.send_keys((By.XPATH, self.textbox_search_care_akv_varient_for_a2l_data_xpath), care_akv_variant)
        if self.bu.is_selected((By.XPATH, self.checkbox_care_akv_varient_for_a2l_data_xpath)):
            pass
        else:
            self.bu.click((By.XPATH, self.checkbox_care_akv_varient_for_a2l_data_xpath))
        self.click_ok()

        if self.bu.is_displayed((By.ID, 'F14155')):
            text = self.bu.get_text((By.ID, 'F14155'))
            return text
        else:
            assert False, "Care akv Variant for a2l data data selection unsuccessful. care akv variant not displayed"

    # author : ankush
    # since : 2021-12-15
    # this method is use to  add comment
    # argument : add comment
    # return :
    def set_comment(self, upload_comment):
        self.bu.send_keys((By.ID, self.textbox_comment_id), upload_comment)

    # author : ankush
    # since : 2021-12-15
    # this method is use to upload a2l file
    # argument :
    # return :
    def upload_a2l_data(self, a2l_file_path):
        self.bu.send_keys((By.XPATH, self.a2l_file_upload_xpath), a2l_file_path)
        time.sleep(8)

    # author : ankush
    # since : 2021-12-23
    # this method is use to upload a2l file
    # argument :
    # return :
    def set_care_akv_variant(self, care_group, care_akv_variant):
        self.click_care_akv_variant()
        self.select_care_group(care_group)
        self.select_care_akv_variant(care_akv_variant)
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='F13688']")):
            text = self.bu.get_text((By.XPATH, "//*[@id='F13688']"))
            return text
        else:
            assert False, "Care AKV Variant selection unsuccessful. Care AKV Variant is not displayed"

    # author : ankush
    # since : 2021-12-23
    # this method is use to click on a2l data button
    # argument :
    # return :
    def click_a2l_data(self):
        self.bu.click((By.XPATH, self.button_select_a2l_data_xpath))

    # author : ankush
    # since : 2021-12-23
    # this method is use to select existing a2l data from list(based on filtering user comment selecting a2l file)
    # argument :
    # return :
    def select_a2l_data_from_list(self, user_comment):
        self.bu.send_keys((By.XPATH, self.textbox_search_user_comment_xpath), user_comment)
        if self.bu.is_selected((By.XPATH, self.radiobutton_a2l_data_xpath)):
            pass
        else:
            self.bu.click((By.XPATH, self.radiobutton_a2l_data_xpath))

    # author : ankush
    # since : 2021-12-24
    # this method is use to select existing a2l data(based on filtering user comment selecting a2l file)
    # argument :
    # return :
    def select_a2l_data(self, user_comment):
        self.click_a2l_data()
        self.select_a2l_data_from_list(user_comment)
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='F14154']")):
            text = self.bu.get_text((By.XPATH, "//*[@id='F14154']"))
            return text
        else:
            assert False, "a2l data selection unsuccessful. a2l file is not displayed"

    # author : ankush
    # since : 2021-12-24
    # this method is use to select existing a2l data(based on filtering user comment selecting a2l file)
    # argument :
    # return :
    def click_precheck_care_and_a2l_data(self):
        self.bu.click((By.XPATH, self.button_precheck_care_and_a2l_data_xpath))


