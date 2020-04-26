import unittest
from selenium import webdriver
from pageobjects.pesas_mancuernas import *

class PesasMancuernas(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.decathlon.es/es/p/kit-de-pesas-y-barras-de-musculacion-cross-training-domyos-de-50-kg/_/R-p-301315?mc=8501164')
        self.page_pesas_mancuernas = DecathPesasMancuernas(self.driver)

    def test_stock(self):
        """
        Test to check if there are stock in decathlon page for one item given in the URL
        :return: None
        """
        text, displayed = self.page_pesas_mancuernas.get_text_stock()
        self.assertNotEqual(text, "ACTUALMENTE AGOTADO", "El elemento que buscas sigue sin estar disponible")
        self.assertFalse(displayed, "Parece que ya hay stock del elemento que buscas, revisalo ¡corre!")

    def test_add_cart(self):
        """
        Test to check if the elemet add_to_cart is present in the given URL. Therefore we can buy it
        :return: None
        """
        verify = self.page_pesas_mancuernas.element_add_to_cart_is_visible()
        self.assertTrue(verify, "Sigue sin haber stock")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
