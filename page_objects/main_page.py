from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

class MainPage:
    cookies = [By.ID, 'rcc-confirm-button']
    button_order_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    button_order_bottom_page = [By.CLASS_NAME, 'Button_Middle__1CSJM']
    question_1 = [By.ID, 'accordion__heading-0']
    question_2 = [By.ID, 'accordion__heading-1']
    question_3 = [By.ID, 'accordion__heading-2']
    question_4 = [By.ID, 'accordion__heading-3']
    question_5 = [By.ID, 'accordion__heading-4']
    question_6 = [By.ID, 'accordion__heading-5']
    question_7 = [By.ID, 'accordion__heading-6']
    question_8 = [By.ID, 'accordion__heading-7']

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.button_order_header))

    def click_cookies(self):
        if len(self.driver.find_elements(*self.cookies)) > 0:
            self.driver.find_element(*self.cookies).click()

    def click_button_order_header(self):
        self.driver.find_element(*self.button_order_header).click()

    def click_button_order_bottom_page(self):
        self.driver.find_element(*self.button_order_bottom_page).click()

    def scroll_to_faq(self):
        element = self.driver.find_element(By.ID, 'accordion__heading-7')
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def wait_for_load_faq(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            (self.driver.find_element(By.ID, 'accordion__heading-7')))

    def click_question_1(self):
        self.driver.find_element(*self.question_1).click()

    def area_expanded_question_1(self):
        return self.driver.find_element(*self.question_1).get_attribute('aria-expanded')

    def click_question_2(self):
        self.driver.find_element(*self.question_2).click()

    def area_expanded_question_2(self):
        return self.driver.find_element(*self.question_2).get_attribute('aria-expanded')

    def click_question_3(self):
        self.driver.find_element(*self.question_3).click()

    def area_expanded_question_3(self):
        return self.driver.find_element(*self.question_3).get_attribute('aria-expanded')

    def click_question_4(self):
        self.driver.find_element(*self.question_4).click()

    def area_expanded_question_4(self):
        return self.driver.find_element(*self.question_4).get_attribute('aria-expanded')

    def click_question_5(self):
        self.driver.find_element(*self.question_5).click()

    def area_expanded_question_5(self):
        return self.driver.find_element(*self.question_5).get_attribute('aria-expanded')

    def click_question_6(self):
        self.driver.find_element(*self.question_6).click()

    def area_expanded_question_6(self):
        return self.driver.find_element(*self.question_6).get_attribute('aria-expanded')

    def click_question_7(self):
        self.driver.find_element(*self.question_7).click()

    def area_expanded_question_7(self):
        return self.driver.find_element(*self.question_7).get_attribute('aria-expanded')

    def click_question_8(self):
        self.driver.find_element(*self.question_8).click()

    def area_expanded_question_8(self):
        return self.driver.find_element(*self.question_8).get_attribute('aria-expanded')
