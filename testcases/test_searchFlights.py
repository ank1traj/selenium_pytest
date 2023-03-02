import pytest
import softest
from ddt import ddt, data, unpack, file_data

from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestFirst(softest.TestCase):

    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @data(("New Delhi", "New York", "23/03/2023", "1 Stop"), ("Bombay", "New York", "23/04/2023", "1 Stop"))
    @unpack
    # @file_data("../testdata/testdata.json")
    def test_first_test(self, depart_from, going_to, date, stop):
        search_flight_result = self.lp.search_flight(depart_from, going_to, date)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop(stop)
        all_stops = search_flight_result.get_search_flight_results()
        self.log.info(len(all_stops))
        self.ut.assert_list_items_text(all_stops, stop)
