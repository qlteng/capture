# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import logging
from screen_shot import capture
import pandas as pd

def read_company_list(path):
    company_list = []
    data = pd.read_csv(path,encoding='GB18030',header=None)

    for i in range(0,len(data)):
        company_list.append(data.iloc[i][0]) 
    
    return company_list

def run(web_dict, path):
    
    item_list = read_company_list(path)

    for key in web_dict:
    
        store_path = "./picture/%s" % key
        if not os.path.exists(store_path):
            os.mkdir(store_path)
        
        url_list = []
   
        if key in ["chinatax", "chinasafety","creditchina","mnr","gkml"]:
        
            url_list = [web_dict[key].format(x) for x in item_list]
            for x in url_list:
                print (x)
        
        elif key in ["mee", "customs", "mee", "zxgk"]:
        
            url_list = [web_dict[key]]
        
        else:
            pass
    
        capture(url_list, item_list, store_path, key)
    

def main(path):
    
    web_dict1 = {
                     
            "chinasafety":"http://www.chinasafety.gov.cn/search/?sw={}",
#            "mnr":"http://s.lrn.cn/search/search.do?webid=6&pg=20&tpl=103&channelid=&searchword=&q={}&x=0&y=0",
            "mee":"http://www.mee.gov.cn/"
            }
#    web_dict1 = {}
    web_dict2 = {
            "zxgk" : "http://zxgk.court.gov.cn/shixin/"}
#    web_dict2={}

    for web_dict in [web_dict1, web_dict2]:
        
        run(web_dict, path)
        
        logging.info("%s done" % web_dict1.keys())

    
if(__name__=='__main__'):
    
    path = 'item.csv'
    main(path)
    
    

