# Eastmoney_hotwords
东方财富热搜词数据接口

# 输入参数 
该数据接口只需要输入一个参数，即为要爬取网页的页数：page_num

原数据网址为：
https://guba.eastmoney.com/default,99_page_num.html

比如page_num = 3时，爬取的网页的网址为：
https://guba.eastmoney.com/default,99_1.html
https://guba.eastmoney.com/default,99_2.html
https://guba.eastmoney.com/default,99_3.html

# 数据提取
所要提取的数据是网页中，列名为“标题”数据中所出现的所有股票和基金名称名称。

# 计算
提取所有股票和基金名称后，对其进行去重，然后计算每只股票或者基金所出现的次
数，次数越多，说明当日该标的在市场受关注的程度越高。

#输出为DataFrame形式
1.“股票”列为网页中被提及过的股票或者基金名称
2.“被提及次数”列为各标的在网页中出现的次数
3.表格以“被提及次数”列为标准，进行降序排列
