from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class DecathPesasMancuernas:

    def __init__(self, myDriver):
        self.driver = myDriver
        self.text_stock = (By.XPATH, '//*[@class="stock-infos"]//..//h3')
        self.add_cart = (By.ID, 'ctaButton')

    def get_text_stock(self):
        displayed = False
        self.driver.implicitly_wait(5)
        element = self.driver.find_element(*self.text_stock)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.get_screenshot_as_file('/screenshots/screenKit_Mancuernas_pesas.png')
        if element.is_displayed():
            displayed= True
        return element.text, displayed

    def element_add_to_cart_is_visible(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.element_to_be_clickable(self.add_cart))
            clickable = True
        except TimeoutException:
            clickable = False
        return clickable
