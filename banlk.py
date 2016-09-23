__author__ = 'MrHowe'
# -*- coding: utf-8 -*-
#
# 1024图片爬虫

import json, time, requests,re
from bs4 import BeautifulSoup

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Host':'cl.romcl.org',
    'Cookie':'__cfduid=d47b0a15a896d4ffc54aecb2e0e9e261d1452925766; __utmt=1; __utma=228258383.1266090352.1452925763.1452925763.1452930100.2; __utmb=228258383.8.10.1452930100; __utmc=228258383; __utmz=228258383.1452925763.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); CNZZDATA950900=cnzz_eid%3D1891176549-1452925516-http%253A%252F%252Fcl.romcl.org%252F%26ntime%3D1452930274',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'
}


html_doc = requests.get('http://cl.romcl.org/thread0806.php?fid=16&search=&page=2',headers = headers)
plain = html_doc.text
soup = BeautifulSoup(plain, "html.parser")
urls = []
for link in soup.find_all('a'):
    lingshi = link.get('href')
    if type(lingshi) == type('str'):
        if lingshi[:8]=='htm_data':
            urls.append(lingshi)
print("正在根据图片网站列表获取图片...")
dowbload_links=[]
for url in urls:
    pic_html = requests.get('http://cl.romcl.org/'+url,headers = headers)
    pic_soup = BeautifulSoup(pic_html.text, "html.parser")
    for pic_tag in pic_soup.find_all('img'):
        pic_link = pic_tag.get('src')
        dowbload_links.append(pic_link)



folder_path = 'D:\pic'






