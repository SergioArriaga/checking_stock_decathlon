import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DecathPesasMancuernas(object):
    """
    Inits a Base Page View Page Model.
    """

    ADD_CART = (By.XPATH, '(//*[@data-anly="pdp-add-to-cart"])[1]')
    ACCEPT_COOKIES = (By.ID, 'didomi-notice-agree-button')
    PRICE = (By.XPATH, '//*[contains(@class,"product-summary-price")]//*[@class="prc__active-price svelte-rppk6w"]')

    def __init__(self, myDriver):
        self.driver = myDriver

    def accept_cookies(self):
        """
        Accept cookies if it is neccesary
        :return:
        """
        try:
            element = self.driver.find_element(*self.ACCEPT_COOKIES)
            self.driver.implicitly_wait(10)
            if element.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                element.click()
        except NoSuchElementException:
            pass

    def get_price(self):
        """
        Return the price of the item displayed in web
        :return:
        """
        self.driver.implicitly_wait(5)
        element = self.driver.find_element(*self.PRICE)
        if element.is_displayed():
            return element.text
        else:
            return None

    def element_add_to_cart_is_enabled(self):
        """
        Check if the element 'add to cart' is clickable
        :return:
        """
        self.driver.implicitly_wait(5)
        element = self.driver.find_element(*self.ADD_CART)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        custom_path = os.path.abspath(os.path.join('screenshots', 'screenKit_Mancuernas_pesas.png'))
        self.driver.get_screenshot_as_file(custom_path)
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
            clickable = True
        except TimeoutException:
            clickable = False
        return clickable
