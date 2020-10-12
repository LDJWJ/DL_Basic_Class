# -*- coding: utf-8 -*-

#%%
from bs4 import BeautifulSoup

page = open("mypage.html", 'r', encoding="utf-8").read()
# print(page)

soup = BeautifulSoup(page, "html.parser")
print(soup)
#%%
# 헤드라인1을 가져오기

data = soup.find("h1")
print(data.text)

# 단락1 정보 가져오기
p1 = soup.find("p")
print(p1.text)

#%% 실습 2-1 구글 논문 링크 정보 가져오기
link_txt = soup.find("a")
print(link_txt.text)

#%% a 태그로 연결된 전체 정보를 가져온다.
link_all = soup.find_all('a')
# print(link_all)

for i in link_all:
    print(i.text)
    
#%% 실습 3-1 p태그 전체 정보를 가져와서,  text출력해 보기
link_p = soup.find_all("p")

for i in link_p:
    print(i.text)

#%% 네이버 가져오기
link_p = soup.find_all("a")
print(link_p[2].text)








