# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:42:32 2019

@author: mannerzhao
"""

import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from PIL import ImageGrab

def capture(urls, pic_list, prefix, keyword):

    chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver" 
    chromedriver = "C:/Users/qlteng/AppData/Local/Google/Chrome/Application/chromedriver" 
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    browser.maximize_window() 
    
    for index in range(len(pic_list)):
        
        if keyword in ["mnr","chinatax", "creditchina", "chinasafety","gkml"] :
            
            browser.get(urls[index])
            time.sleep(1)
            if keyword == "chinasafety":
                js="var q=document.documentElement.scrollTop=0"
                browser.execute_script(js)
                time.sleep(random.uniform(0.8,1))
            
            
        elif keyword in ["mee","customs"]:
            
            browser.get(urls[0])
            if keyword == "customs":
                time.sleep(5)
            elem = None
            for searchword_id in ["ess_ctr126388_ListC_Info_ctl00_KEYWORDS","searchword", "schword", "gover_search_key"]:
                try:
                    elem = browser.find_element_by_id(searchword_id)
                except:
                    pass
                
            if elem == None:
                logging.error("Can't find right searchword element in the url %s" % (urls[0]))
                continue
            
            elem.click()
            
            elem.send_keys(pic_list[index])
            time.sleep(random.random())
            elem.send_keys(Keys.ENTER)
        
        elif keyword in ["zxgk"]:
            
            browser.get(urls[0])
            
            elem_input = None
            
            for input_id in ["ID_codeName", "objName", "pName"]:
                try:
                    elem_input = browser.find_element_by_id(input_id)
                except:
                    pass
                
            if elem_input == None:
                logging.error("Can't find right searchword element in the url %s" % (urls[0]))
                continue
            
            elem_input.click()

            elem_input.send_keys(pic_list[index])
            
            
            elem_ocr = None
            for ocr_id in ["ID_randomCode", "ycode", "yzm"]:
                try:
                    elem_ocr = browser.find_element_by_id(ocr_id)
                except:
                    pass
            if elem_ocr == None:
                logging.error("Can't find right ocr element in the url %s" % (urls[0]))
                continue
            
            elem_ocr.click()
            time.sleep(0.5)
            ocr = input("请在下方输入当前网站上的验证码，回车结束\n")
            elem_ocr.send_keys(ocr)
            
            time.sleep(0.5)
            
            elem_bn = None
            
            if keyword == "zxgk":
                elem_bn = browser.find_element_by_class_name("btn-zxgk")
            if elem_bn == None:
                logging.error("Can't find right button element in the url %s" % (urls[0]))
                continue
            elem_bn.click()
                
        path = "%s/%s.png"%(prefix , pic_list[index])
        im = ImageGrab.grab()
        im.save(path,'jpeg')
        time.sleep(0.5)
        
    browser.close()
