# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
def login(username,password):
    hosturl = 'http://sep.ucas.ac.cn/'  
    posturl = 'http://sep.ucas.ac.cn/slogin'  
    cj = cookielib.LWPCookieJar()  
    cookie_support = urllib2.HTTPCookieProcessor(cj)  
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
    urllib2.install_opener(opener)  
    
    h = urllib2.urlopen(hosturl)  
    headers = {'Host':'sep.ucas.ac.cn',
               'Origin':'http://sep.ucas.ac.cn',
               'Referer' : 'http://sep.ucas.ac.cn/',
               'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36',  
              }  
    postData = {'userName' : username,   
                'pwd' : password,  
                'sb'  : 'sb',
                'rememberMe':'1'
               }  
    postData = urllib.urlencode(postData)  
    request = urllib2.Request(posturl, postData, headers)  
    #print request  
    response = urllib2.urlopen(request)  
    #text = response.read()  
    #print text  
    ChooseClassSysUrl = 'http://sep.ucas.ac.cn/portal/site/226/821'
    ClassSys = urllib2.urlopen(ChooseClassSysUrl)
   
    ClassText = ClassSys.read()
    #print ClassText
    soup = BeautifulSoup(ClassText)
    test = soup.find('noscript')
    ClassUrl = test.contents[1].attrs['content'][6:]
    #print ClassUrl
    GetClassSysText = urllib2.urlopen(ClassUrl)
    ClassTextUrl = 'http://jwjz.ucas.ac.cn/Student/DeskTopModules/Left.aspx'
    request1 = urllib2.urlopen(ClassTextUrl)
    #print request1.read()
    ChooseClassTextUrl = 'http://jwjz.ucas.ac.cn/Student/DeskTopModules/Course/CourseManage.aspx'
    request2 = urllib2.urlopen(ChooseClassTextUrl)
    return request2.read()




