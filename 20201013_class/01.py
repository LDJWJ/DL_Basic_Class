# -*- coding: utf-8 -*-

#%%
from bs4 import BeautifulSoup

html = "<p>test</p>"
soup = BeautifulSoup(html, 'lxml')
print(soup)

#%%
from bs4 import BeautifulSoup

html = "<p>test</p>"
soup = BeautifulSoup(html, 'html5lib')
print(soup)


#%%
from bs4 import BeautifulSoup

html = "<p>test</p>"
soup = BeautifulSoup(html, 'html.parser')
print(soup)

#%%


#%%
from bs4 import BeautifulSoup

html = """
<html>
<head><title>나의 웹페이지</title></head>
<p>test1</p>
<p>test2</p>
<p>test3</p>
</html>
"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title   # soup 내부의 title 정보를 가져온다. 가정 첫번째 것만 해당됨.
print(tag_title.text)    # 정보 
print(tag_title.name)
print(type(soup))

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
print( soup.p )

#%%
print( soup.p.attrs )

#%% 
print( soup.p['class'] )
      
#%%
from bs4 import BeautifulSoup
html = """
<html>
<head><title> text와 string의 차이 </title></head>
<p>
    <span>test1</span>
    <span>test2</span>
    <span><b>test3</b></span>
</p>
</html>
"""
soup = BeautifulSoup(html, 'lxml')
tag_p = soup.p # soup 내부의 title 정보를 가져온다. 가정 첫번째 것만 해당됨.

data_text = tag_p.text
data_string = tag_p.string
data_span_str = tag_p.span.string

# text를 이용한 하위 정보 전체 출력 
print(data_text, type(data_text) )

# string을 이용한 현재 내용에 대해서만 출력 
print(data_string, type(data_string) )

# string을 이용한 span 태그의 첫번째 줄에 대해서만 출력
print(data_span_str)
      
#%%
from bs4 import BeautifulSoup

page = open("mypage.html", 'r', encoding="utf-8").read()
page

#%%
soup = BeautifulSoup(page, 'lxml')
print( soup )
     
print(soup.prettify())
      
#%%
print(list(soup.children))
      
#%%
soup_children_list = list(soup.children)
soup_children_list

#%%
tmp = list(soup_children_list[1].children)
print(tmp)

















