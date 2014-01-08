# -*- coding: utf-8 -*-
import os
import json
from time import time,sleep
import webbrowser
#os.chdir("D:\hacksen\michaelliao-sinaweibopy-4a93870\src")
from weibo import APIClient
import pdb
import urllib2
import urllib
APP_KEY = '1102114376'
APP_SECRET = '0f1edba57330f68c4fffc543c4a018de'
CALLBACK_URL = 'http://fluthear.blog.163.com'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url
webbrowser.open(url)
params=urllib.urlencode({
'action':'login',
'display':'default',
'withOfficalFlag':0,
'withOfficalAccount':'',
'scope':'',
'ticket':'ST-MTM0NTc4MzEyMA==-1388418481-xd-2F6ACE603A16BF4B7224AB4CD93BF56E',
'isLoginSina':'',
'response_type':'code',
'regCallback':'https%3A%2F%2Fapi.weibo.com%2F2%2Foauth2%2Fauthorize%3Fclient_id%3D1102114376%26response_type%3Dcode%26display%3Ddefault%26redirect_uri%3Dhttp%3A%2F%2Ffluthear.blog.163.com%26from%3D%26with_cookie%3D',
'redirect_uri':'http://fluthear.blog.163.com',
'client_id':'1102114376',
'appkey62':'1M8S2Q',
'state':'',
'verifyToken':'null',
'from':"",
'userId':"jacins",
'passwd':"311yzfs" }
)
#req = urllib2.Request(url)
#resp = urllib2.urlopen(req)
#body = resp.read()
#print body
#url='https://api.weibo.com/oauth2/authorize'
#req = urllib2.Request(url,params)
#resp = urllib2.urlopen(req)
#rediurl= resp.geturl()
#print rediurl

#code=input('请输入PIN码:').strip()
code=raw_input()
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)
while 1:
    #friends_timeline=client.get.statuses__friends_timeline()
   # pdb.set_trace()
    home_timeline=client.get.statuses__home_timeline()
    #a=json.dumps(friends_timeline.values(),indent=4,ensure_ascii=False)
    b=json.dumps(home_timeline.values(),indent=4,ensure_ascii=False)
    f=open("123." + str(time()) + ".txt" ,'w')
    #f.write(a.encode("UTF-8"))
    f.write(b.encode("gb18030"))
    f.close()
    count_down=20
    while count_down :
        sleep(2)
        count_down-=1
        print count_down
    
