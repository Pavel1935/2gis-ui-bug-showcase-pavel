from pages.directions_page import DirectionsPage
from conftest import browser_page
from Constants import Constants

class TestDirectionsPage:

    def test_route_to_yerevan_shows_error(self, browser_page):
        browser_page.goto("https://2gis.ru/")

        directions = DirectionsPage(browser_page)

        directions.wait_and_click_button_directions()
        directions.enter_from_moscow()
        directions.enter_to_yerevan()
        directions.wait_for_error()

    def test_route_to_tbilisi_shows_error(self, browser_page):
        browser_page.goto("https://2gis.ru/")

        directions = DirectionsPage(browser_page)

        directions.wait_and_click_button_directions()
        directions.enter_from_moscow()
        directions.enter_to_tbilisi()
        directions.wait_for_error()



