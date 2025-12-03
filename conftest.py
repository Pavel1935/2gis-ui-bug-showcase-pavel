import pytest
from playwright.sync_api import sync_playwright


"""ФИКСТУРА КОТОРАЯ ЗАПУСКАЕТ UI Playwright"""
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            permissions=["geolocation"],   # ← ДАЁМ ДОСТУП
            geolocation={"latitude": 55.75, "longitude": 37.61},  # Москва
        )

        page = context.new_page()
        yield page

        context.close()
        browser.close()


        context.close()
        browser.close()
