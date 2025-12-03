from pages.directions_page import DirectionsPage
from conftest import browser_page
from Constants import Constants

class TestDirectionsPage:

    def test_route_to_erevan_shows_error(self, browser_page):
        browser_page.goto("https://2gis.ru/")

        directions = DirectionsPage(browser_page)

        directions.wait_and_click_button_directions()
        directions.enter_from(Constants.LOCATORS_FROM)
        directions.enter_to(Constants.LOCATORS_TO)
        directions.wait_for_error()


