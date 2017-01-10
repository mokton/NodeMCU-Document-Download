# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:10:48 2017

@author: Angus
"""

import urllib2
import os

modules = ["adc","adxl345","am2320","apa102","bit","bme280",
            "bmp085","cjson","coap","crypto","dht","encoder","enduser-setup",
            "file","gpio","hmc5883l","http","hx711","i2c","l3g4200d","mdns",
            "mqtt","net","node","ow","pcm","perf","pwm","rc","rotary",
            "rtcfifo","rtcmem","rtctime","sigma-delta","sntp","somfy","spi",
            "struct","switec","tm1829","tmr","tsl2561","u8g","uart","ucg",
            "wifi","ws2801","ws2812","cron"]

css = ["http://nodemcu.readthedocs.io/en/master/css/theme.css",
       "http://nodemcu.readthedocs.io/en/master/css/theme_extra.css",
       "http://nodemcu.readthedocs.io/en/master/css/highlight.css",
       "http://nodemcu.readthedocs.io/en/master/css/extra.css",
       "https://media.readthedocs.org//css/badge_only.css",
       "https://media.readthedocs.org//css/readthedocs-doc-embed.css"]
       
js = ["http://nodemcu.readthedocs.io/en/master/js/jquery-2.1.1.min.js",
      "http://nodemcu.readthedocs.io/en/master/js/modernizr-2.8.3.min.js",
      "http://nodemcu.readthedocs.io/en/master/js/highlight.pack.js",
      "http://nodemcu.readthedocs.io/en/master/js/theme.js",
      "http://nodemcu.readthedocs.io/en/master/js/extra.js",
      "https://media.readthedocs.org/static/core/js/readthedocs-doc-embed.js",
      "http://nodemcu.readthedocs.io/en/master/readthedocs-data.js",
      "http://nodemcu.readthedocs.io/en/master/readthedocs-dynamic-include.js"]

def get_page(url):  
    
    page = ""
    for i in range(3):
        try:
            myheaders = {'Connection':'Keep-Alive',
                         "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36"}
            req = urllib2.Request(url, headers = myheaders)
            res = urllib2.urlopen(req, timeout = 15)
            page = res.read()
            break
        except Exception, msg:
            print "[-] Error getting html:", msg
    return(page) 

# level: dev or master
def download(level = "dev", single = False, module = ""):
    home = "http://nodemcu.readthedocs.io/en/" + level + "/en/modules/"
    direct_path = os.path.abspath(os.curdir) + "/" + level
    if not os.path.exists(direct_path):
        os.mkdir(direct_path) #在本地新建文件夹
    if single:
        try:
            url = home + module
            html = get_page(url)
            if html <> "":
                filename = direct_path + "/" + module + ".html"
                f = open(filename, "w")
                f.write(html)
                f.close()
                print(module + " is done.")
            else:
                print(module + " is empty.")
        except Exception, e:
            print e
    else:
        for m in modules:
            try:
                url = home + m
                html = get_page(url)
                if html <> "":
                    filename = direct_path + "/" + m + ".html"
                    f = open(filename, "w")
                    f.write(html)
                    f.close()
                    print(m + " download is done.")
                else:
                    print(m + " is empty.")
            except Exception, e:
                print e

def replace_content(level = "dev", single = False, module = ""):
    direct_path = os.path.abspath(os.curdir) + "/" + level
    if not os.path.exists(direct_path):
        os.mkdir(direct_path) 
    if single:
        try:
            filename = direct_path + "/" + module + ".html"
            f = open(filename, "r")
            content = str(f.read())
            f.close()
            content = content.replace("../../../css/", "css/")
            content = content.replace("https://media.readthedocs.org//css/", "css/")
            #print(content)
            f = open(filename, "w")
            f.write(content)
            f.close()
            print(module + " replace is done.")
        except Exception, e:
            print e
    else:
        for m in modules:
            try:
                filename = direct_path + "/" + m + ".html"
                f = open(filename, "r")
                content = str(f.read())
                f.close()
                content = content.replace("../../../css/", "css/")
                content = content.replace("https://media.readthedocs.org//css/", "css/")
                content = content.replace("../../../js/", "js/")
                content = content.replace("https://media.readthedocs.org/static/core/js/", "js/")
                content = content.replace("../../../readthedocs", "js/readthedocs")
                #print(content)
                f = open(filename, "w")
                f.write(content)
                f.close()
                print(m + " replace is done.")
            except Exception, e:
                print e
                
def css_js(level = "dev"):
    direct_path = os.path.abspath(os.curdir) + "/" + level + "/css"
    if not os.path.exists(direct_path):
        os.mkdir(direct_path) 
    for url in css:
        try:
            html = get_page(url)
            fn = os.path.basename(url)
            if html <> "":
                filename = direct_path + "/" + fn
                f = open(filename, "w")
                f.write(html)
                f.close()
                print(fn + " download is done.")
            else:
                print(fn + " is empty.")
        except Exception, e:
            print e
    direct_path = os.path.abspath(os.curdir) + "/" + level + "/js"
    if not os.path.exists(direct_path):
        os.mkdir(direct_path) 
    for url in js:
        try:
            html = get_page(url)
            fn = os.path.basename(url)
            if html <> "":
                filename = direct_path + "/" + fn
                f = open(filename, "w")
                f.write(html)
                f.close()
                print(fn + " download is done.")
            else:
                print(fn + " is empty.")
        except Exception, e:
            print e

if __name__ == "__main__":
    #modules.sort()
    #for m in modules:
    #    print(m)
    #level = "master" # no cron module
    level = "dev"
    download(level=level)
    #download(level=level, single=True,module="cron")
    replace_content(level=level)
    #replace_content(level=level, single=True,module="cron")
    css_js(level=level)
