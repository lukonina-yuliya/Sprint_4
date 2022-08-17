from selenium import webdriver
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
import time
from selenium.webdriver.common.by import By
import pytest


class TestPlaceOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("first,last,address,subway,phone", [
        ('Тест', 'Первый', 'Москва, 4-я Парковая, 9', 'Измайловская', '89111111111'),
        ('Тест', 'Второй', 'Москва, Тульская, 10-11', 'Тульская', '89222222222')
    ])
    def test_place_order_from_header(self, first, last, address, subway, phone):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()

        main_page.click_button_order_header()

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()

        order_page.authorization_page_order_1(first, last, address, subway, phone)

        order_page.authorization_page_order_2('Комментарий курьеру')

        order_page.click_button_confirm_order()
        time.sleep(2)

        assert self.driver.find_element(By.XPATH,
                                        ".//div[@class='Order_Modal__YZ-d3']/div[2]/button").text == "Посмотреть статус"

        order_page.click_button_check_status()
        order_page.click_logo_samokat()

        time.sleep(1)

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        order_page.check_click_logo_yandex(2, 1)

        time.sleep(20)

        assert self.driver.current_url == 'https://yandex.ru/'

        self.driver.close()
        order_page.switch_to_tab(0)

    @pytest.mark.parametrize("first,last,address,subway,phone", [
        ('Тест', 'Третий', 'Москва, 4-я Парковая, 9', 'Измайловская', '89111111111'),
        ('Тест', 'Четвертый', 'Москва, Тульская, 10-11', 'Тульская', '89222222222')
    ])
    def test_place_order_from_bottom_page(self, first, last, address, subway, phone):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()

        time.sleep(2)

        main_page.click_button_order_bottom_page()

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()

        order_page.authorization_page_order_1(first, last, address, subway, phone)

        order_page.authorization_page_order_2('Комментарий курьеру')

        order_page.click_button_confirm_order()
        time.sleep(2)

        assert self.driver.find_element(By.XPATH,
                                        ".//div[@class='Order_Modal__YZ-d3']/div[2]/button").text == "Посмотреть статус"

        order_page.click_button_check_status()
        order_page.click_logo_samokat()

        time.sleep(2)

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        order_page.check_click_logo_yandex(2, 1)

        time.sleep(2)

        assert self.driver.current_url == 'https://yandex.ru/'

        self.driver.close()
        order_page.switch_to_tab(0)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
