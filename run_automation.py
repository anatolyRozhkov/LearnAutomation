from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from perform_actions import Actions


# install the latest version of chromedriver on your PC
chrome_service = Service(executable_path=ChromeDriverManager().install())

# enable options for webdriver
chrome_options = webdriver.ChromeOptions()
# set window size
chrome_options.add_argument(f"--window-size=1920,1080")
# prevent driver from quiting
#chrome_options.add_experimental_option("detach", True)

# create driver object
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

# execute code
page = Actions(driver)
page.go("https://uptrader-staging-primary.uptr.dev/auth/login")

# input email
page.input_text((By.XPATH, "//input[@id='emailOrPhone']"), "admin@uptrader.us")
# input password
page.input_text((By.CSS_SELECTOR, "#password"), "qwerty123")
# click on submit button
page.click((By.CSS_SELECTOR, "button[type='submit']"))
