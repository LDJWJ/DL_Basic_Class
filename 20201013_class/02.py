# -*- coding: utf-8 -*-

#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

#%%
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
print(soup)

#%%
print(soup.find_all('span', id='KOSDAQ_now')[0].text)  # 코스닥)
print(soup.find_all('span', id='KOSPI_now')[0].text)   # 코스피)\
print(soup.find_all('span', id='KPI200_now')[0].text)  # 코스피200 )


#%% 코스피 지수 관련 정보 얻기
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"

#%%
#%%
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
print(soup.title)
print(soup)


#%% 
# 거래량 및 거래대금 가져오기
# 거래량 : td , id : quant
deal = soup.find("td", id="quant")
print("오늘의 코스피 거래량 :", deal )

#%%
deal_money = soup.find("td", id = "amount")
print("오늘의 코스피 거래대금 :", deal_money )

#%%
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

quant = soup.find("td", id = "quant").text            # 거래량(천주)
high_value = soup.find("td", id = "high_value").text  # 장중 최고
low_value = soup.find("td", id = "low_value").text    # 장중 최저
print(quant, high_value, low_value)


#%%
dat = soup.find("div", class_="subtop_sise_detail")
high = dat.find_all("td", class_="td")[2].text
low = dat.find_all("td", class_="td2")[2].text

print("52주 최고", high)
print("52주 최저", low)


#%% 예외
url = "https://finance.naver.com/item/main.nhn?code=000100"
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
print(soup.title)

#%%
# no_today 검색
dat = soup.find('p', class_='no_today').find('span', class_='blind').text
print(dat)

#%% 
dat = soup.find('p', class_='no_today')
dat01 = dat.find("span", class_="blind").text
print(dat01)

#%% QA
no_today = soup.find("span", class_= "blind").text            # 현재가
print("유한양행 현재 거래가:",no_today)








