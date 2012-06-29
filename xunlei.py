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
from hashlib import md5

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
        check_result_info =  self.get_cookie('check_result');
        check_result_code = \
            check_result_info.split(':')[1]
        login_url = 'http://login.xunlei.com/sec2login/'
#        login_enable    0
#        login_hour    720
#        p    5d0f7f4e758df9e366267f329d0a7e9e
#        u    firefoxmmx
#        verifycode    !ES4
        md5_maker = md5()
        md5_maker.update(password)
        
        postdata = {'u':username,
                    'p':md5_maker.hexdigest(),
                    'login_hour':0,
                    'login_hour':720,
                    'verifycode':check_result_code}
        postdata = urllib.urlencode(postdata)
        login_page = self.opener.open(login_url, postdata).read()
        print login_page
    def logout(self):
        ''' 移除登录的COOKIE数据'''
        pass
    def get_cookie(self,key):
        '''获取COOKIE里面的属性'''
        if self.cookie.has_nonstandard_attr(key):
            return self.cookie._cookies[self.domain][key].value
        else:
            return None
    def save_cookie(self):
        '''保存COOKIE到硬盘'''
        pass
    def load_cookie(self,cookiepath):
        '''载入已存在的COOKIE'''
        self.cookie = FileCookieJar(cookiepath)
        self.cookie.load()
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