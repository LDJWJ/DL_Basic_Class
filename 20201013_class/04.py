# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:14:07 2020

@author: user
"""

#%%
from bs4 import BeautifulSoup

html = """
<html>
<head><title> test site </title></head>
<p class='class1' align="left">test3</p>
<p class='class1'>test2</p>
<p id='p1'>오늘의 주가지수 1500</p>
<span class='class3'>span tag text</span>
<p class='class4'>test3</p>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

print( list(soup.children)  )
print( list(soup.body.children)  )

#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = 'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after'
basic_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page="
# 2page 
# 3page

#%%
url1 = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"
page = urlopen(url1)
soup = BeautifulSoup(page, "html.parser")
comment_all = soup.find_all('td', class_='title')
print( comment_all )

#%% 개수 확인 
print(len( comment_all )) 

#%% 
print( comment_all[0] ) 

#%% 
ch_td = list(comment_all[5].children )
print( ch_td[6].strip() )

#%% 여러개 댓글 가져오기
cnt = 0
comments = []
for comment in comment_all:
    temp = list(comment.children)
    result = temp[6].strip()
    # print(result)
    comments.append(result)

print(comments)

#%% 1-7페이지
comments = []
cnt = 0

basic_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page="

for i in range(1,8):
    url = basic_url + str(i)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    
    comment_all = soup.find_all("td", class_="title")
    
    for comment in comment_all:
        temp = list(comment.children)
        result = temp[6].strip()
        # print(result)
        comments.append(result)

print(len(comments))
print(comments)

#%%
from wordcloud import WordCloud, STOPWORDS

import numpy as np
from PIL import Image

#%%
import os
print( os.getcwd() )

#%%

f = open("스파이더맨리뷰.csv", encoding="utf-8")
#f = open("SpiderMan.txt", 'r', encoding='utf-8')
text = f.read()
f.close()


#%%
from matplotlib import rc
rc('font', family='NanumGothic')


#%%
%matplotlib inline
from wordcloud import WordCloud
wcloud = WordCloud('./data/D2Coding.ttf', max_words=1000, relative_scaling = 0.2).generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


