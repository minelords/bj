from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import random
import re
def browser(url):  #返回html信息
    # 创建 Chrome WebDriver 实例，并添加代理选项
    opt = webdriver.ChromeOptions()
    opt.add_argument("--proxy-server=http://localhost:2080")
    opt.add_argument(f'user-agent={UserAgent().Chrome}')
    opt.add_argument("--headless") 
    #eager加载策略加速
    opt.page_load_strategy = 'eager'
    driver=webdriver.Chrome(options=opt)  
    driver.get(url)
    time.sleep(1)
    html=driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
    tag= soup.find_all("div", {"class":"responsive-player"})
    #print(tag[0])
    pattern=re.compile(r'.*?src="(.*?)"',re.S)
    myurl=pattern.findall(str(tag[0]))
    print(myurl)
    m3u8=get_m3u8(myurl[0])
    return m3u8

def get_m3u8(url):
    proxies = {
            'http': 'http://127.0.0.1:2080',
            'https': 'http://127.0.0.1:2080',
        }
    headers={
            'User-Agent': f'{UserAgent().Chrome}'
        }
    res=requests.get(url=url,proxies=proxies,headers=headers)
    #print(res.text)
    html=res.text
    pattern=re.compile(r'file:"(https://.*?)"}]',re.S)
    myurl=pattern.findall(html)
    print(myurl[0])
    return myurl


if __name__=="__main__":
    url='https://sexbjcam.com/2024/06/11/kbj24061106_eunyoung1238_20240209/'
    browser(url)