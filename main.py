import re
import string
import urlparse
import scrapy
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

class Product(scrapy.Item):
    state_name = scrapy.Field()
    district_name = scrapy.Field()
    ulb_name = scrapy.Field()
    app_received = scrapy.Field()
    app_verifiednot = scrapy.Field()
    app_approved = scrapy.Field()
    app_approved_aadhar = scrapy.Field()
    app_rejected = scrapy.Field()
    app_pullback = scrapy.Field()
    app_closed = scrapy.Field()
    app_ctp = scrapy.Field()
    app_intermediate = scrapy.Field()
    label811 = scrapy.Field()
    app_verified = scrapy.Field()

class socialcops(object):
    def __init__(self):
        self.url = "http://swachhbharaturban.gov.in/ihhl/RPTApplicationSummary.aspx"
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=options)
        #self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def no1(self):
        row_count = self.driver.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_gvApplicationListState']/tbody/tr")
        return len(row_count)
    def no2(self):
        row_count = len(self.driver.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_gvApplicationListDistrict']/tbody/tr"))
        return row_count
    def no3(self):
        row_count = len(self.driver.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_gvApplicationListULB']/tbody/tr"))
        return row_count
    def parse(self,state,district,no):
        ## print "parse me hooon"
        for x in range(0,no):
            # print "x {}".format(no)  
            str0 = '//a[@id="ContentPlaceHolder1_gvApplicationListULB_LinkButton3_{0}"]'.format(x)
            str1 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label54_{0}"]'.format(x)
            str2 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_lblAPP_VERIFIEDNOT_{0}"]'.format(x)
            str3 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label56_{0}"]'.format(x)
            str4 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label58_{0}"]'.format(x)
            str5 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_lblAPP_APPROVED115_{0}"]'.format(x)
            str6 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label60_{0}"]'.format(x)
            str7 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_lblAPP_PULLBACK_{0}"]'.format(x)
            str8 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label62_{0}"]'.format(x)
            str9 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label64_{0}"]'.format(x)
            str10 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label66_{0}"]'.format(x)
            str11 = '//span[@id="ContentPlaceHolder1_gvApplicationListULB_Label817_{0}"]'.format(x)
            str00 = self.driver.find_element_by_xpath(str0).text
            # print str00 + "fdsghjhgfddsfgh"
            #pdb.set_trace()
            str01 = self.driver.find_element_by_xpath(str1).text
            str02 = self.driver.find_element_by_xpath(str2).text
            str03 = self.driver.find_element_by_xpath(str3).text
            str04 = self.driver.find_element_by_xpath(str4).text
            str05 = self.driver.find_element_by_xpath(str5).text
            str06 = self.driver.find_element_by_xpath(str6).text
            str07 = self.driver.find_element_by_xpath(str7).text
            str08 = self.driver.find_element_by_xpath(str8).text
            str09 = self.driver.find_element_by_xpath(str9).text
            str010 = self.driver.find_element_by_xpath(str10).text
            str011 = self.driver.find_element_by_xpath(str11).text
            product = Product(state_name=state,district_name=district,ulb_name=str00,app_received=str01,app_verifiednot=str02,app_approved=str04,app_approved_aadhar=str05,app_rejected=str06,app_pullback=str07,app_closed=str08,app_ctp=str09,app_intermediate=str010,label811=str011,app_verified=str03)
            product1 = dict(product)
            address = 'state.csv'
            with open(address, 'a') as f:  # Just use 'w' mode in 3.x
                w = csv.DictWriter(f, product1.keys())
                # print "# print me hoon "
                #w.writeheader()
                w.writerow(product1)


    def scrape(self):
        self.driver.get(self.url)
        str1="ContentPlaceHolder1_gvCountry_lnkCOUNTRY_NAME_0"
        # print "1"
        try:
            #str0 = 'ContentPlaceHolder1_gvApplicationListState_lnkSTATE_NAME_'
            #no of states
            # print "noo1"
            noo1=self.no1()
            # print "2"

            ## print noo1
            #self.parse()
            try:
                for x in range(0,noo1-1):
                    # print "3"
                    str0 = 'ContentPlaceHolder1_gvApplicationListState_lnkSTATE_NAME_{0}'.format(x)
                    str64=  "ContentPlaceHolder1_gvSTATECommon_LinkButton1_{0}".format(0)
                    str00 = '//a[@id="ContentPlaceHolder1_gvApplicationListState_lnkSTATE_NAME_{0}"]'.format(x)
                    state = self.driver.find_element_by_xpath(str00).text
                    try:
                        links0 = self.driver.find_element_by_id(str0).click()
                    #here I am aware of the fact that this "Stale element ..... might lead to missing some data points, It can be solved if there is time"
                    except (NoSuchElementException, StaleElementReferenceException):
                        pass
                    # no of district
                    noo2 = self.no2()
                    # print "noo2 {}".format(noo2)

                    try:
                        for y in range(1, noo2-2):
                            #pdb.set_trace()
                            # print "y {}".format(y)
                            str000 = 'ContentPlaceHolder1_gvApplicationListDistrict_LinkButton2_{0}'.format(y)
                            str0000 = '//a[@id="ContentPlaceHolder1_gvApplicationListDistrict_LinkButton2_{0}"]'.format(y)

                            district = self.driver.find_element_by_xpath(str0000).text
                            # print str000
                            try:
                                links00 = self.driver.find_element_by_id(str000).click()
                                str2 = 'ContentPlaceHolder1_gvSTATECommon_LinkButton1_{}'.format(0)
                                wait = WebDriverWait(self.driver, 20)
                                wait.until(lambda driver: driver.find_element_by_id(str2).is_displayed() == True)
                    #here I am aware of the fact that this "Stale element ..... might lead to missing some data points, It can be solved if there is time"
                            except (StaleElementReferenceException, StaleElementReferenceException):
                                pass
                            noo3=self.no3()
                            # print "noo3 {}".format(noo3)
                            #pdb.set_trace()
                            self.parse(state,district,noo3-1)
                            #pdb.set_trace()
                            try:
                                links00 = self.driver.find_element_by_id(str64).click()
                                if(y+1<=noo2-1):
                                    str2 = 'ContentPlaceHolder1_gvApplicationListDistrict_LinkButton2_{0}'.format(y+1)
                                    wait = WebDriverWait(self.driver, 20)
                                    wait.until(lambda driver: driver.find_element_by_id(str2).is_displayed() == True)

                    #here I am aware of the fact that this "Stale element ..... might lead to missing some data points, It can be solved if there is time"
                            except (NoSuchElementException, StaleElementReferenceException):
                                pass
                            
                    #here I am aware of the fact that this "Stale element ..... might lead to missing some data points, It can be solved if there is time"
                    except (NoSuchElementException, StaleElementReferenceException):
                        # print "Except me hoon "
                        pass
                    try:
                        links = self.driver.find_element_by_id(str1).click()
                        str2 = 'ContentPlaceHolder1_gvApplicationListState_lnkSTATE_NAME_{0}'.format(x+1)
                        wait = WebDriverWait(self.driver, 10)
                        wait.until(lambda driver: driver.find_element_by_id(str2).is_displayed() == True)
                    #here I am aware of the fact that this "Stale element ..... might lead to missing some data points, It can be solved if there is time"
                    except (NoSuchElementException, StaleElementReferenceException):
                        pass
                    #here I am aware of the fact that this "Stale element ..... might lead to missing some data points, It can be solved if there is time"
            except (NoSuchElementException, StaleElementReferenceException):
                # print "Bade except me hoon "
                pass

                    #here I am aware of the fact that this "Stale element ..... might lead to missing some data points, It can be solved if there is time"
        except (NoSuchElementException, StaleElementReferenceException):
            # print "hi"
            pass
    # def scrape(self):
    #     self.driver.get(self.url)
    #     noo1 = self.no1()
    #     # print noo1

if __name__ == '__main__':
    scraper = socialcops()
    scraper.scrape() 
