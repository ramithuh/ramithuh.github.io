from mimetypes import guess_extension
from shutil import copyfile
import time
import pandas as pd
import os
import urllib.request
import wget
import math
from os.path import basename
import subprocess as sub

df=pd.read_csv('/Users/ramith/final-match-cv.csv') 
base_path='/Users/ramith/RUR_19_CV'

def isNaN(num):
    return num != num

def file_name(one,two):

    for entry in two:
        
        if entry not in one:
            return entry

for index, row in df.iterrows():
    pre_dir = os.listdir(base_path + '/all')
    
    companies = [row['interview1'],row['interview2'],row['interview3']]
    
    reg = row['registrationNumber']
    print(reg)
    cvUrl = row['cvUrl']
    print(cvUrl)
    
    s='curl -O ' + cvUrl
    subp.check_call(str(s), shell=True)
    
    time.sleep(10)
    now_dir = os.listdir(base_path + '/all')
    
    file = file_name(pre_dir,now_dir)
    
    for company in companies:
        #print(company)
        if company not in os.listdir(base_path) and not isNaN(company):
            os.makedirs(base_path + '/' + company)
        
        if not isNaN(company):
            print(file)
            copyfile(base_path + 'all/' + file , base_path + '/' + company + '/' + reg + '_' + file)
    
    print(reg)
    break
    """    
    extension = guess_extension(cv.info()['Content-Type'])

    if extension:
        print(reg + cv.url)
        with open(base_path + '/' +reg + extension,'wb') as output:
              output.write(cv_file)
    else:
        # what to do? discard?
        print("__ERROR " + reg)

        pass"""

    #print(row['registrationNumber'], row['interview1'])