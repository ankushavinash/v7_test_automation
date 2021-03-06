import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.browserUtilis import BrowserUtilities


class ReleasePage:
    # ---------------------------locator identifier----------------------------
    text_title_id = "F11160"
    button_ok_id = "formbtns_ok"
    button_close_xpath = "//*[@id='issuedetails']/div[1]/div/button"
    button_cancel_xpath = "//input[@id='formbtns_cancel']"
    button_update_id = "TransitionId_4060"
    button_upload_xpath = "//Button[text()='Upload & Attach AKV (.csv file)']"
    link_workarea_xpath = "//a[text()='Workarea']"
    textbox_description_xpath = "//textarea[@id='F11203']"
    textbox_v8_release_date_xpath = "//*[@id='F13445']"
    textbox_v8_xpath = "//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[2]"
    button_search_v8_name_xpath = "//*[@id='F12646.wrapper']/div/table/tbody/tr[1]/td/input[1]"
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
    checkbox_care_akv_varient_for_a2l_data_xpath = "//*[@id='mrx2table']/tbody/tr[137]/td[1]/input"
    textbox_comment_id = "a2luploadcomment"
    a2l_file_upload_id = "a2ldropzone"
    button_select_a2l_data_xpath = "//*[@id='Button19']"
    textbox_search_user_comment_xpath = "//*[@id='mrx2table']/tbody/tr[1]/th[3]/div/input"
    radiobutton_a2l_data_xpath = "//*[@id='mrx2table']/tbody/tr[266]/td[1]/input"
    radiobutton_a2l_data_without_q_group_xpath = "//*[@id='mrx2table']/tbody/tr[399]/td[1]/input"
    button_precheck_care_and_a2l_data_xpath = "//*[@id='Button22']"
    textbox_internal_comment_id = "H11204"
    textbox_release_letter_comment_xpath = "//*[@id='F14387']"
    button_import_akv_from_care_and_start_confirmation_xpath = "//*[@id='Button14']"
    checkbox_override_v8_id = "SELECT_F13842"
    link_child_confirmation_linktext = "Child Confirmations"
    button_discard_complete_confirmation_id = "TransitionId_4065"
    button_v4_user_confirm_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[6]/span[1]"
    button_confirmation_button_id = "ConfirmationButton"
    # link_User_confirmation_record_v4_user_xpath = "//*[@id='ReportOutput']/tbody/tr[3]/td[2]/span/a"
    link_User_confirmation_record_v4_user_xpath = "//table[@id='ReportOutput']/tbody//span[contains(text(), 'v7_automation_v4_user')]/../../td[2]//a"
    button_discard_id = "TransitionId_4061"
    button_v4_user_reject_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[6]/span[2]"
    button_v8_confirmation_id = "TransitionId_4063"
    button_v8_rejection_id = "TransitionId_4064"
    # link_User_confirmation_record_v5_user_xpath = "//*[@id='ReportOutput']/tbody/tr[4]/td[2]/span/a"
    link_User_confirmation_record_v5_user_xpath = "//table[@id='ReportOutput']/tbody//span[contains(text(), 'v7_automation_v5_user')]/../../td[2]//a"
    button_v5_user_confirm_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[7]/span[1]"
    button_v5_user_reject_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[7]/span[2]"
    checkbox_override_id = "SELECT_F12585"
    button_accept_tick_xpath = "//*[@id='ucmatrix']/tbody/tr[2]/td[7]/p[1]/span[1]"
    # link_User_confirmation_record_v6_user_xpath = "//*[@id='ReportOutput']/tbody/tr[5]/td[2]/span/a"
    link_User_confirmation_record_v6_user_xpath = "//table[@id='ReportOutput']/tbody//span[contains(text(), 'v7_automation_v6_user')]/../../td[2]//a"
    button_v6_user_confirm_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[8]/span[1]"
    button_v6_accept_tick_xpath = "//*[@id='ucmatrix']/tbody/tr[2]/td[8]/p[1]/span[1]"
    button_v6_user_all_part_modules_reject_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[8]/span[1]"
    button_v6_first_part_module_reject_tick_xpath = "//*[@id='ucmatrix']/tbody/tr[2]/td[8]/p[1]/span[2]"
    # link_User_confirmation_record_v7_user_xpath = "//*[@id='ReportOutput']/tbody/tr[6]/td[2]/span/a"
    link_User_confirmation_record_v7_user_xpath = "//table[@id='ReportOutput']/tbody//span[contains(text(), 'v7_automation_v7_user')]/../../td[2]//a"
    button_v7_user_all_part_modules_accept_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[9]/span[1]"
    button_v7_first_part_module_accept_tick_button_xpath = "//*[@id='ucmatrix']/tbody/tr[2]/td[9]/p[1]/span[1]"
    button_v7_user_all_part_modules_reject_button_xpath = "//*[@id='ucmatrix']/tbody/tr[1]/th[9]/span[2]"
    button_v7_first_part_module_reject_tick_xpath = "//*[@id='ucmatrix']/tbody/tr[2]/td[9]/p[1]/span[2]"
    button_final_v8_confirmation_id = "TransitionId_4030"
    button_final_v8_rejection_id = "TransitionId_4031"
    link_first_module_xpath = "//a[@title= 'A0 (1.0.0)']"
    button_confirm_id = "TransitionId_3580"
    button_reject_id = "TransitionId_3581"
    textbox_reject_comment_v4_user_id = "F11865"
    button_confirm_v5_user_id = "TransitionId_3582"
    button_reject_v5_user_id = "TransitionId_3589"
    textbox_reject_comment_v5_user_id = "F11866"
    button_confirm_v6_user_id = "TransitionId_3583"
    button_reject_v6_user_id = "TransitionId_3591"
    textbox_reject_comment_v6_user_id = "F11867"
    button_confirm_v7_user_id = "TransitionId_3586"
    button_reject_v7_user_id = "TransitionId_3593"
    textbox_reject_comment_v7_user_id = "F11868"
    textbox_v4_primary_name = "G11178_LEFT"
    button_search_v4_primary_xpath = "//*[@id='F11178.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v4_primary_id = "F11178_LEFT"
    button_select_v4_primary_xpath = "//*[@id='F11178.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_v5_primary_name = "G11181_LEFT"
    button_search_v5_primary_xpath = "//*[@id='F11181.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v5_primary_id = "F11181_LEFT"
    button_select_v5_primary_xpath = "//*[@id='F11181.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_v6_primary_name = "G11184_LEFT"
    button_search_v6_primary_xpath = "//*[@id='F11184.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v6_primary_id = "F11184_LEFT"
    button_select_v6_primary_xpath = "//*[@id='F11184.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_v7_primary_name = "G11187_LEFT"
    button_search_v7_primary_xpath = "//*[@id='F11187.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v7_primary_id = "F11187_LEFT"
    button_select_v7_primary_xpath = "//*[@id='F11187.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_v4_fallback_name = "G11176_LEFT"
    button_search_v4_fallback_xpath = "//*[@id='F11176.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v4_fallback_id = "F11176_LEFT"
    button_select_v4_fallback_xpath = "//*[@id='F11176.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_v5_fallback_name = "G11179_LEFT"
    button_search_v5_fallback_xpath = "//*[@id='F11179.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v5_fallback_id = "F11179_LEFT"
    button_select_v5_fallback_xpath = "//*[@id='F11179.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_v6_fallback_name = "G11182_LEFT"
    button_search_v6_fallback_xpath = "//*[@id='F11182.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v6_fallback_id = "F11182_LEFT"
    button_select_v6_fallback_xpath = "//*[@id='F11182.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    textbox_v7_fallback_name = "G11185_LEFT"
    button_search_v7_fallback_xpath = "//*[@id='F11185.wrapper']/div/table/tbody/tr[1]/td/input[1]"
    dropdown_v7_fallback_id = "F11185_LEFT"
    button_select_v7_fallback_xpath = "//*[@id='F11185.wrapper']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/a"
    link_first_part_module_xpath = "//a[@title='A0 (1.0.0)']"
    button_refresh_id = "refresh_view"
    checkbox_accept_module_without_q_group_id = "SELECT_F13877"
    button_admin_update_responsibility_id = "TransitionId_5345"

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
        self.bu.send_keys((By.ID, self.a2l_file_upload_id), a2l_file_path)
        time.sleep(15)

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

    # author : ankush
    # since : 2021-12-28
    # this method is use to click on discard button
    # argument :
    # return :
    def click_discard(self):
        self.bu.click((By.ID, self.button_discard_id))

    # author : ankush
    # since : 2021-12-28
    # this method is use to set release letter comment
    # argument :
    # return :
    def set_release_letter_comment(self, release_letter_comment):
        self.bu.send_keys((By.XPATH, self.textbox_release_letter_comment_xpath), release_letter_comment)

    # author : ankush
    # since : 2021-12-28
    # this method is use to set release letter comment
    # argument :
    # return :
    def set_internal_comment(self, internal_comment):
        self.bu.send_keys((By.ID, self.textbox_internal_comment_id), internal_comment)

    # author : ankush
    # since : 2022-01-04
    # this method is use to precheck care and a2l data
    # argument :
    # return : precheck care a2l data
    def click_precheck_care_a2l_data(self):
        self.bu.click((By.XPATH, self.button_precheck_care_and_a2l_data_xpath))
        if self.bu.is_displayed((By.XPATH, "//*[@id='v7rpcc']/table/tbody/tr[1]/th[1]")):
            text = self.bu.get_text((By.XPATH, "//*[@id='v7rpcc']/table/tbody/tr[1]/th[1]"))
            return text
        else:
            assert False, "a2l file selection unsuccessful. a2l data is not displayed"

    # author : ankush
    # since : 2022-01-04
    # this method is use to click on import AKV from care and start confirmation while overriding v8
    # argument :
    # return :
    def click_import_akv_from_care_and_start_confirmation(self):
        self.click_ok()
        self.bu.click((By.XPATH, self.button_import_akv_from_care_and_start_confirmation_xpath))
        self.click_ok()

    # author : ankush
    # since : 2021-12-06
    # this method is to click on child confirmation link
    # argument :
    # return :
    def click_child_confirmation(self):
        self.bu.click((By.LINK_TEXT, self.link_child_confirmation_linktext))

    # author : ankush
    # since : 2022-01-04
    # this method is use to click on import AKV from care and start confirmation while overriding v8
    # argument :
    # return :
    def click_import_akv_from_care_and_start_confirmation_(self):
        self.click_ok()
        self.bu.click((By.XPATH, self.button_import_akv_from_care_and_start_confirmation_xpath))
        self.click_ok()
        if self.bu.is_displayed((By.ID, "F11170")):
            text = self.bu.get_text((By.ID, "F11170"))
            return text
        else:
            assert False, "import AKV from care is unsuccessful. import unsuccessful"

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on discard button
    # argument :
    # return :
    def click_discard_complete_confirmation(self):
        self.bu.click((By.ID, self.button_discard_complete_confirmation_id))

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  v4 user confirmation project as v4 user
    # argument :
    # return :
    def click_user_confirmation_project_v4_user(self):
        parent_window = self.driver.current_window_handle
        self.driver.switch_to.frame("4ea6d89b-d573-4aa9-bfe5-1209284765c4")
        self.bu.click((By.XPATH, self.link_User_confirmation_record_v4_user_xpath))
        self.bu.switch_to_child_window(parent_window)

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  confirmation button
    # argument :
    # return :
    def click_confirmation_or_reject_button(self):
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_confirmation_button_id))

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  confirmation button of modules as v4 user
    # argument :
    # return :
    def confirm_part_modules_as_v4_user(self):
        by_locator = (By.XPATH, self.button_v4_user_confirm_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v4_user_confirm_button_xpath))
                assert True, "V4 Confirmation button displayed"
        except TimeoutException:
            assert False, "V4 Confirmation button not displayed"

    # author : ankush
    # since : 2022-01-18
    # this method is use to confirm module as v4 user
    # argument :
    # return :
    def user_confirmation_as_v4_user(self):
        self.click_child_confirmation()
        self.click_user_confirmation_project_v4_user()
        self.click_confirmation_or_reject_button()
        self.confirm_part_modules_as_v4_user()
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[6]/p[2]")):
            text = self.bu.get_text((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[6]/p[2]"))
            v4_user_validation = text.replace("[v7_automation_v4_user]", "").strip()
            return v4_user_validation
        else:
            assert False, "confirm release as v4 user unsuccessful."

    # author : ankush
    # since : 2022-01-18
    # this method is use to discard confirmation as v4 user
    # argument :
    # return :
    def discard_complete_confirmation(self, release_letter_comment, internal_comment):
        self.click_discard_complete_confirmation()
        self.set_release_letter_comment(release_letter_comment)
        self.set_internal_comment(internal_comment)
        self.click_ok()

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  confirmation button
    # argument :
    # return :
    def click_reject_button(self):
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_confirmation_button_id))

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  confirmation button of modules as v4 user
    # argument :
    # return :
    def reject_part_modules_as_v4_user(self):
        by_locator = (By.XPATH, self.button_v4_user_reject_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v4_user_reject_button_xpath))
                assert True, "V4 reject button displayed"
        except TimeoutException:
            assert False, "V4 reject button not displayed"

    # author : ankush
    # since : 2022-01-20
    # this method is use to confirm release as v8 user
    # argument :
    # return :
    def confirm_release_as_v8_user(self, internal_comment):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_v8_confirmation_id))
        self.set_internal_comment(internal_comment)
        self.click_ok()

    # author : ankush
    # since : 2022-01-20
    # this method is use to reject release as v8 user
    # argument : release letter comment and internal comment
    # return :
    def reject_release_as_v8_user(self, release_letter_comment, internal_comment):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_v8_rejection_id))
        self.set_release_letter_comment(release_letter_comment)
        self.set_internal_comment(internal_comment)
        self.click_ok()

    # author : ankush
    # since : 2022-01-27
    # this method is to close icon
    # argument :
    # return :
    def click_close_icon(self):
        self.driver.switch_to.default_content()
        self.bu.click((By.XPATH, self.button_close_xpath))

    # author : ankush
    # since : 2022-01-27
    # this method is use to discard confirmation as v8 user
    # argument :
    # return :
    def discard_complete_confirmation_as_v8_user(self, release_letter_comment, internal_comment):
        self.driver.switch_to.frame("issuedetails-frame")
        self.click_discard_complete_confirmation()
        self.set_release_letter_comment(release_letter_comment)
        self.set_internal_comment(internal_comment)
        self.click_ok()

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  v4 user confirmation project as v4 user
    # argument :
    # return :
    def click_user_confirmation_project_v5_user(self):
        parent_window = self.driver.current_window_handle
        self.driver.switch_to.frame("4ea6d89b-d573-4aa9-bfe5-1209284765c4")
        self.bu.click((By.XPATH, self.link_User_confirmation_record_v5_user_xpath))
        self.bu.switch_to_child_window(parent_window)

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  confirmation button of part modules as v5 user
    # argument :
    # return :
    def confirm_part_modules_as_v5_user_override_v4(self):
        by_locator = (By.XPATH, self.button_v5_user_confirm_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.ID, self.checkbox_override_id))
                by_tick = (By.XPATH, self.button_accept_tick_xpath)
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_tick))
                self.bu.click((By.XPATH, self.button_v5_user_confirm_button_xpath))
                assert True, "V5 Confirmation button displayed"
        except TimeoutException:
            assert False, "V5 Confirmation button not displayed"

    # author : ankush
    # since : 2022-01-27
    # this method is use to click on  reject button of part modules as v5 user
    # argument :
    # return :
    def reject_part_modules_as_v5_user_override_v4(self):
        by_locator = (By.XPATH, self.button_v5_user_reject_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                # click on override
                self.bu.click((By.ID, self.checkbox_override_id))
                by_tick = (By.XPATH, self.button_accept_tick_xpath)
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_tick))
                self.bu.click((By.XPATH, self.button_v5_user_reject_button_xpath))
                assert True, "V5 reject button displayed"
        except TimeoutException:
            assert False, "V5 reject button not displayed"

    # author : ankush
    # since : 2022-01-28
    # this method is use for user confirmation as v5 user by overriding v4 user
    # argument :
    # return :
    def user_confirmation_as_v5_user_override_v4(self):
        self.click_child_confirmation()
        self.click_user_confirmation_project_v5_user()
        self.click_confirmation_or_reject_button()
        self.confirm_part_modules_as_v5_user_override_v4()
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[7]/p[2]")):
            text = self.bu.get_text((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[7]/p[2]"))
            v5_user_validation = text.replace("[v7_automation_v5_user]", "").strip()
            return v5_user_validation
        else:
            assert False, "confirm release as v5 user unsuccessful."

    # author : ankush
    # since : 2022-01-28
    # this method is use to click on  confirmation button of part modules as v5 user
    # argument :
    # return :
    def confirm_part_modules_as_v5_user(self):
        by_locator = (By.XPATH, self.button_v5_user_confirm_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v5_user_confirm_button_xpath))
                assert True, "V5 Confirmation button displayed"
        except TimeoutException:
            assert False, "V5 Confirmation button not displayed"

    # author : ankush
    # since : 2022-01-28
    # this method is use to confirm module as v5 user
    # argument :
    # return :
    def user_confirmation_as_v5_user(self):
        self.click_child_confirmation()
        self.click_user_confirmation_project_v5_user()
        self.click_confirmation_or_reject_button()
        self.confirm_part_modules_as_v5_user()
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[7]/p[2]")):
            text = self.bu.get_text((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[7]/p[2]"))
            return text
        else:
            assert False, "confirm release as v5 user unsuccessful."

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  reject button of part modules as v5 user
    # argument :
    # return :
    def reject_part_modules_as_v5_user(self):
        by_locator = (By.XPATH, self.button_v5_user_reject_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v5_user_reject_button_xpath))
                assert True, "V5 reject button displayed"
        except TimeoutException:
            assert False, "V5 reject button not displayed"

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  v6 user confirmation project as v6 user
    # argument :
    # return :
    def click_user_confirmation_project_v6_user(self):
        parent_window = self.driver.current_window_handle
        self.driver.switch_to.frame("4ea6d89b-d573-4aa9-bfe5-1209284765c4")
        self.bu.click((By.XPATH, self.link_User_confirmation_record_v6_user_xpath))
        self.bu.switch_to_child_window(parent_window)

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  confirmation button of part modules as v6 user
    # argument :
    # return :
    def confirm_part_modules_as_v6_user_override_v4_and_v5(self):
        by_locator = (By.XPATH, self.button_v6_user_confirm_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.ID, self.checkbox_override_id))
                by_tick = (By.XPATH, self.button_v6_accept_tick_xpath)
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_tick))
                self.bu.click((By.XPATH, self.button_v6_user_confirm_button_xpath))
                assert True, "V6 Confirmation button displayed"
        except TimeoutException:
            assert False, "V6 Confirmation button not displayed"

    # author : ankush
    # since : 2022-01-31
    # this method is use to click on  reject button of part modules as v6 user
    # argument :
    # return :
    def reject_part_modules_as_v6_user_override_v4_and_v5(self):
        by_locator = (By.XPATH, self.button_v6_user_all_part_modules_reject_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                # click on override
                self.bu.click((By.ID, self.checkbox_override_id))
                by_tick = (By.XPATH, self.button_v6_first_part_module_reject_tick_xpath)
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_tick))
                self.bu.click((By.XPATH, self.button_v6_user_all_part_modules_reject_button_xpath))
                assert True, "V6 reject button displayed"
        except TimeoutException:
            assert False, "V6 reject button not displayed"

    # author : ankush
    # since : 2022-01-31
    # this method is use for user confirmation as 65 user by overriding v4 user and V5 user
    # argument :
    # return :
    def user_confirmation_as_v6_user_override_v4_and_v5(self):
        self.click_child_confirmation()
        self.click_user_confirmation_project_v6_user()
        self.click_confirmation_or_reject_button()
        self.confirm_part_modules_as_v6_user_override_v4_and_v5()
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[8]/p[2]")):
            text = self.bu.get_text((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[8]/p[2]"))
            v7_user_validation = text.replace("[v7_automation_v6_user]", "").strip()
            return v7_user_validation
        else:
            assert False, "confirm release as v6 user unsuccessful."

    # author : ankush
    # since : 2022-01-31
    # this method is use to click on  v7 user confirmation project as v7 user
    # argument :
    # return :
    def click_user_confirmation_project_v7_user(self):
        parent_window = self.driver.current_window_handle
        self.driver.switch_to.frame("4ea6d89b-d573-4aa9-bfe5-1209284765c4")
        self.bu.click((By.XPATH, self.link_User_confirmation_record_v7_user_xpath))
        self.bu.switch_to_child_window(parent_window)

    # author : ankush
    # since : 2022-01-11
    # this method is use to click on  confirmation button of part modules as v7 user
    # argument :
    # return :
    def confirm_part_modules_as_v7_user_override_v4_v5_and_v6(self):
        by_locator = (By.XPATH, self.button_v7_user_all_part_modules_accept_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.ID, self.checkbox_override_id))
                by_tick = (By.XPATH, self.button_v7_first_part_module_accept_tick_button_xpath)
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_tick))
                self.bu.click((By.XPATH, self.button_v7_user_all_part_modules_accept_button_xpath))
                assert True, "V7 Confirmation button displayed"
        except TimeoutException:
            assert False, "V7 Confirmation button not displayed"

    # author : ankush
    # since : 2022-02-01
    # this method is use to click on reject button of all part modules as v7 user
    # argument :
    # return :
    def reject_part_modules_as_v7_user_override_v4_v5_and_v6_user(self):
        by_locator = (By.XPATH, self.button_v7_user_all_part_modules_reject_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                # click on override
                self.bu.click((By.ID, self.checkbox_override_id))
                by_tick = (By.XPATH, self.button_v7_first_part_module_reject_tick_xpath)
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_tick))
                self.bu.click((By.XPATH, self.button_v7_user_all_part_modules_reject_button_xpath))
                assert True, "V7 reject button displayed"
        except TimeoutException:
            assert False, "V7 reject button not displayed"

    # author : ankush
    # since : 2022-02-01
    # this method is use for user confirmation as v7 user by overriding v4 user and V5 user
    # argument :
    # return :
    def user_confirmation_as_v7_user_override_v4_v5_and_v6_user(self):
        self.click_child_confirmation()
        self.click_user_confirmation_project_v7_user()
        self.click_confirmation_or_reject_button()
        self.confirm_part_modules_as_v7_user_override_v4_v5_and_v6()
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[9]/p[2]")):
            text = self.bu.get_text((By.XPATH, "//*[@id='ucmatrix']/tbody/tr[2]/td[9]/p[2]"))
            v7_user_validation = text.replace("[v7_automation_v7_user]", "").strip()
            return v7_user_validation
        else:
            assert False, "confirm release as v7 user unsuccessful."

    # author : ankush
    # since : 2022-02-01
    # this method is use to confirm release as v8 user after v7 confirmation
    # argument : internal comment and release letter comment
    # return :
    def click_v8_confirmation(self, release_letter_comment, internal_comments):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_final_v8_confirmation_id))
        self.set_release_letter_comment(release_letter_comment)
        self.set_internal_comment(internal_comments)
        self.click_ok()

    # author : ankush
    # since : 2022-01-03
    # this method is use to reject release as v8 user after all confirmation
    # argument : release letter comment and internal comment
    # return :
    def click_v8_rejection(self, release_letter_comment, internal_comment):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_final_v8_rejection_id))
        self.set_release_letter_comment(release_letter_comment)
        self.set_internal_comment(internal_comment)
        self.click_ok()

    # author : ankush
    # since : 2022-01-03
    # this method is use to click on  confirmation button of part modules as v6 user
    # argument :
    # return :
    def confirm_part_modules_as_v6_user(self):
        by_locator = (By.XPATH, self.button_v6_user_confirm_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v6_user_confirm_button_xpath))
                assert True, "V6 Confirmation button displayed"
        except TimeoutException:
            assert False, "V6 Confirmation button not displayed"

    # author : ankush
    # since : 2022-02-04
    # this method is use to click on  reject button of part modules as v6 user
    # argument :
    # return :
    def reject_part_modules_as_v6_user(self):
        by_locator = (By.XPATH, self.button_v6_user_all_part_modules_reject_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v6_user_all_part_modules_reject_button_xpath))
                assert True, "V6 reject button displayed"
        except TimeoutException:
            assert False, "V6 reject button not displayed"

    # author : ankush
    # since : 2022-01-03
    # this method is use to click on  confirmation button of part modules as v7 user
    # argument :
    # return :
    def confirm_part_modules_as_v7_user(self):
        by_locator = (By.XPATH, self.button_v7_user_all_part_modules_accept_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v7_user_all_part_modules_accept_button_xpath))
                assert True, "V7 Confirmation button displayed"
        except TimeoutException:
            assert False, "V7 Confirmation button not displayed"

    # author : ankush
    # since : 2022-02-07
    # this method is use to click on  reject button of part modules as v6 user
    # argument :
    # return :
    def reject_part_modules_as_v7_user(self):
        by_locator = (By.XPATH, self.button_v7_user_all_part_modules_reject_button_xpath)
        try:
            if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)):
                self.bu.click((By.XPATH, self.button_v7_user_all_part_modules_reject_button_xpath))
                assert True, "V7 reject button displayed"
        except TimeoutException:
            assert False, "V7 reject button not displayed"

    # author : ankush
    # since : 2022-02-07
    # this method is use to clcik on first module to navigate to confirmation page
    # argument :
    # return :
    def click_module_confirmation(self):
        self.driver.switch_to.frame("d40aa4b3-f81d-4f82-b8bf-af6b57d91fa1")
        self.bu.click((By.XPATH, self.link_first_module_xpath))

    # author : ankush
    # since : 2022-02-07
    # this method is use to click on confirm
    # argument :
    # return :
    def click_confirm(self, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_confirm_id))

    # author : ankush
    # since : 2022-02-10
    # this method is use to reject module as v4 user
    # argument :
    # return :
    def click_reject_as_v4_user(self, reject_comment_v4_user, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_reject_id))
        self.bu.send_keys((By.ID, self.textbox_reject_comment_v4_user_id), reject_comment_v4_user)

    # author : ankush
    # since : 2022-02-10
    # this method is use to confirm module as v4 user
    # argument :
    # return :
    def module_confirmation_as_v4_user(self, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_confirm(main_window)
        self.click_ok()
        if self.bu.is_displayed((By.ID, "F11197")):
            text = self.bu.get_text((By.ID, "F11197"))
            self.driver.switch_to.parent_frame()
            return text
        else:
            assert False, "confirm module as v4 user unsuccessful."

    # author : ankush
    # since : 2022-02-10
    # this method is use to click on confirm
    # argument :
    # return :
    def click_confirm_as_v5_user(self, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_confirm_v5_user_id))

    # author : ankush
    # since : 2022-02-10
    # this method is use to reject module as v5 user
    # argument :
    # return :
    def click_reject_as_v5_user(self, reject_comment_v5_user, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_reject_v5_user_id))
        self.bu.send_keys((By.ID, self.textbox_reject_comment_v5_user_id), reject_comment_v5_user)

    # author : ankush
    # since : 2022-02-10
    # this method is use to click on confirm
    # argument :
    # return :
    def click_confirm_as_v6_user(self, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_confirm_v6_user_id))

    # author : ankush
    # since : 2022-02-12
    # this method is use to confirm module as v5 user
    # argument : main_window
    # return : status of confirmation
    def module_confirmation_as_v5_user(self, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_confirm_as_v5_user(main_window)
        self.click_ok()
        if self.bu.is_displayed((By.ID, "F11197")):
            text = self.bu.get_text((By.ID, "F11197"))
            self.driver.switch_to.parent_frame()
            return text
        else:
            assert False, "confirm module as v5 user unsuccessful."

    # author : ankush
    # since : 2022-02-11
    # this method is use to reject module as v6 user
    # argument :
    # return :
    def click_reject_as_v6_user(self, reject_comment_v6_user, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_reject_v6_user_id))
        self.bu.send_keys((By.ID, self.textbox_reject_comment_v6_user_id), reject_comment_v6_user)

    # author : ankush
    # since : 2022-02-12
    # this method is use to confirm module as v5 user
    # argument : main_window
    # return : status of confirmation
    def module_confirmation_as_v6_user(self, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_confirm_as_v6_user(main_window)
        self.click_ok()
        if self.bu.is_displayed((By.ID, "F11197")):
            text = self.bu.get_text((By.ID, "F11197"))
            self.driver.switch_to.parent_frame()
            return text
        else:
            assert False, "confirm module as v6 user unsuccessful."

    # author : ankush
    # since : 2022-02-11
    # this method is use to click on confirm
    # argument :
    # return :
    def click_confirm_as_v7_user(self, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_confirm_v7_user_id))

    # author : ankush
    # since : 2022-02-11
    # this method is use to reject module as v6 user
    # argument :
    # return :
    def click_reject_as_v7_user(self, reject_comment_v7_user, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_reject_v7_user_id))
        self.bu.send_keys((By.ID, self.textbox_reject_comment_v7_user_id), reject_comment_v7_user)

    # author : ankush
    # since : 2022-03-03
    # this method is use to confirm module as v7 user
    # argument : main_window
    # return : status of confirmation
    def module_confirmation_as_v7_user(self, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_confirm_as_v7_user(main_window)
        self.click_ok()
        if self.bu.is_displayed((By.ID, "F11197")):
            text = self.bu.get_text((By.ID, "F11197"))
            self.driver.switch_to.parent_frame()
            return text
        else:
            assert False, "confirm module as v7 user unsuccessful."

    # author : ankush
    # since : 2022-03-07
    # this method is use to confirm release as v8 user after v7 confirmation
    # argument : internal comment
    # return :
    button_v8_confirmation_after_other_confirmation_id = "TransitionId_4063"
    def final_v8_confirmation(self, internal_comments):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_v8_confirmation_after_other_confirmation_id))
        self.set_internal_comment(internal_comments)
        self.click_ok()

    # author : ankush
    # since : 2022-03-08
    # this method is use to reject release as v8 user after v7 confirmation
    # argument : release letter comment, internal comment
    # return :
    button_v8_rejection_after_all_confirmation_id = "TransitionId_4064"
    def final_v8_rejection(self, release_letter_comment, internal_comments):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_v8_rejection_after_all_confirmation_id))
        self.set_release_letter_comment(release_letter_comment)
        self.set_internal_comment(internal_comments)
        self.click_ok()

    # author : ankush
    # since : 2021-03-11
    # this method is use to select existing a2l data from list(based on filtering user comment selecting a2l file)
    # argument : user comment
    # return :
    def set_a2l_data_without_q_group(self, user_comment):
        self.bu.send_keys((By.XPATH, self.textbox_search_user_comment_xpath), user_comment)
        if self.bu.is_selected((By.XPATH, self.radiobutton_a2l_data_without_q_group_xpath)):
            pass
        else:
            self.bu.click((By.XPATH, self.radiobutton_a2l_data_without_q_group_xpath))

    # author : ankush
    # since : 2021-12-24
    # this method is use to select existing a2l data(based on filtering user comment selecting a2l file)
    # argument :
    # return :
    def select_a2l_data_without_q_group(self, user_comment):
        self.click_a2l_data()
        self.set_a2l_data_without_q_group(user_comment)
        self.click_ok()
        if self.bu.is_displayed((By.XPATH, "//*[@id='F14154']")):
            text = self.bu.get_text((By.XPATH, "//*[@id='F14154']"))
            return text
        else:
            assert False, "a2l data selection unsuccessful. a2l file is not displayed"

    # author : ankush
    # since : 2022-03-28
    # this method is use to get text for validation without q group
    # argument :
    # return : text for without q group validation
    def without_q_group_text_validation(self):
        time.sleep(10)
        if self.bu.is_displayed((By.XPATH, "//*[@id='v7rpcc']/pre")):
            text = self.bu.get_text((By.XPATH, "//*[@id='v7rpcc']/pre"))
            return text
        else:
            assert False, "Modules upload failed"

    # author : ankush
    # since : 2022-03-30
    # this method is use to get text for validation without q group
    # argument :
    # return : text for without q group validation
    def override_v8_assignment_and_start_confirmation(self):
        self.click_ok()
        self.bu.click((By.XPATH, self.button_import_akv_from_care_and_start_confirmation_xpath))
        self.bu.click((By.ID, self.checkbox_accept_module_without_q_group_id))
        self.click_ok()
        self.bu.click((By.XPATH, self.button_import_akv_from_care_and_start_confirmation_xpath))
        self.bu.click((By.ID, self.checkbox_override_v8_id))
        self.click_ok()

    # author : ankush
    # since : 2022-03-31
    # this method is use to click admin update responsibility button
    # argument :
    # return :
    def click_admin_update_responsibility(self):
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_admin_update_responsibility_id))




    # author : ankush
    # since : 2022-03-31
    # this method is to select v4 primary
    # argument : v4 primary user
    # return :
    def select_v4_primary(self, v4_primary):
        self.bu.send_keys((By.NAME, self.textbox_v4_primary_name), v4_primary)
        self.bu.click((By.XPATH, self.button_search_v4_primary_xpath))
        self.bu.select(By.ID, self.dropdown_v4_primary_id, v4_primary)
        self.bu.click((By.XPATH, self.button_select_v4_primary_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to select v5 primary
    # argument : v5 primary user
    # return :
    def select_v5_primary(self, v5_primary):
        self.bu.send_keys((By.NAME, self.textbox_v5_primary_name), v5_primary)
        self.bu.click((By.XPATH, self.button_search_v5_primary_xpath))
        self.bu.select(By.ID, self.dropdown_v5_primary_id, v5_primary)
        self.bu.click((By.XPATH, self.button_select_v5_primary_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to select v6 primary
    # argument : v6 primary user
    # return :
    def select_v6_primary(self, v6_primary):
        self.bu.send_keys((By.NAME, self.textbox_v6_primary_name), v6_primary)
        self.bu.click((By.XPATH, self.button_search_v6_primary_xpath))
        self.bu.select(By.ID, self.dropdown_v6_primary_id, v6_primary)
        self.bu.click((By.XPATH, self.button_select_v6_primary_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to select v7 primary
    # argument : v7 primary user
    # return :
    def select_v7_primary(self, v7_primary):
        self.bu.send_keys((By.NAME, self.textbox_v7_primary_name), v7_primary)
        self.bu.click((By.XPATH, self.button_search_v7_primary_xpath))
        self.bu.select(By.ID, self.dropdown_v7_primary_id, v7_primary)
        self.bu.click((By.XPATH, self.button_select_v7_primary_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to select v4 fallback
    # argument : v4 fallback user
    # return :
    def select_v4_fallback(self, v4_fallback):
        self.bu.send_keys((By.NAME, self.textbox_v4_fallback_name), v4_fallback)
        self.bu.click((By.XPATH, self.button_search_v4_fallback_xpath))
        self.bu.select(By.ID, self.dropdown_v4_fallback_id, v4_fallback)
        self.bu.click((By.XPATH, self.button_select_v4_fallback_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to select v5 fallback
    # argument : v5 fallback user
    # return :
    def select_v5_fallback(self, v5_fallback):
        self.bu.send_keys((By.NAME, self.textbox_v5_fallback_name), v5_fallback)
        self.bu.click((By.XPATH, self.button_search_v5_fallback_xpath))
        self.bu.select(By.ID, self.dropdown_v5_fallback_id, v5_fallback)
        self.bu.click((By.XPATH, self.button_select_v5_fallback_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to select v6 fallback
    # argument : v6 fallback user
    # return :
    def select_v6_fallback(self, v6_fallback):
        self.bu.send_keys((By.NAME, self.textbox_v6_fallback_name), v6_fallback)
        self.bu.click((By.XPATH, self.button_search_v6_fallback_xpath))
        self.bu.select(By.ID, self.dropdown_v6_fallback_id, v6_fallback)
        self.bu.click((By.XPATH, self.button_select_v6_fallback_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to select v7 fallback
    # argument : v7 fallback user
    # return :
    def select_v7_fallback(self, v7_fallback):
        self.bu.send_keys((By.NAME, self.textbox_v7_fallback_name), v7_fallback)
        self.bu.click((By.XPATH, self.button_search_v7_fallback_xpath))
        self.bu.select(By.ID, self.dropdown_v7_fallback_id, v7_fallback)
        self.bu.click((By.XPATH, self.button_select_v7_fallback_xpath))

    # author : ankush
    # since : 2022-03-31
    # this method is to fill all primary and fallback user of admin update responsibility
    # argument : fill all v4, v5, v6, v7 user and fallback user
    # return :
    def admin_update_of_all_primary_and_fallback_user(self, v4_primary, v5_primary, v6_primary, v7_primary, v4_fallback, v5_fallback, v6_fallback, v7_fallback):
        self.select_v4_primary(v4_primary)
        self.select_v5_primary(v5_primary)
        self.select_v6_primary(v6_primary)
        self.select_v7_primary(v7_primary)
        self.select_v4_fallback(v4_fallback)
        self.select_v5_fallback(v5_fallback)
        self.select_v6_fallback(v6_fallback)
        self.select_v7_fallback(v7_fallback)
        self.click_ok()

    # author : ankush
    # since : 2022-04-04
    # this method is to click on first module for admin update responsibility
    # argument :
    # return :
    def select_first_module_for_admin_update_responsibility(self):
        self.driver.switch_to.frame("issuedetails-frame")
        self.click_child_confirmation()
        self.driver.switch_to.frame("d40aa4b3-f81d-4f82-b8bf-af6b57d91fa1")
        self.bu.click((By.XPATH, self.link_first_part_module_xpath))

    # author : ankush
    # since : 2022-04-04
    # this method is to click refresh
    # argument :
    # return :
    def click_refresh(self):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_refresh_id))

    # author : ankush
    # since : 2022-04-08
    # this method is use to confirm release as v8 user after v7 confirmation
    # argument : internal comment and release letter comment
    # return :
    button_v8_confirmation_post_v7_confirmation_id = "TransitionId_4030"
    def click_v8_confirmation_post_v7_confirmation(self, internal_comments):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_v8_confirmation_post_v7_confirmation_id))
        self.set_internal_comment(internal_comments)
        self.click_ok()

    # author : ankush
    # since : 2022-01-03
    # this method is use to reject release as v8 user after all confirmation
    # argument : release letter comment and internal comment
    # return :
    button_v8_rejection_post_v7_confirmation_id = "TransitionId_4031"
    def click_v8_rejection_post_v7_confirmation(self, internal_comment):
        self.driver.switch_to.frame("issuedetails-frame")
        self.bu.click((By.ID, self.button_v8_rejection_post_v7_confirmation_id))
        self.set_internal_comment(internal_comment)
        self.click_ok()

    # author : ankush
    # since : 2022-04-12
    # this method is use to reject module as v4 user
    # argument :
    # return :
    def reject_as_v4_user(self, reject_comment_v4_user, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_reject_as_v4_user(reject_comment_v4_user, main_window)
        self.click_ok()

    # author : ankush
    # since : 2022-02-10
    # this method is use to reject module as v5 user
    # argument :
    # return :
    button_reject_v5_user_post_v4_rejection_id = "TransitionId_3584"
    def click_reject_as_v5_user_post_v4_rejection(self, reject_comment_v5_user, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_reject_v5_user_post_v4_rejection_id))
        self.bu.send_keys((By.ID, self.textbox_reject_comment_v5_user_id), reject_comment_v5_user)


    # author : ankush
    # since : 2022-04-12
    # this method is use to reject module as v5 user
    # argument :
    # return :
    def reject_as_v5_user(self, reject_comment_v5_user, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_reject_as_v5_user_post_v4_rejection(reject_comment_v5_user, main_window)
        self.click_ok()

    # author : ankush
    # since : 2022-02-10
    # this method is use to reject module as v5 user
    # argument :
    # return :
    button_reject_v6_user_post_v4_and_v5_rejection_id = "TransitionId_3585"
    def click_reject_as_v6_user_post_v4_and_v5_rejection(self, reject_comment_v6_user, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_reject_v6_user_post_v4_and_v5_rejection_id))
        self.bu.send_keys((By.ID, self.textbox_reject_comment_v6_user_id), reject_comment_v6_user)

    # author : ankush
    # since : 2022-04-12
    # this method is use to reject module as v5 user
    # argument :
    # return :
    def reject_as_v6_user(self, reject_comment_v6_user, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_reject_as_v6_user_post_v4_and_v5_rejection(reject_comment_v6_user, main_window)
        self.click_ok()

    # author : ankush
    # since : 2022-02-10
    # this method is use to reject module as v5 user
    # argument :
    # return :
    button_reject_v7_user_post_v4_v5_and_v6_rejection_id = "TransitionId_3587"
    def click_reject_as_v7_user_post_v4_v5_and_v6_rejection(self, reject_comment_v7_user, main_window):
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_reject_v7_user_post_v4_v5_and_v6_rejection_id))
        self.bu.send_keys((By.ID, self.textbox_reject_comment_v7_user_id), reject_comment_v7_user)

    # author : ankush
    # since : 2022-04-12
    # this method is use to reject module as v5 user
    # argument :
    # return :
    def reject_as_v7_user(self, reject_comment_v7_user, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.click_reject_as_v7_user_post_v4_v5_and_v6_rejection(reject_comment_v7_user, main_window)
        self.click_ok()



    # author : ankush
    # since : 2022-04-12
    # this method is use to discard module as admin user
    # argument :
    # return :
    button_admin_discard_module_id = "TransitionId_5159"
    textbox_generic_comment = "H13881"
    def admin_discard_module(self, generic_comment, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.bu.switch_to_child_window(main_window)
        self.driver.switch_to.frame("ViewFrame")
        self.bu.click((By.ID, self.button_admin_discard_module_id))
        self.bu.send_keys((By.ID, self.textbox_generic_comment), generic_comment)
        self.click_ok()

    # author : ankush
    # since : 2022-05-06
    # this method is use to switch to view frame
    # argument :
    # return :
    def switch_to_view_frame(self):
        self.driver.switch_to.frame("ViewFrame")

    # author : ankush
    # since : 2022-05-06
    # this method is use to switch to view frame
    # argument :
    # return :
    def switch_to_button_frame(self):
        self.driver.switch_to.frame("buttons")

    # author : ankush
    # since : 2022-05-06
    # this method is use to reset and requery of different user
    # argument :
    # return :
    button_reset_and_requery_id = "TransitionId_3601"
    def click_reset_and_requery(self, main_window):
        self.driver.switch_to.frame("issuedetails-frame-iframe")
        self.click_child_confirmation()
        self.click_module_confirmation()
        self.bu.switch_to_child_window(main_window)
        self.switch_to_view_frame()
        self.bu.click((By.ID, self.button_reset_and_requery_id))
        self.driver.switch_to.parent_frame()
        time.sleep(3)
        self.switch_to_view_frame()
        time.sleep(3)
        self.switch_to_button_frame()
        self.click_ok()

