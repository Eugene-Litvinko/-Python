from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import contextlib
import time

WORD = 'Пылесос'
class PageObject:

    url = "https://catalog.onliner.by/"
    driver = webdriver.Chrome(executable_path="C:\\Users\\kat1k\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get(url)
# class LoginPage(PageObject):   #пример с занятия
#     login_editable_locator = "xpath = DOM/html/header/div"
#     password_editable_locator = "xpath = DOM/html/header/div"
#     submit_clickable_locator = "xpath = DOM/html/header/div/div"
#
#     def login(self, login, password):
#         self.enter_login(login)
#         self.enter_password(password)
#         self.click_submit_button()
#
#     def enter_login(self, login):
#         print(self.login_editable_locator)
#         print(login)
#
#     def enter_password(self, password):
#         print(self.password_editable_locator)
#         print(password)
#
#     def click_submit_button(self):
#         print(self.submit_clickable_locator)

class HeaderPage(PageObject):

    button_catalog_locator = "//span[@class='b-main-navigation__text' and text()='Каталог']"
    button_news_locator = "//span[@class='b-main-navigation__text' and text()='Новости']"
    button_auto_locator = "//span[@class='b-main-navigation__text' and text()='Автобарахолка']"
    button_haus_locator = 'xpath = DOMhaus'
    button_services_locator = 'xpath = DOMservices'
    button_forum_locator = 'xpath = DOMforum'
    search_string_locator = "//input[@class = 'fast-search__input']"
    first_product_button_locator = "//div[@class = 'result__item result__item_category']"

    def click_button(self, button):
        button_1 = self.driver.find_element(By.XPATH, button)
        button_1.click()

    def enter_search_word(self, word):
        self.driver.find_element(By.XPATH, self.search_string_locator).send_keys(word)


class MainPage(PageObject):
    list_locator = {'first_locator': 'xpath_1', 'second_locator': 'xpath_2', 'third_locator': 'xpath_3', 'fourth_locator': 'xpath_4'}

    def click_button(self, button):
        print('нажатие на кнопку по локатору ' + button)

class FooterPage:
    pass

def test_header_click():
    header_click_catalog = HeaderPage()
    header_click_catalog.click_button(header_click_catalog.button_news_locator)
    return print('тест успешен')

def test_search():
    search_word = HeaderPage()
    search_word.enter_search_word(WORD)
    time.sleep(10)
    #search_word.click_button(search_word.first_product_button_locator)
    PageObject.driver.quit()
    return print('тест_2 успешно')

if __name__ == '__main__':

    #login_page = LoginPage()
    #login_page.login("Комунарка", "12345678")
    #driver = webdriver.Chrome(executable_path = "C:\\Users\\kat1k\\Downloads\\chromedriver_win32\\chromedriver.exe")
    #driver.get(PageObject.url)

    test_header_click()
    PageObject.driver.get(PageObject.url)#сделал так запуск с начального места второго теста
    test_search()

    #search_word.click_button(search_word.first_product_button_locator)

    # main_click_first = MainPage()
    # main_click_first.click_button(main_click_first.list_locator['first_locator'])
    # main_click_first.click_button(main_click_first.list_locator['second_locator'])