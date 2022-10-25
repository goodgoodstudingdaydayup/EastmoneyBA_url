# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
        

    
def web_url(page_num):
    url = []
    for i in range(1,page_num+1):
        url.append('https://guba.eastmoney.com/default,99_'+str(i)+'.html')
    
    return url

def web_get(url):
        ret = requests.get(url).text
        pro1 = BeautifulSoup(ret, "lxml")
        pro2 = pro1.find_all(name='div',attrs={"class":"balist"})[0]
        pro3 = pro2.find_all(name='li')
        m = len(pro3)
        
        main1 = []
        for i in range(0,m):
            main1.append(pro3[i].find_all(name='a')[0].contents[0])
            
        main2 = []
        for i in range(0,m):
            try:
                main2.append(re.match(r'([\s\S]*?)吧',main1[i])[0])
            except:
                pass
            
        m = len(main2)
        main3 = []
        for i in range(0,m):
            try:
                main3.append((re.sub(r'吧','',main2[i])))
            except:
                pass  
    

        
        return main3

def web_get_sum(page_num):
     url = web_url(page_num)
     m = len(url)
     
     main = []
     for i in range(0,m):
         main.append(web_get(url[i]))
         
     pro1 = []
     for i in range(0,m):
         pro1 += main[i]
         
     pro1_uni =list(set(pro1))
     mm = len(pro1_uni)
     countt = [0]*mm
     for i in range(0,mm):
         countt[i] = pro1.count(pro1_uni[i])
         
     df = pd.DataFrame({'股票':pro1_uni,
                        '被提及次数':countt})
     
     dfin = df.sort_values(by = '被提及次数',ascending = False)
     
     return dfin


     
         

    
    
    

        
        
