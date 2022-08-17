from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import datetime


class OrderPage:
    first_name_field = [By.XPATH, ".//div[@class='Order_Form__17u6u']/div[1]/input"]
    last_name_field = [By.XPATH, ".//div[@class='Order_Form__17u6u']/div[2]/input"]
    address_field = [By.XPATH, ".//div[@class='Order_Form__17u6u']/div[3]/input"]
    subway_field = [By.XPATH, ".//div[@class='Order_Form__17u6u']/div[4]/div/div[1]/input"]
    subway_option = [By.XPATH, ".//div[@class='select-search__select']/ul/li[1]"]
    phone_number_field = [By.XPATH, ".//div[@class='Order_Form__17u6u']/div[5]/input"]
    button_next = [By.CLASS_NAME, "Button_Middle__1CSJM"]

    order_date = [By.XPATH, ".//div[@class='Order_Form__17u6u']/div[1]/div[1]/div/input"]
    rental_period = [By.CLASS_NAME, 'Dropdown-root']
    rental_period_option = [By.XPATH, ".//div[@class='Dropdown-menu']/div[2]"]
    color_option_black = [By.ID, 'black']
    color_option_grey = [By.ID, 'grey']
    comment_field = [By.XPATH, ".//div[@class='Order_Form__17u6u']/div[4]/input"]

    button_order = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[2]"]

    button_confirm_order = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']/div[2]/button[2]"]

    button_check_status = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']/div[2]/button"]

    logo_samokat = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.last_name_field))

    def send_keys_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def send_keys_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def send_keys_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def send_keys_subway(self, subway):
        self.driver.find_element(*self.subway_field).click()
        self.driver.find_element(*self.subway_field).send_keys(subway)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.subway_option))
        self.driver.find_element(*self.subway_option).click()

    def send_keys_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_button_next(self):
        button = self.driver.find_element(*self.button_next)
        self.driver.execute_script('arguments[0].scrollIntoView();', button)
        self.driver.find_element(*self.button_next).click()

    def send_order_date(self):
        date = datetime.date.today() + datetime.timedelta(days=1)
        self.driver.find_element(*self.order_date).send_keys(date.strftime("%d.%m.%Y"))
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def send_rental_period(self):
        self.driver.find_element(*self.rental_period).click()
        self.driver.find_element(*self.rental_period_option).click()

    def click_color_option_black(self):
        self.driver.find_element(*self.color_option_black).click()

    def click_color_option_grey(self):
        self.driver.find_element(*self.color_option_grey).click()

    def send_comment_field(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()

    def click_button_confirm_order(self):
        self.driver.find_element(*self.button_confirm_order).click()

    def click_button_check_status(self):
        self.driver.find_element(*self.button_check_status).click()

    def click_logo_samokat(self):
        self.driver.find_element(*self.logo_samokat).click()

    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    def wait_for_new_tab(self, number_of_tabs):
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(number_of_tabs))

    def switch_to_tab(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])

    def authorization_page_order_1(self, first_name, last_name, address, subway, phone_number):
        self.send_keys_first_name(first_name)
        self.send_keys_last_name(last_name)
        self.send_keys_address(address)
        self.send_keys_subway(subway)
        self.send_keys_phone_number(phone_number)
        self.click_button_next()

    def authorization_page_order_2(self, comment):
        self.send_order_date()
        self.send_rental_period()
        self.click_color_option_black()
        self.send_comment_field(comment)
        self.click_button_order()

    def check_click_logo_yandex(self, number_of_tabs, number):
        self.click_logo_yandex()
        self.wait_for_new_tab(number_of_tabs)
        self.switch_to_tab(number)
