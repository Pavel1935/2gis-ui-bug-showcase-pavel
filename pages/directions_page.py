from pages.base_page import BasePage
from locators.directions_locators import DirectionsLocators
from locators.main_locators import MainLocators
from playwright.sync_api import expect
from Constants import Constants



class DirectionsPage(BasePage):

    def wait_and_click_button_directions(self):
        self.wait_and_click(MainLocators.DIRECTIONS_BUTTON)

    def enter_from_moscow(self, timeout: int = 10_000):
        from_input = self.page.locator(DirectionsLocators.FROM_INPUT)
        from_input.click()
        # печатаем по одному слову
        for ch in "Москва, Город":
            from_input.type(ch, delay=120)
        from_input.fill(Constants.LOCATORS_FROM)

        suggestion = self.page.locator(DirectionsLocators.FROM_SUGGESTION_MOSCOW)
        suggestion.wait_for(state="visible", timeout=timeout)
        suggestion.click()

    def enter_to_yerevan(self, timeout: int = 10_000):
        to_input = self.page.locator(DirectionsLocators.TO_INPUT)
        to_input.click()
        # печатаем по одному слову
        for ch in "Ереван, Город":
            to_input.type(ch, delay=120)
        to_input.fill(Constants.LOCATORS_TO)

        suggestion = self.page.locator(DirectionsLocators.TO_SUGGESTION_YEREVAN)
        suggestion.wait_for(state="visible", timeout=timeout)
        suggestion.click()

    def enter_to_tbilisi(self, timeout: int = 10_000):
        to_input = self.page.locator(DirectionsLocators.TO_INPUT)
        to_input.click()
        # печатаем по одному слову
        for ch in "Тбилист, Город":
            to_input.type(ch, delay=120)
        to_input.fill(Constants.LOCATORS_TO_1)

        suggestion = self.page.locator(DirectionsLocators.TO_SUGGESTION_TBILISI)
        suggestion.wait_for(state="visible", timeout=timeout)
        suggestion.click()

    def wait_for_error(self, timeout: int = 10_000):
        try:
            self.wait_for_text("Что-то пошло не так", timeout)
        except:
            self.wait_for_text("Не удалось проложить маршрут", timeout)

