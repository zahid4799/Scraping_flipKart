from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib.request
import pandas as pd


driver = webdriver.Chrome('E:\\chromedriver\\chromedriver_win32 (1)\\chromedriver.exe') //from local drive
def page_load(url):
    driver.get(url)
    time.sleep(3)
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    return soup
def pagination(page_count):
    basic_url='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page='
    new_page=basic_url+str(page_count)
    return new_page
master_list=[]
for i in range(1,407,1):
    page_count=i
    content=page_load((pagination(page_count))).find_all("div",{"class":"_3pLy-c row"})
    for c in content:
        data_dict={}
        try:
            data_dict['name']=c.find("div",{"class":"_4rR01T"}).text
        except:
            data_dict['name']='No Data'
        try:
            data_dict['rating']=c.find("div",{"class":"_3LWZlK"}).text
        except:
            data_dict['rating']='No Data'
        try:
            data_dict['rating_number']=c.find("span",{"class":"_2_R_DZ"}).text
        except:
            data_dict['rating_number']='No Data'
        try:
            specs=c.find("ul",{"class":"_1xgFaf"}).find_all("li",{"class":"rgWa7D"})
            holder=' '
            for spec in specs:
                specification=spec.text
                holder=holder+','+specification
            holder=holder[2:]
            data_dict['specs_all']=holder
        except:
            data_dict['specs_all']='No Data'
        try:
            data_dict['price']=c.find("div",{"class":"_30jeq3 _1_WHN1"}).text
        except:
            data_dict['price']='No Data'
        master_list.append(data_dict)
flipkart_df=pd.DataFrame(master_list)
flipkart_df.to_csv('flipkart.csv',index=False)