from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import contextlib
import time
import requests

WORD = 'Пылесос'
class PageObject:

    url = "https://catalog.onliner.by/"
    driver = webdriver.Chrome(executable_path="C:\\Users\\kat1k\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get(url)

class HeaderPage(PageObject):

    button_catalog_locator = "//span[@class='b-main-navigation__text' and text()='Каталог']"
    button_news_locator = "//span[@class='b-main-navigation__text' and text()='Новости']"
    button_auto_locator = "//span[@class='b-main-navigation__text' and text()='Автобарахолка']"
    button_haus_locator = 'xpath = DOMhaus'
    button_services_locator = 'xpath = DOMservices'
    button_forum_locator = 'xpath = DOMforum'
    search_string_locator = "//input[@class = 'fast-search__input']"
    first_product_button_locator = "//div[@class = 'result__item result__item_category']"

    def search(self):
        iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
        #self.driver.switch_to.default_content()
        self.driver.switch_to.frame(iframe)

    def click_button(self, button):
        button_1 = self.driver.find_element(By.XPATH, button)
        button_1.click()

    def enter_search_word(self, word):
        self.driver.find_element(By.XPATH, self.search_string_locator).send_keys(word)

def search_search():
    search_word = HeaderPage()
    search_word.enter_search_word(WORD)
    time.sleep(10)
    search_word.search()
    search_word.click_button(search_word.first_product_button_locator)
    print(search_word.driver.current_url)
    print(search_word.driver.sta)
    time.sleep(10)
    PageObject.driver.quit()
    return print('\nтест_2 успешно')

if __name__ == '__main__':
    search_search()