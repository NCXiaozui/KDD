# -*- coding: UTF-8 -*-

__author__ = 'XYlander'

'''
 @ This code is using GBDT for solving KDD 2017 task 1
'''

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor


def Set_GBDT():  #Set GBDT model parameter
    gbdt = GradientBoostingRegressor(
        loss='ls'     #loss function huber / ls
        , learning_rate=0.1
        , n_estimators=1000
        , subsample=0.9
        , min_samples_split=2
        , min_samples_leaf=1
        , max_depth= 7
        , init=None
        , random_state=None
        , max_features=None
        , alpha=0.9
        , verbose=0
        , max_leaf_nodes=None
        , warm_start=False
    )
    return gbdt


def train_model(file_feature,file_target,GBDT):
    train_feat = np.genfromtxt(file_feature,dtype=np.float32)
    train_target = np.genfromtxt(file_target,dtype=np.float32)
    GBDT.fit(train_feat,train_target)
    print GBDT.feature_importances_




def predict(file_predict,GBDT,exam):
    file_predict = np.genfromtxt(file_predict, dtype=np.float32)
    exam = np.genfromtxt(exam, dtype=np.float32)
    pred = GBDT.predict(file_predict)
    total_err = 0
    for i in range(pred.shape[0]):
        print pred[i], exam[i]
        err = abs(pred[i] - exam[i]) #/ exam[i]
        total_err = total_err + err
    print total_err / pred.shape[0]

    return pred

def output(final,pred):
    final_file = open(final,'r')
    result_file = open('/home/xy/Data/KDD/final_result_ls.txt','w')
    i = 0
    for line in final_file:
        line = line.strip('\n').split(' ')
        #print line
        line.append(str(pred[i]))
        i += 1
        result_file.write('%s\n'%(','.join(line)))
    result_file.close()
    final_file.close()



if __name__ == '__main__':
    file_feature = '/home/xy/Data/KDD/data/train_feature.txt' #训练特征数据
    file_target = '/home/xy/Data/KDD/data/train_target.txt'   #训练目标数据
    file_predict = '/home/xy/Data/KDD/data/test/pred_feature.txt' #测试特征数据
    #exam = '/home/xy/Data/KDD/test_target.txt'          #对照数据
    exam = '/home/xy/Data/KDD/data/test/pred_target.txt'
    final = '/home/xy/Data/KDD/final.txt'


    GBDT = Set_GBDT()
    train_model(file_feature,file_target,GBDT)
    pred = predict(file_predict,GBDT,exam)
    output(final,pred)
