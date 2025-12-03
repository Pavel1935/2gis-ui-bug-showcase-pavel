from pages.base_page import BasePage
from locators.directions_locators import DirectionsLocators
from locators.main_locators import MainLocators
from playwright.sync_api import expect


# class DirectionsPage(BasePage):

    # def wait_and_click_button_directions(self):
    #     self.wait_and_click(MainLocators.DIRECTIONS_BUTTON)
    #
    #
    # def enter_from(self, value: str, timeout: int = 10_000):
    #     self.page.locator(DirectionsLocators.FROM_INPUT).fill(value)
    #
    #     suggestion = self.page.get_by_text(value).first
    #     suggestion.wait_for(state="visible", timeout=timeout)
    #     suggestion.click()
    #     self.page.keyboard.press("Enter")
    #
    #
    # def enter_to(self, value: str, timeout: int = 10_000):
    #     self.page.locator(DirectionsLocators.TO_INPUT).fill(value)
    #
    #     suggestion = self.page.get_by_text(value).first
    #     suggestion.wait_for(state="visible", timeout=timeout)
    #     suggestion.click()
    #     self.page.keyboard.press("Enter")
    #
    # def wait_for_error(self, timeout: int = 10_000):
    #     self.wait_for_text("Что-то пошло не так", timeout)

class DirectionsPage(BasePage):

    def wait_and_click_button_directions(self, timeout: int = 10_000):
        self.wait_and_click(MainLocators.DIRECTIONS_BUTTON, timeout)

    def enter_from(self, value: str, timeout: int = 10_000):
        self.page.locator(DirectionsLocators.FROM_INPUT).fill(value)
        self.select_suggestion(value, timeout)
        self.page.keyboard.press("Enter")

    def enter_to(self, value: str, timeout: int = 10_000):
        self.page.locator(DirectionsLocators.TO_INPUT).fill(value)
        self.select_suggestion(value, timeout)
        self.page.keyboard.press("Enter")

    def wait_for_error(self, timeout: int = 10_000):
        self.page.get_by_text("Что-то пошло не так").wait_for(
            state="visible", timeout=timeout
        )

    def select_suggestion(self, value: str, timeout: int = 10_000):
        # Ждём появления блока подсказок
        dropdown = self.page.locator(".suggests__list").first
        dropdown.wait_for(state="visible", timeout=timeout)

        # Берём первую подсказку, содержащую value (например "Москва")
        suggestion = dropdown.locator("div").filter(has_text=value).first
        suggestion.wait_for(state="visible", timeout=timeout)
        suggestion.click()


