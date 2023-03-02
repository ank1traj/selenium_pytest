import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_flight_page import SearchFlightResults
from utilities.utils import Utils


class LaunchPage(BaseDriver):

    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    SEARCH_RESULTS = "//div[@class='viewport']//div[1]//li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[""@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def get_depart_location_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def get_going_to_location_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def get_search_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_RESULTS)

    def get_date_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def get_all_dates(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enter_depart_from_location(self, depart_location):
        self.get_depart_location_field().click()
        self.get_depart_location_field().send_keys(depart_location)
        self.get_depart_location_field().send_keys(Keys.ENTER)

    def enter_going_to_location(self, going_to_location):
        self.get_going_to_location_field().click()
        time.sleep(2)
        self.get_going_to_location_field().send_keys(going_to_location)
        time.sleep(2)

        search_results = self.get_search_results()
        for result in search_results:
            if going_to_location in result.text:
                self.log.info(result.text)
                result.click()
                break

    def select_departure_date(self, departure_date):
        self.get_date_field().click()
        all_dates = self.get_all_dates().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                date.click()
                break

    def click_search_flight_button(self):
        self.get_search_button().click()
        time.sleep(4)

    def search_flight(self, departure_location, going_to_location, departure_date):
        self.enter_depart_from_location(departure_location)
        self.enter_going_to_location(going_to_location)
        self.select_departure_date(departure_date)
        self.click_search_flight_button()
        search_flight_result = SearchFlightResults(self.driver)
        return search_flight_result
