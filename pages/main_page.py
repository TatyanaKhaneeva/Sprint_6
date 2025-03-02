import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    # принять куки
    @allure.step('Принять Куки')
    def accept_cookie(self):
        return self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    # клик по кнопке Заказать вверху страницы
    @allure.step('Клик по кнопке Заказать вверху страницы')
    def upper_order_button_click(self):
        return self.click_to_element(MainPageLocators.UPPER_ORDER_BUTTON)

    # скролл страницы до кнопки Заказать
    @allure.step('Скролл страницы до кнопки Заказать')
    def scroll_for_order_button_down(self):
        button_order_finish = self.find_element_with_wait(MainPageLocators.LOWER_ORDER_BUTTON)
        self.scroll_for_element(button_order_finish)

    # клик по кнопке Заказать внизу страницы
    @allure.step('Клик по кнопке Заказать внизу страницы')
    def lower_order_button_click(self):
        return self.click_to_element(MainPageLocators.LOWER_ORDER_BUTTON)

    # создание заказа
    def create_order(self, button):
        self.click_to_element(button)

    @allure.step('Скролл страницы до последнего вопроса')
    def scroll_for_question_block(self):
        last_question = self.find_element_with_wait(MainPageLocators.SCROLL_TO_QUESTION_LOCATOR)
        return self.scroll_for_element(last_question)

    # клик по стрелке Вопроса
    @allure.step('Клик на Вопрос')
    def click_for_question (self, question_id):
        locator_question = self.format_locators(MainPageLocators.QUESTION_LOCATOR, question_id)
        self.scroll_for_question_block()
        self.click_to_element(locator_question)

    @allure.step('Получение ответа на Вопрос')
    # получение ответа на Вопрос
    def get_answer_text(self, question_id):
        locator_answer = self.format_locators(MainPageLocators.ANSWER_LOCATOR, question_id)
        self.scroll_for_question_block()
        return self.get_text_from_element(locator_answer)

    @allure.step('Проверка корректности ответа на Вопрос')
    # проверка корректности ответа на Вопрос
    def check_answer_for_question(self, question_id):
        self.click_for_question(question_id)
        return self.get_answer_text(question_id)