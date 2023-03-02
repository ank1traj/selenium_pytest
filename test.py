import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC


class First:

    def first_test(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        wait = WebDriverWait(driver, 10)
        driver.get('https://yatra.com')
        driver.maximize_window()

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)

        going_to = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        time.sleep(3)
        going_to.send_keys("New York")
        time.sleep(3)

        search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div["
                                                                                   "1]//li")))

        for result in search_results:
            if "New York (JFK)" in result.text:
                print(result.text)
                result.click()
                break
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td")))
        all_dates = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='monthWrapper']//tbody//td["
                                                                              "@class!='inActiveTD']")))

        for date in all_dates:
            if date.get_attribute("data-date") == "23/03/2023":
                date.click()
                break

        driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        time.sleep(5)

        pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var "
                                           "pageLength=document.body.scrollHeight;")

        match = False
        while match == False:
            last_count = pageLength
            time.sleep(2)
            lenOfPage = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var "
                "pageLength=document.body.scrollHeight;"
            )
            if last_count == pageLength:
                match = True

        time.sleep(4)

        driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()

        time.sleep(4)
        all_stops = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), 'Non Stop')]")))
        print(len(all_stops))

        for stop in all_stops:
            assert stop.text == "1 Stop"

        driver.close()
        driver.quit()


first = First()
first.first_test()
