class PageObject:
    url = "https://catalog.onliner.by/"

class LoginPage(PageObject):   #пример с занятия
    login_editable_locator = "xpath = DOM/html/header/div"
    password_editable_locator = "xpath = DOM/html/header/div"
    submit_clickable_locator = "xpath = DOM/html/header/div/div"

    def login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_submit_button()

    def enter_login(self, login):
        print(self.login_editable_locator)
        print(login)

    def enter_password(self, password):
        print(self.password_editable_locator)
        print(password)

    def click_submit_button(self):
        print(self.submit_clickable_locator)

class HeaderPage:
    button_catalog_locator = 'xpath = DOMcatalog'
    button_news_locator = 'xpath = DOMnews'
    button_auto_locator = 'xpath = DOMauto'
    button_haus_locator = 'xpath = DOMhaus'
    button_services_locator = 'xpath = DOMservices'
    button_forum_locator = 'xpath = DOMforum'
    search_string_locator = 'xpath = DOMstring'
    first_product_button_locator = 'xpath = DOMbuttonProduct'

    def click_button(self, button):
        print('нажатие на кнопку по локатору ' + button)

    def enter_search_word(self, word):
        print(self.search_string_locator)
        print(word)

class MainPage:
    list_locator = {'first_locator': 'xpath_1', 'second_locator': 'xpath_2', 'third_locator': 'xpath_3', 'fourth_locator': 'xpath_4'}

    def click_button(self, button):
        print('нажатие на кнопку по локатору ' + button)

class FooterPage:
    pass



if __name__ == '__main__':

    #login_page = LoginPage()
    #login_page.login("Комунарка", "12345678")

    header_click_catalog = HeaderPage()
    header_click_catalog.click_button(header_click_catalog.button_catalog_locator)

    search_word = HeaderPage()
    search_word.enter_search_word('Apple')
    search_word.click_button(search_word.first_product_button_locator)

    main_click_first = MainPage()
    main_click_first.click_button(main_click_first.list_locator['first_locator'])
    main_click_first.click_button(main_click_first.list_locator['second_locator'])