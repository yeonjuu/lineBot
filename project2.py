# -*- coding: utf-8 -*-
import csv
#import numpy
import pandas

datas = pandas.read_csv('C:\\Users\\COM\\python\\추정유동인구.csv', sep = ",", encoding='euc-kr')
# print(datas.shape)
# print(datas.columns)
dt2 = datas[['기준_년월_코드','총_유동인구_수','남성_유동인구_수','여성_유동인구_수']]
print(dt2)

#print(datas)