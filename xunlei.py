#!/usr/bin/env python2
# -*- coding:utf-8 -*-
'''
Created on 2012-6-15

@author: hooxin
'''

import httplib
#开启调试模式
httplib.HTTPSConnection.debuglevel=1

class Xunlei:
    def __init__(self,username,password,cookiepath):
        pass
    def login(self,username,password,cookiepath):
        pass
    def logout(self):
        pass
    def get_cookie(self,domain,key):
        pass
    def save_cookie(self):
        pass
    def load_cookie(self):
        pass
    def urlopen(self,url,**kwargs):
        pass
    def urlread(self):
        pass
    def add_task(self,task):
        pass
    def remove_task(self,task):
        pass
    def update_task(self,task):
        pass
    def get_task_list(self):
        pass
    def __parse_task(self,html):
        pass
    
    
class Task:
    def __init__(self):
        self.id=''
        self.name=''
        self.origin_link=''
        self.size=0
        self.dl_link=''
        self.dcid=''
        self.durl=''
        self.furl=''
        self.dstatus=''
        self.dtasktype=''
        self.ref_url=''
        self.verity=''
        self.ifvod=''
        self.vodurl=''
        self.openformat=''
        self.progress = ''
        self.speed=''
        
    def download(self):
        pass
    

class BtTask(Task):
    def __init__(self):
        super(BtTask, self).__init()
        
        