from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class Actions(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait_time = 10

    def go(self, url):
        self.driver.get(url)
        return None

    def refresh(self):
        self.driver.refresh()
        return None

    def switch_to_tab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[tab])
        return None

    def click(self, locator):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(locator))
        element.click()
        return None

    def click_by_enter(self, locator):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(locator))
        element.send_keys(Keys.RETURN)
        return None

    def input_text(self, locator, text):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(locator)
        )
        element.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        element.send_keys(text)
        return None

    def attach_file_to_invisible_input(self, locator, file_path):
        """make hidden <input> visible, attach file, than make hidden again"""
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(locator))

        self.driver.execute_script(f"arguments[0].setAttribute(arguments[1], arguments[2])",
                                   element, "style", "display: yes;")

        element.send_keys(file_path)

        self.driver.execute_script(f"arguments[0].setAttribute(arguments[1], arguments[2])",
                                   element, "style", "display: none;")
        return None
