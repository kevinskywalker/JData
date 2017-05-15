# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:57:19 2017

@author: liujiacheng1
"""

import pandas as pd
import numpy as np
import time 

time=str(time.time())


def merge(filename_a,filename_b,how,on):
    
    file_a=pd.read_csv(filename_a)
    file_b=pd.read_csv(filename_b)
    file_c=pd.merge(file_a,file_b,on=on,how=how)
    file_c.to_csv('new_data'+time+'.csv')
    
    

#merge('JData_Product.csv','JData_Comment.csv','left','sku_id')   

def run(time,name):
    action=pd.read_csv(name)
    print('ok')
    #action=action.sortby('user_id')
    action=pd.get_dummies(action,columns=['type','model_id','cate'])
    print('ok')
    action['new']=action['user_id']*1000000+action['sku_id']
    action=action.groupby('id').sum()
    action.to_csv('action_sortpin'+time+'.csv')
    
    
    
    
run(time,'JData_Action_0301_0315.csv')
run(time,'JData.csv')