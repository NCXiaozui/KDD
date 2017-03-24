# -*- coding: utf-8 -*-
__author__ = 'XYlaner'
'''
  pick the features of  from weather.cvs file
'''
import csv
import datetime

path = '/home/xy/Data/WeatherAverageData/Av_Wea_C_1.csv'
outfile = '/home/xy/Data/WeatherAverageData/Av_Wea_C_1_week.csv'
def readfile(file_in,file_out):
    csvfile = file(file_in,'r')
    reader = csv.reader(csvfile)
    csvfile = file(file_out,'w')
    writer = csv.writer(csvfile)


    i = 0
    for line in reader :
        if i == 0:
            line.append('week')
            print line
            writer.writerow(line)
            i += 1
        else:
            date = line[0].split('/')
            print date
            print date[0],date[1],date[2].split(' ')[0]
            #week = datetime.date(int(line[0][0:4]),int(line[0][5:7]),int(line[0][8:10])).weekday()
            week = datetime.date(int(date[0]), int(date[1]), int(date[2].split(' ')[0])).weekday()
            line.append(week)
            writer.writerow(line)



if __name__ == '__main__':
    readfile(path,outfile)

