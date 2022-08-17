from selenium import webdriver
from page_objects.main_page import MainPage
import time
import pytest


class TestFAQ:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_faq_1(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_1()

        time.sleep(1)
        assert main_page.area_expanded_question_1() == 'true'

    def test_faq_2(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_2()

        time.sleep(1)
        assert main_page.area_expanded_question_2() == 'true'

    def test_faq_3(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_3()

        time.sleep(1)
        assert main_page.area_expanded_question_3() == 'true'

    def test_faq_4(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_4()

        time.sleep(1)
        assert main_page.area_expanded_question_4() == 'true'

    def test_faq_5(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_5()

        time.sleep(1)
        assert main_page.area_expanded_question_5() == 'true'

    def test_faq_6(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_6()

        time.sleep(1)
        assert main_page.area_expanded_question_6() == 'true'

    def test_faq_7(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_7()

        time.sleep(1)
        assert main_page.area_expanded_question_7() == 'true'

    def test_faq_8(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_cookies()
        main_page.wait_for_load_home_page()
        main_page.scroll_to_faq()
        time.sleep(1)

        main_page.click_question_8()

        time.sleep(1)
        assert main_page.area_expanded_question_8() == 'true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
