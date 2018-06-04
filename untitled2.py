# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:31:40 2018

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 08:31:18 2018

@author: lenovo
"""

#1.导包
import urllib.request as r
import json
import time


#2.欢迎界面
print('欢迎使用城市天气查询系统')
time.sleep(1)
a=input('尊敬的使用者，您是第一次使用本系统吗？ 请输入：YES  or  NO ')
#判断选择
#3.城市查询
z=Choose_Information(a)
if z=="1":
         city='leshan'
         print(Check_Information(city))
elif z=="2":
         city=input('请输入城市拼音：')
         print(Check_Information(city))
else:
        city=input('请输入您所需要保存信息的城市拼音')
        Save_City_name(city)   
        
def Choose_Information(a):
    if a=='YES':
        time.sleep(1)
        print('欢迎第一次使用天气查询系统')
        time.sleep(1)
        z=input('菜单是：1.查看当前城市天气   2.查看其它城市天气  3.天气信息存储')
    else:
        time.sleep(1)
        z=input('菜单是：1.查看当前城市天气   2.查看其它城市天气  3.天气信息存储')
    return(z)

    ##保存函数
  
information_weather=[]  
def Check_Information(city):  #信息查询  
    city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996 ".format(city)
    info=r.urlopen(city_address).read().decode('utf-8','ignore')
    data=json.loads(info)
    index=int(len(data['list']))
    for i in range(0,index):
        day=data['list'][i]
        time=day['dt_txt']
        temp=day['main']['temp']
        description=day['weather'][0]['description']
        temp_max=day['main']['temp_max']
        pressure=day['main']['pressure']
        information_weather=('{} 当前时间{}温度为{}，天气情况{}，最高温度{}，气压为{}'.format(city,time,temp,description,temp_max,pressure))
        #print(information_weather)
        return(information_weather)
    return(information_weather)




def Save_City_name(city):#4.信息存储
    city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996 ".format(city)
    info=r.urlopen(city_address).read().decode('utf-8','ignore')
    data=json.loads(info)
    index=int(len(data['list']))
    information_weather=[]
    fo = open("foo.txt", "w")
    for i in range(0,index):
            day=data['list'][i]
            time=day['dt_txt']
            temp=day['main']['temp']
            description=day['weather'][0]['description']
            temp_max=day['main']['temp_max']
            pressure=day['main']['pressure']
            information_weather=('{} 当前时间{}温度为{}，天气情况{}，最高温度{}，气压为{}'.format(city,time,temp,description,temp_max,pressure))
            fo.write('information_weather\n')
    fo.close()
    
    
print ("文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)
print ("末尾是否强制加空格 : ",fo.softspace)

 
# 关闭打开的文件
fo.close()


#5.打包程序,

