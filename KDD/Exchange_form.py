# -*- coding: UTF-8 -*-


__author__ = 'XYlander_Peng'

import csv
import time

def exchange_formation(file_in,file_out_feature,file_out_target):
    csvfile = file(file_in, 'r')
    reader = csv.reader(csvfile)
    feature_txt = open(file_out_feature,'a+')
    target_txt = open(file_out_target,'a+')
    fina_txt = open('/home/xy/Data/KDD/final.txt','a+')
    flag = 0
    for line in reader:
        if flag == 0:
            flag = 1
            continue
        else:
            for i in range(0,len(line)):
                #print i

                if i < len(line) - 1:
                    if i == 0 :
                        feature_txt.write('%d ' % (float(line[i][-2:]))) #记录日期
                        fina_txt.write('%s ' % (line[i]))
                        continue
                    if i == 2 :
                        target_txt.write('%.5f\n'%(float(line[i])))
                        continue
                    if i == 1 :
                        print line[i],line[i][0:2],line[i][3:5] #我们将小时和分钟分开来记录
                        feature_txt.write('%d %d '%(float(line[i][0:2]),float(line[i][3:5])))
                    if i == 6 or i == 7 or i == 48 :
                        feature_txt.write('%.2f '%(float(line[i])))
                    fina_txt.write('%s ' % (line[i]))


                else:
                    feature_txt.write('%.2f\n'%(float(line[i])))
                    fina_txt.write('%s\n' % (line[i]))

    feature_txt.close()
    target_txt.close()

if __name__ == '__main__':
    file_in = '/home/xy/Data/KDD/predict_data/C_3_pred.csv'
    file_out_feature = '/home/xy/Data/KDD/pred_feature.txt'
    file_out_target = '/home/xy/Data/KDD/pred_target.txt'
    exchange_formation(file_in,file_out_feature,file_out_target)