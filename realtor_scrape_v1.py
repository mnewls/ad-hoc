# https://www.landsoftexas.com/Coryell-County-TX/all-land/

from multiprocessing.sharedctypes import Value
from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path 

import pandas as pd

# open each - grab date, job title, location - these will be different cols in the excel.
# 

from openpyxl import Workbook

import html5lib

from selenium.webdriver.support.ui import Select

# to find links
from bs4 import BeautifulSoup
import urllib.request

import time # to sleep

def get_page_info(driver):

    #https://www.landsoftexas.com/Coryell-County-TX/all-land/
    #https://www.gtar.com/active-agents/
    #https://www.gtar.com/index.php?src=directory&view=rets_agents&srctype=rets_agents_lister&pos=30,30,1709
    # ^^ page 2 info
    #https://www.gtar.com/index.php?src=directory&view=rets_agents&srctype=rets_agents_lister&pos=60,30,1709
    #page 3 info

    url_str = r'https://www.gtar.com/active-agents/'

    #https://www.landsoftexas.com/zip-75555/all-land/

    #print(url_str)

    driver.get(url_str)

    time.sleep(2)

    #print(driver.find_element_by_xpath("//*[@id='content']/div[1]/div[1]/div[1]/text()").getText())

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html5lib")

    #price_list = soup.findAll("div", {"class": "cell affiliate box-shadow"})

    realtor_list = soup.findAll("div", {"class": "aff-info-inner"})

    #print(realtor_list)
    #test_text = price_list[1].text

    #test_filter = test_text[test_text.find(start:='>')+len(start):test_text.find('<')]

    #print(test_filter)
    names = []
    companies = []
    emails = []
    phones = []

    
    #print(test_break)

    #acreage_list = soup.findAll("span", {"class": "_1a278"})


    for realtor in realtor_list:

        #print(price.text)

        this_realtor = realtor.text

        #print(this_realtor)

        #print("break")

        filter = this_realtor[this_realtor.find(start:='>')+len(start):this_realtor.find('<')]

        #print(type(filter))

        break_up_data = filter.split(' ')

        break_up_data[:] = [x for x in break_up_data if x]

        #print(break_up_data)
        #print(type(break_up_data))

        #remove_1_data = break_up_data.remove('')

        #print(remove_1_data)

        #filter_empty = filter(lambda x: x, break_up_data)

        #print(filter_empty)

        first_name = break_up_data[1]
        last_name_raw = break_up_data[2]
        last_name = last_name_raw[:-2]

        company = break_up_data[3]
        company_2_raw = break_up_data[4]
        company_2 = company_2_raw.replace(',', '')

        #email = break_up_data[12]d
        exist_count_email = break_up_data.count('Email:')

        if exist_count_email >= 1:
            email_idx = break_up_data.index('Email:')
            email_idx_real = email_idx + 1
            email = break_up_data[email_idx_real]
        else:
            email = 'null'

            #print(type(break_up_data))
        exist_count = break_up_data.count('Office:')


        if exist_count >= 1:
            phone_idx = break_up_data.index('Office:')
            phone_idx_real = phone_idx + 1
            phone = break_up_data[phone_idx_real]
        else:
            phone = 'null'


        full_name = first_name + ' '+ last_name
        full_company = company + ' ' + company_2



        names.append(full_name)
        companies.append(full_company)
        emails.append(email)
        phones.append(phone)
        ##add code here to summ prices

    #print(first_page_frame.head(5))

    #print('done')

    #print(soup.prettify())

    #https://www.gtar.com/index.php?src=directory&view=rets_agents&srctype=rets_agents_lister&pos=30,30,1709
    # ^^ page 2 info

    #https://www.gtar.com/index.php?src=directory&view=rets_agents&srctype=rets_agents_lister&pos=60,30,1709
    #page 3 info

    #https://www.gtar.com/index.php?src=directory&view=rets_agents&srctype=rets_agents_lister&pos=90,30,1709

    #https://www.gtar.com/index.php?src=directory&view=rets_agents&srctype=rets_agents_lister&pos=1680,30,1709

    iter_a = 57
    iter_b = 30
    iter_c = 30
    total_num = 1709

    for x in range(iter_a):

        url_str = r'https://www.gtar.com/index.php?src=directory&view=rets_agents&srctype=rets_agents_lister&pos=' + str(iter_b) + ',' + str(iter_c) + ',' + str(total_num)

        #https://www.landsoftexas.com/zip-75555/all-land/

        #print(url_str)

        driver.get(url_str)

        iter_b = iter_b + 30

        time.sleep(2)

        #print(driver.find_element_by_xpath("//*[@id='content']/div[1]/div[1]/div[1]/text()").getText())

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html5lib")

        #price_list = soup.findAll("div", {"class": "cell affiliate box-shadow"})

        realtor_list = soup.findAll("div", {"class": "aff-info-inner"})

        #print(realtor_list)
        #test_text = price_list[1].text

        #test_filter = test_text[test_text.find(start:='>')+len(start):test_text.find('<')]

        #print(test_filter)
        
        #print(test_break)

        #acreage_list = soup.findAll("span", {"class": "_1a278"})


        for realtor in realtor_list:

            #print(price.text)

            this_realtor = realtor.text

            #print(this_realtor)

            #print("break")

            filter = this_realtor[this_realtor.find(start:='>')+len(start):this_realtor.find('<')]

            #print(type(filter))

            break_up_data = filter.split(' ')

            break_up_data[:] = [x for x in break_up_data if x]

            #print(break_up_data)
            #print(type(break_up_data))

            #remove_1_data = break_up_data.remove('')

            #print(remove_1_data)

            #filter_empty = filter(lambda x: x, break_up_data)

            #print(filter_empty)

            first_name = break_up_data[1]
            last_name_raw = break_up_data[2]
            last_name = last_name_raw[:-2]

            company = break_up_data[3]
            company_2_raw = break_up_data[4]
            company_2 = company_2_raw.replace(',', '')

            #email = break_up_data[12]
            exist_count_email = break_up_data.count('Email:')

            if exist_count_email >= 1:
                email_idx = break_up_data.index('Email:')
                email_idx_real = email_idx + 1
                email = break_up_data[email_idx_real]
            else:
                email = 'null'

            #print(type(break_up_data))
            exist_count = break_up_data.count('Office:')


            if exist_count >= 1:
                phone_idx = break_up_data.index('Office:')
                phone_idx_real = phone_idx + 1
                phone = break_up_data[phone_idx_real]
            else:
                phone = 'null'


            full_name = first_name + ' '+ last_name
            full_company = company + ' ' + company_2



            names.append(full_name)
            companies.append(full_company)
            emails.append(email)
            phones.append(phone)
            ##add code here to summ prices


    first_page_dict = {'names': names, 'companies': companies, 'emails': emails, 'phone numbers': phones}

    first_page_frame = pd.DataFrame(first_page_dict)

    filepath = Path(r'C:\Users\Michael\Desktop\Python\realtor_scrape\out.csv') 

    first_page_frame.to_csv(filepath)

    #print(first_page_frame)
    

def get_info():
 

    

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(executable_path=r'C:\Users\Michael\Desktop\Python\Automate Application\chromedriver.exe', chrome_options=options)

    get_page_info(driver)
    


get_info()