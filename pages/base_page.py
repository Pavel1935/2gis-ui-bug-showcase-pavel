from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def click_text(self, text: str):
        self.page.get_by_text(text).click()

    def wait_for_text(self, text: str, timeout: int = 10_000):
        self.page.get_by_text(text).wait_for(state="visible", timeout=timeout)

    def wait_for_visible(self, locator: str, timeout: int = 10_000):
        expect(self.page.locator(locator)).to_be_visible(timeout=timeout)

    def fill_inputs_by_index(self, selector, code: str):
        inputs = self.page.locator(selector)
        for i, digit in enumerate(code):
            inputs.nth(i).fill(digit)

    def wait_and_click(self, locator: str, timeout: int = 10_000):
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=timeout)
        expect(element).to_be_enabled(timeout=timeout)
        element.click()
