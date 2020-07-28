import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

dbname=input("Enter the db name:")
connect.connect(dbname)

olx_url="https://www.olx.in/items/q-yamaha-rx100?isSearchCall=true"

scraped_info_list=[]


req=requests.get(olx_url)
content=req.content

soup = BeautifulSoup(content,"html.parser")
all_bikes=soup.find_all("div",{"class":"IKo3_"})

for bike in all_bikes:
        bike_dict={}
        bike_dict["prices"]= bike.find("span",{"class":"_89yzn"}).text

        try:
            bike_dict["year"]=bike.find("span",{"class":"_2TVI3"}).text
        except AttributeError:
            pass

        bike_dict["title"]=bike.find("span",{"class":"_2tW1I"}).text
        bike_dict["address"]=bike.find("span",{"class":"tjgMj"}).text
        scraped_info_list.append(bike_dict)
        connect.insert_into_table(dbname, tuple(bike_dict.values()))

dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("olx.csv")
connect.get_bike_info(dbname)
