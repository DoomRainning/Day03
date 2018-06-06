# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:29:43 2018

@author: lenovo
"""
import urllib.request as r
import json

url1="http://www.gaokaopai.com/university-ajaxGetMajor.html"
#header body url
params1="id=477&type=2&city=51&state=1".encode()
headers1={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
         "Connection":"keep-alive",
         "X-Requested-With":"XMLHttpRequest"}
req1=r.Request(url1,params1,headers1)#Ctrl + i
data1=r.urlopen(req1).read().decode("utf-8","ifnore")
print(data1)
open('./gaokaopai_L.txt','a',encoding="utf-8").write(data1+'/n')


info=json.loads(data1)
print(info['data'][0]['school'])

# readlines 将文本中所有的元素读成列表list
ls=open('./all_school.txt','r',encoding='utf-8').readlines()
len(ls)#查看列表长度

kemu=[1,2]#文理科

city=[11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,50,51,52,53,54,61,62,63,64,65]

for i in ls:#学校
    ls.append(i[:-5].split("-")[2].split(".")[0])

    
f.open('.urls.txt','a')
for city in citys:#全中国文科招生
    for i in ids:
        p='id={}&type={}%state=1'
        p.format(i,1,city)
        f.write(p.format(i,1,city)+'\n')
            
for i in ids:#全中国理科招生
    for city in citys:#城市
        p='id={}&type={}%state=1'
        p.format(i,2,city)
        f.write(p.format(i,2,city)+'\n')
f.close()
            




# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:04:36 2018

@author: yq
"""
kemus=[1,2]#文理科
#全国城市
citys=[11 , 12 , 13 , 14 , 15 , 21 , 22 , 23 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 41 , 42 , 43 , 44 , 45 , 46 , 50 , 51 , 52 , 53 , 54 , 61 , 62 , 63 , 64 , 65]
#全国高校编号
ids=[]
s='北京大学	北京	http://www.gaokaopai.com/daxue-jianjie-477.html'
s[:-5].split("-")[2]
#readlines() 一次性将文件所有行读出来，是list
ls=open('./all_school.txt','r',encoding='utf-8').readlines()
len(ls)

for i in ls:
    ids.append(i[:-5].split("-")[2].split('.')[0])


f=open('./urls.txt','a')
for i in ids:#全中国高效文科招生
    for city in citys:#城市
        p='id={}&type={}&city={}&state=1'
        f.write(p.format(i,1,city)+'\n')
for i in ids:#全中国高效理科招生
    for city in citys:#城市
        p='id={}&type={}&city={}&state=1'
#        print(p.format(i,2,city))
        f.write(p.format(i,2,city)+'\n')
f.close()
"""
文科-四川-乐山师范学院
理科-四川-乐山师范学院
文科-成都-乐山师范学院
理科-成都-乐山师范学院

"""
  









