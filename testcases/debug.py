from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\anavina\PycharmProjects\\v7_test_automation\\utilities\\driver\\chromedriver.exe")
driver.get("https://smtcat0007prj.rd.corpintra.net/workcenter/tmtrack.dll?shell=swc&LoginPage&Template=loginform&ParamsInUserCache=53.244.194.32_160487468")
parent_window = driver.current_window_handle


driver.switch_to.frame("issuedetails-frame-iframe")
driver.find_element_by_xpath("//Button[text()='Upload & Attach AKV (.csv file)']").click()
child_windows = driver.window_handles
for child in child_windows:
    if parent_window != child:
        driver.switch_to.window(child)
        driver.set_page_load_timeout(5)
    else:
        assert "Window not found"
# driver.execute_script("window.stop();")

driver.switch_to.frame("utiltop")
driver.find_element_by_class_name("frmTxt").send_keys("test_Upload")

#release_id = driver.find_element_by_id("issue_id").get_attribute("value")

