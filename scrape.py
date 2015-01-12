from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import csv
import sys
from optparse import OptionParser

class DataRow():
    def __init__(self):
        self.company_name = ''
        self.phone = ''
        self.address = ''
        self.city = ''
        self.state = ''
        self.zipcode = ''
        self.website = ''

    def dump(self):
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_MINIMAL)
        writer.writerow((self.company_name, self.phone, self.address, self.city, self.state, self.zipcode, self.website))

def crawl_page(driver):
    listings = driver.find_elements_by_xpath('//div[@class="result"]')

    for listing in listings:
        row = DataRow()

        try:
            row.company_name = listing.find_element_by_xpath('.//span[@itemprop="name"]').text.decode('utf-8','ignore')
        except:
            pass

        try:
            row.phone = listing.find_element_by_xpath('.//li[@itemprop="telephone"]').text.decode('utf-8','ignore')
        except:
            pass

        try:
            row.address = listing.find_element_by_xpath('.//span[@itemprop="streetAddress"]').text.decode('utf-8','ignore')
        except:
            pass

        try:
            row.city = listing.find_element_by_xpath(".//span[@itemprop='addressLocality']").text.decode('utf-8','ignore')
        except:
            pass

        try:
            row.state = listing.find_element_by_xpath(".//span[@itemprop='addressRegion']").text.decode('utf-8','ignore')
        except:
            pass

        try:
            row.zipcode = listing.find_element_by_xpath(".//span[@itemprop='postalCode']").text.decode('utf-8','ignore')
        except:
            pass

        try:
            row.website = listing.find_element_by_xpath(".//a[@class='track-visit-website']").get_attribute('href').decode('utf-8','ignore')
        except:
            pass

        row.dump()

def has_next_page(driver):
    try:
        return driver.find_element_by_xpath('//li/a[@class="next ajax-page"]')
    except:
        return None

def scroll_element_into_view(driver, element):
    """Scroll element into view"""
    y = int(element.location['y']) - 50
    driver.execute_script('window.scrollTo(0, {0})'.format(y))

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("--what",
                  help="what to look for")
    parser.add_option("--where",
                  help="where to look")

    (options, args) = parser.parse_args()

    driver = webdriver.Chrome()
    driver.get("http://www.yellowpages.com/")

    search_terms = driver.find_element_by_name("search_terms")
    search_terms.click()
    search_terms.send_keys(options.what)

    sleep(randint(2,6))

    location = driver.find_element_by_name("geo_location_terms")
    location.click()
    location.send_keys(options.where)

    sleep(randint(3,5))

    search_button = driver.find_element_by_xpath('//button[@type="submit" and @value="Search"]')
    search_button.click()

    while True:

        sleep(randint(26,47))

        crawl_page(driver)

        next_page = has_next_page(driver)

        if not next_page:
            break

        scroll_element_into_view(driver, next_page)

        next_page.click()

    driver.close()
