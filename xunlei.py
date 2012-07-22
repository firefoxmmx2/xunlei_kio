#!/usr/bin/env python2
# -*- coding:utf-8 -*-
'''
Created on 2012-6-15

@author: hooxin
'''

from cookielib import CookieJar, FileCookieJar, LWPCookieJar,Cookie,MozillaCookieJar
from hashlib import md5
from urllib2 import Request, HTTPCookieProcessor
import httplib
import time
import urllib
import urllib2
import os
import logging
#开启调试模式
httplib.HTTPSConnection.debuglevel=1
logging.basicConfig(level=logging.DEBUG)
def get_cachetime():
    return int(time.time() * 1000)
class Xunlei:
    def __init__(self,username=None,password=None,cookiepath=None):
        '''初始化信息数据，用户密码，已存在COOKIE'''
        self.cookiepath = cookiepath
        
        self.rootdomain = '.xunlei.com' #设置离线COOKIE ROOT域
        self.vipdomain = '.vip.xunlei.com' #迅雷vip COOKE 域
        if username is not None and password is not None:
            self.is_login = self.login(username, password) #是否登录
        
    def login(self,username,password):
        '''连接登录迅雷离线，并且吧登录信息保存在COOKIE里面'''
        try:
            self.load_cookie()
            lsessionid = self.get_cookie(self.rootdomain, 'lsessionid')
            logging.debug('coookie_lsessionid = '+repr(lsessionid) )
            if lsessionid is not None:
                return True
            else:
                self.cookie = LWPCookieJar()
        except Exception as e:
            logging.debug(e)
            self.cookie = LWPCookieJar()
            
        self.opener = urllib2.build_opener( 
                    HTTPCookieProcessor(self.cookie))
        check_url = 'http://login.xunlei.com/check'
        cachetime = get_cachetime()
        postdata = {'u':username,'cachetime':cachetime}
        postdata = urllib.urlencode(postdata)
        check_url += '?'+postdata
        login_page = self.opener.open(check_url).read()
        check_result_info =  self.get_cookie(self.rootdomain,'check_result');
        check_result_code = \
            check_result_info.split(':')[1]
        login_url = 'http://login.xunlei.com/sec2login/'
        
#        login_enable    1
#        login_hour    720
#        p    5d0f7f4e758df9e366267f329d0a7e9e
#        u    firefoxmmx
#        verifycode    !ES4

        
        postdata = {'u':username,
                    'p':md5(md5(md5(password).hexdigest()).hexdigest()
                            +check_result_code.upper())
                            .hexdigest(),
                    'login_enable':1,
                    'login_hour':720,
                    'verifycode':check_result_code}
        postdata = urllib.urlencode(postdata)
        login_page = self.opener.open(login_url, postdata).read()
        lsessionid = self.get_cookie(self.rootdomain,'lsessionid')
        logging.debug('lsessionid =' + repr(lsessionid) );
        if lsessionid is not None:
            return True
        else:
            return False
        
    def logout(self):
        ''' 移除登录的COOKIE数据'''
        if self.is_login:
            logout_url = 'http://login.xunlei.com/unregister?sessionid=' \
            +self.get_cookie(self.rootdomain, 'sessionid')
#            vip_ckeys = ["vip_isvip","lx_sessionid","vip_level","lx_login",
#                     "dl_enable","in_xl","ucid","lx_login_u","rw_list_open"]
#            root_ckeys1 = ["sessionid","usrname","nickname","usernewno",
#                      "lsessionid","luserid","userid","vip_paytype"]
            root_ckeys1 = ["sessionid","usrname","nickname","usernewno",
                      "lsessionid","luserid","userid"]
#            for i in vip_ckeys:
#                self.remove_cookie(self.vipdomain , i)
            for i in root_ckeys1:
                self.remove_cookie(self.rootdomain, i)
            self.set_cookie(self.vipdomain,'lx_nf_all',
                            'page_check_all=commtask&fltask_all_guoqi=0&\
            class_check=0&page_check=task&fl_page_id=0&class_check_new=0')
            self.set_cookie(self.rootdomain,'menu_isopen','0')
            
    def remove_cookie(self,domain,key):
        '''移除COOKIE对应属性'''
        self.cookie.clear(domain, '/', key)
    def get_cookie(self,domain,key):
        '''获取COOKIE里面的属性'''
        try:
            return self.cookie._cookies[domain]['/'][key].value
        except Exception:
            return None
    def save_cookie(self):
        '''保存COOKIE到硬盘'''
        self.cookie.save(self.cookiepath,True, True)
    def set_cookie(self,domain,key,value):
        '''设置cookie属性的值'''
        cookie_ = Cookie(version=0, 
                                name=key, 
                                value=value,
                                discard=True,
                                domain=domain,
                                domain_initial_dot=False,
                                domain_specified=True,
                                expires=None,
                                path="/",
                                path_specified=False,
                                port=None,
                                port_specified=False,
                                secure=False,
                                comment=None,
                                comment_url=None,
                                rest={},)
        
        self.cookie.set_cookie(cookie_)
    def load_cookie(self):
        '''载入已存在的COOKIE'''
        self.cookie = LWPCookieJar()
        self.cookie.load(self.cookiepath,True,True)
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
    
    account_file = open(os.environ['HOME']+os.sep+'.xunlei','r')
    username = account_file.readline()[:-1]
    password = account_file.readline()[:-1]
    cookie_path = account_file.readline()[:-1]
    account_file.close()
    xl = Xunlei(username,password,os.path.expanduser(cookie_path))
    print (xl.get_cookie(xl.rootdomain, 'lsessionid'))
  
    xl.logout()
    print (xl.get_cookie(xl.rootdomain, 'lsessionid'))
    xl.save_cookie()  
