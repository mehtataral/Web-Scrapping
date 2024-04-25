# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:09:23 2023

@author: Livewire
"""

# pip install requests
# pip install beautifulsoup4

# Beautiful Soup is a library that makes it easy to scrape information from web pages.
# Requests HTTP Library
# ~~~~~~~~~~~~~~~~~~~~~

# Requests is an HTTP library, written in Python, for human beings.
# Basic GET usage:    b

# .find() - it is used for searching first element 
# .find_all() - it gives all element from the HTML file    



import requests
import bs4

url = input("Enter your url")
response = requests.get(url)
# print(type(response))
# print(response.text)  #it gives whole code of 
# https://www.cricbuzz.com/live-cricket-scores/45951/mi-vs-kkr-14th-match-indian-premier-league-2022 
# https://pandawebology.com/   https://www.mojarto.com/artworks/digitalart?pageNumber=0
filename ="temp.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")
bs
formatted_data = bs.prettify()
print(formatted_data)

# 200 =ok
# 301 =moved permanently
# 302 =found
# 304 =not modified
# 403 =forbidden
# 404 =not found
# 410 =gone
# 503 =service unavailable

status = response.status_code
status
if response.status_code ==200:
    print("Connection Successfull")
else:
    print('Connection Failed')
# data = open(r"C:\Users\user\Desktop\webscrapping\temp.html","w")
# data.write(formatted_data)



tag = bs.find_all(class_ = "cb-col cb-col-100")
tag

country  = []
for x in range(len(tag)):
    country.append(tag[x].text)


data = []
tag = bs.find(id = "main_table_countries_today")
tag
len(tag)





for x in tag.find_all("tr"):
    nested_list = []
    for y in x.find_all("td"):
        nested_list.append(y.get_text())
    data.append(nested_list)
    


import pandas as pd
pd.DataFrame(data)
#***************************img TAG  *************************************
list_img = bs.find('img') #fetch first img tag
print(list_img)

list_img = bs.find_all('img')
print(list_img)

no_of_img = len(list_img)
print(no_of_img)

print(list_img[-1])

for x in list_img:
    print(x,"\n\n")

#***************************a & p  TAG  **************************

list_a = bs.find_all('a')
print(list_a)
print(list_a[-1])

no_of_a = len(list_a)
print(no_of_a)

p_tag =bs.find_all('h1')#for loop niche che
print(p_tag)

p_tag[-1].text

print(p_tag[-1])
print(len(p_tag))

prices =bs.find_all(text ="₹")
print(prices)


id_class = bs.find(class_ ="cb-com-ln cb-col cb-col-100") # last line from HTML scripting code
print(id_class)
print(id_class.text)


id_class = bs.find(class_ ="cb-com-ln cb-col cb-col-90") # last line from HTML class code
print(id_class)
print(id_class.text)

#***************************title head and body TAG  **************************
title  = bs.title.text # gets you the text of the <title>(...)</title>
title

title = bs.title
title


head = bs.head.text
head

head = bs.head
head 

body =bs.body.text
body

body = bs.body
body

#***************************Extract first <h1>(...)</h1> text **************************
#Perform a CSS selection operation on the current element.
# By using select method we can run a CSS selector and get all matching elements. 
# We can find tags also by using select method.
first_head = bs.select('h1')
first_head

first_head = bs.select('style')[0].text
first_head
 
first_head = bs.select('style')[0]
first_head

first_head = bs.select('style')[1].text
first_head

first_head = bs.select('style')[1]
first_head


first_head = bs.select('style')[-1].text
first_head

first_head = bs.select('style')[-1]
first_head
#*********************************SAME ************************************
# first_head = bs.find_all('style')
# first_head
# len(first_head)

first_head = bs.select('style')
first_head
len(first_head)

first_head = bs.select('style')[-1]
first_head

sec_head = bs.select('div')
sec_head
len(sec_head)

sec_head = bs.select('div')[-1]
sec_head
len(sec_head)

sec_head=bs.select('div span')
sec_head
len(sec_head)


sec_head=bs.select('div > span')
sec_head
len(sec_head)


print(bs.select("a:nth-of-type(even)")) 

print(bs.select("a:nth-of-type(odd)")) 

#*******************************************************************

# thr_head  = bs.select('div.es_spinner_image')
# thr_head[0].get_text()

#***************************************************************************

# ctrl + shift + i
# ctrl + shift + c

data1 =  bs.find_all(class_ ="cb-pos-rel")
data1
len(data1)
data1[0]
data1[1]
data1[2]
data1[3]
data1[13]
data1


data1 =  bs.find_all(class_ ="text-hvr-underline suggested-video-gtm")
len(data1)
data1
data1[0]
data1[1]
data1[2].text


data2 =  bs.find(class_ ="text-hvr-underline suggested-video-gtm")#fetch first tag
data2
data2.text


file2= open(r"C:\Users\user\Desktop\cricket_info_v2.txt","a",encoding="utf-8")

data3 = bs.find_all("p")
data3
len(data3)

data3_list=[]

for x in range(len(data3)):
    data3_list.append(data3[x].text)

print(data3_list)

print(len(data3_list))

for i in range(len(data3)):
    print(data3_list[i])
    file2.write("\n")
    file2.write(data3_list[i])
    file2.write("\n")
file2.close()

---------------------------------

url  =input("Enter any url")
# https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=117;type=trophy


response = requests.get(url)

if response.status_code == 200:
    print("successful connection")
else:
    print("connection failed")

filename ="cric.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")
bs
len(bs)
formatted_new_data = bs.prettify()
print(formatted_new_data)



a1 = bs.find_all("a")
print(a1)
print(len(a1))
print(a1[0].text)
print(a1[2].text)
print(a1[10].text)
print(a1[15].text)
print(a1[18].text)
print(a1[180].text)
print(a1[181].text)

print(a1[210].text)
print(a1[211].text)
print(a1[105].text)

a2 = bs.find_all("p")
print(len(a2))
print(a2)
print(a2[0].text)

a3 = bs.find_all("img")
print(a3)
print(len(a3))

print(a3[0].text)


a4 = bs.find_all(class_ = "ds-text-tight-s ds-font-regular ds-text-typo-primary hover:ds-text-typo-primary-hover ds-block")
print(a4)
len(a4)
print(a4[0].text)
file3= open(r"C:\Users\user\Desktop\most runin ipl.txt","a",encoding="utf-8")
file3= open(r"C:\Users\user\Desktop\most runin ipl1.xls","a",encoding="utf-8")
file3= open(r"C:\Users\user\Desktop\most runin ipl3.xls","a",encoding="utf-8")

a5 = []

for x in range(len(a4)):
    a5.append(a4[x].text)
import pandas as pd
pd.DataFrame(a5)
print(a5)
len(a5)
print(a5[46])
print(a5[40])
print(a5[1])
print(a5[12])
print(a5[0])

for i in range(len(a4)):
    file3.write(a5[i])
    file3.write("' ' \t ' ' ")

file3.close()

