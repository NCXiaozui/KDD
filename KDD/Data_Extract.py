# -*- coding: UTF-8 -*-
__author__ = 'XYlander'

import pandas as pa
import os

file_list = os.listdir('/home/xy/Data/KDD/data/train/')
print file_list
file_out_feature = '/home/xy/Data/KDD/data/train_feature.txt'
file_out_target = '/home/xy/Data/KDD/data/train_target.txt'

out_feature = open(file_out_feature,'w')
out_target = open(file_out_target,'w')

def read_file():
    for file in file_list:
        print file
        data = pa.read_csv('/home/xy/Data/KDD/data/train/' + file)
        for index,row in data.iterrows(): #迭代获得数据
            if row[u'date'] in ['2016-10-11','2016-10-12','2016-10-13','2016-10-14','2016-10-15','2016-10-16','2016-10-17'] :
                out_feature.write('%d %d %d %.2f %.2f %.2f %.2f\n'% (float(row[u'date'][-2:]),float(row[u'hour'][0:2]),float(row[u'hour'][3:5]),float(row[u'wind_direction']),float(row[u'wind_speed']),float(row[u'last_av_time']),float(row[u'now_av_time'])))
                out_target.write('%f\n'%(float(row[u'average_time'])))


if __name__ == '__main__':
    read_file()
