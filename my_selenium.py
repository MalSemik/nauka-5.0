from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

opts = Options()
opts.add_argument("--start-maximized")
#opts.add_argument("--headless") nie pokazuje, co fobi, cfaniaczek
path_to_chrome_webdriver_executable = r"C:\Users\Magija\Downloads\chromedriver_win32 (1)\chromedriver.exe"
chrome = WebDriver(path_to_chrome_webdriver_executable, options=opts)
chrome.get("http://www.pindiy.com/")
seconds_to_wait_for_elements_on_page_to_load = 10
chrome.implicitly_wait(seconds_to_wait_for_elements_on_page_to_load)


html_login = chrome.find_element_by_xpath(r'//*[@id="ls_username"]')
html_pass = chrome.find_element_by_xpath(r'//*[@id="ls_password"]')

html_login.send_keys("jewelinka")
html_pass.send_keys("jewelinka")
button = chrome.find_element_by_css_selector(r"#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button > em")
button.click()

