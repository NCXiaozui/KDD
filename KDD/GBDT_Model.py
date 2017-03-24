# -*- coding: UTF-8 -*-

__author__ = 'XYlander'

'''
 @ This code is using GBDT for solving KDD 2017 task 1
'''

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

def Set_GBDT():  #Set GBDT model parameter
    gbdt = GradientBoostingRegressor(
        loss='huber'     #loss function
        , learning_rate=0.1
        , n_estimators=1000
        , subsample=0.8
        , min_samples_split=2
        , min_samples_leaf=1
        , max_depth=3
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
    train_feat = np.genfromtxt(file_feature, dtype=np.float32)
    train_target = np.genfromtxt(file_target,dtype=np.float32)
    GBDT.fit(train_feat,train_target)
    print GBDT.feature_importances_



def predict():
    pass

if __name__ == '__main__':
    file_feature = '/home/xy/Data/KDD/feature.txt'
    file_target = '/home/xy/Data/KDD/target.txt'
    GBDT = Set_GBDT()
    train_model(file_feature,file_target,GBDT)
    predict()
