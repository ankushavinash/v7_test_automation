from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from msedge.selenium_tools import EdgeOptions, Edge
import pytest
from utilities import xlUtilis
from utilities.browserUtilis import BrowserUtilities
from utilities.readProperties import ReadConfig
driver = None

# ----------------------------------------setup method run before every test-------------------------------------------
@pytest.fixture()
def setup(browser, environment, headless):
    root_path = str(Path(__file__).parent.parent)
    global driver
    # options.add_experimental_option("browser.download.folderList", 2)
    # options.add_experimental_option("browser.download.manager.showWhenStarting", False)
    # options.add_experimental_option("browser.download.dir", root_path + "\\automation")
    # options.add_experimental_option("browser.helperApps.neverAsk.saveToD  isk",
    #                                 "application/octet-stream,application/vnd.ms-excel,application/zip")
    # options.add_experimental_option("browser.helperApps.neverAsk.openFile",
    #                                 "application/octet-stream,application/vnd.ms-excel,application/zip"

    # setting browser based on user command
    try:
        if browser == "chrome":
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.add_experimental_option("excludeSwitches", ["enable-logging"])
            if headless == "yes":
                chrome_opt.add_argument("--headless")
                driver = webdriver.Chrome(executable_path='.\\utilities\\driver\\chromedriver.exe',options=chrome_opt)
            driver = webdriver.Chrome(executable_path='.\\utilities\\driver\\chromedriver.exe',options=chrome_opt)
        elif browser == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            if headless == "yes":
                options.add_argument("--headless")
                driver = Edge(executable_path='.\\utilities\\driver\\msedgedriver.exe', options=options)
            driver = Edge(executable_path='.\\utilities\\driver\\msedgedriver.exe', options=options)
        else:
            driver = webdriver.Edge(executable_path=".\\utilities\\driver\\msedgedriver.exe")
    except WebDriverException:
        assert False, "Failed to launch the browser : unexpected error occurred"
    else:
        # setting test data based on environment
        # excel_path = ".\\TestData\\" + "TestData_" + environment.upper() + ".xlsx"
        excel_path = ".\\TestData\\" + "testData_mirror.xlsx"
        if not environment == "":
            url = ReadConfig.get_application_url(environment)
        else:
            assert False, "environment parameter missing"

        # Login
        driver.delete_all_cookies()
        bu = BrowserUtilities(driver)
        bu.launch_application(driver, url)

        # Login Steps removed and will be used at test script level
        # login_id = str(xlUtilis.read_data(excel_path, 'Login', 2, 2))
        # password = str(xlUtilis.read_data(excel_path, 'Login', 2, 3))
        # bu.login_application(login_id, password)
        yield [driver, url, excel_path]
        #driver.close()
        #driver.quit()


# phrasing and fetching data from command
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--environment")
    parser.addoption("--headless")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def environment(request):
    return request.config.getoption("--environment")


@pytest.fixture()
def headless(request):
    return request.config.getoption("--headless")


# ---------pytest html ------------------------------------------------
# hook for adding environment info to html allurereport
def pytest_configure(config):
    config._metadata['Project Name'] = 'V7 Application'
    config._metadata['Tester'] = 'Ankush Avinash'
    config._metadata['Suite'] = 'Regression'


def pytest_html_report_title(report):
    report.title = "V7 Test Automation Report"

# hook for delete/modify environment info to html allurereport
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot():
    return driver.get_screenshot_as_base64()