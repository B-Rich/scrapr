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

def crawl_page(listing, name):
    row = DataRow()

    try:
        row.company_name = name #listing.find_element_by_xpath('.//div[@class="lxT6526"]/h1').text.decode('utf-8','ignore')
    except:
        pass

    try:
        row.phone = listing.find_elements_by_xpath('.//div[@class="gtech-school-info"]/p')[1].text.decode('utf-8','ignore')[9:]
    except:
        pass

    try:
        row.address = listing.find_elements_by_xpath('.//div[@class="gtech-school-info"]/p')[2].text.decode('utf-8','ignore')[14:]
    except:
        pass

    try:
        row.city = ''
    except:
        pass

    try:
        row.state = ''
    except:
        pass

    try:
        row.zipcode = ''
    except:
        pass

    try:
        row.website = listing.find_elements_by_xpath('.//div[@class="gtech-school-info"]/p/a')[0].get_attribute('href').decode('utf-8','ignore')
    except:
        pass

    row.dump()

def scroll_element_into_view(driver, element):
    """Scroll element into view"""
    y = int(element.location['y']) - 50
    driver.execute_script('window.scrollTo(0, {0})'.format(y))

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.yisd.net/Schools.aspx")

    schools = len(driver.find_elements_by_xpath('//h5/a'))

    for i in range(0, schools):
        school = None
        name = None
        while True:
            try:
                school = driver.find_elements_by_xpath('//h5/a')[i]
                name = school.text.decode('utf-8','ignore')
                break
            except:
                sleep(3)

        school.click()

        sleep(3)

        crawl_page(driver.find_element_by_xpath('//article'), name)
        driver.find_element_by_xpath('//a[text()="Return to List"]').click()

        sleep(1)

    driver.close()
