#!/usr/bin/env python2
# -*- coding:utf-8 -*-
'''
Created on 2012-6-15

@author: hooxin
'''

import httplib
from cookielib import CookieJar,FileCookieJar,LWPCookieJar
import urllib2
import urllib
from urllib2 import Request,HTTPCookieProcessor
import time

#开启调试模式
httplib.HTTPSConnection.debuglevel=1

def get_cachetime():
    return int(time.time() * 1000)
class Xunlei:
    def __init__(self,username=None,password=None,cookiepath=None):
        '''初始化信息数据，用户密码，已存在COOKIE'''
        self.cookiepath = cookiepath
        if self.cookiepath is not None:
            self.load_cookie(self.cookiepath)
            self.opener = urllib2.build_opener( 
                    HTTPCookieProcessor(self.cookie))
        self.domain = 'xunlei.com' #设置离线COOKIE域
        
    def login(self,username,password,cookiepath=None):
        '''连接登录迅雷离线，并且吧登录信息保存在COOKIE里面'''
        if cookiepath is not None:
            self.cookiepath = cookiepath
            self.cookie = self.load_cookie(cookiepath)
        else:
            self.cookie = CookieJar()
        self.opener = urllib2.build_opener( 
                    HTTPCookieProcessor(self.cookie))
        check_url = 'http://login.xunlei.com/check'
        postdata = {'u':username,'cachetime':get_cachetime()}
        postdata = urllib.urlencode(postdata)
        check_url += '?'+postdata
        login_page = self.opener.open(check_url).read()
        
        pass
    def logout(self):
        ''' 移除登录的COOKIE数据'''
        pass
    def get_cookie(self,key):
        '''获取COOKIE里面的属性'''
        self.cookie._cookies[self.domain][key].val
        pass
    def save_cookie(self):
        '''保存COOKIE到硬盘'''
        pass
    def load_cookie(self,cookiepath):
        '''载入已存在的COOKIE'''
        pass
    def urlopen(self,url,**kwargs):
        '''打开连接，过滤掉自己不需要的信息'''
        pass
    def urlread(self):
        '''读取需要的部分'''
        pass
    def add_task(self,task):
        '''向离线空间添加任务'''
        pass
    def remove_task(self,task):
        '''移除离线的任务信息 '''
        pass
    def update_task(self,task):
        ''' 修改离线任务的内容'''
        pass
    def get_task_list(self):
        ''' 通过连接打开,通过__parse_task解析HTML元素 \
        返回一个任务列表'''
        pass
    def __parse_task(self,html):
        '''解析HTML元素，返回TASK列表'''
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
        
    def download(self):
        pass

if __name__ == '__main__':
    xl = Xunlei()
    xl.login('firefoxmmx', 'missdark')
    pass