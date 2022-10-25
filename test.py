# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:29:46 2022

@author: acer
"""


import unittest  
import Eastmoney_hotwords as ea

class TestStudent(unittest.TestCase):
    main = ea.EastmoneyBA_url.web_get_sum(10)


#运行单元测试	
if __name__ == '__main__':
	unittest.main()
