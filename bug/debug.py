# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree
import json
import string
import os, sys
from googletrans import Translator
tr = Translator(timeout=10)
pagename = 'MC-4'
try:
    try:
        os.remove('bug_cache_text.txt')
    except Exception:
        pass
    url_str ='https://bugs.mojang.com/si/jira.issueviews:issue-xml/'+ str.upper(pagename) + '/' + str.upper(pagename) + '.xml'
    respose_str =  requests.get(url_str,timeout=10)
    try:
        respose_str.encoding = 'utf-8'
        root = ElementTree.XML(respose_str.text)
        for node in root.iter("channel"):
            for node in root.iter("item"):
                Title = node.find("title").text
                Titleg = tr.translate(node.find("title").text,dest='zh-cn').text
                Type = "类型：" + node.find("type").text
                Project = "项目：" + node.find("project").text
                TStatus = "进度：" + tr.translate(str(node.find("status").text),dest='zh-cn').text
                Resolution = "状态：" + tr.translate(str(node.find("resolution").text),dest='zh-cn').text
                Link = node.find("link").text
        url_json = 'https://bugs.mojang.com/rest/api/2/issue/'+str.upper(pagename)
        json_text = requests.get(url_json,timeout=10)
        file = json.loads(json_text.text)
        Versions = file['fields']['versions']
        for item in Versions[:]:
            name = item['name']+"|"
            y = open('bug_cache_text.txt',mode='a',encoding='utf-8')
            y.write(name)
            y.close()
        z = open('bug_cache_text.txt',mode='r',encoding='utf-8')
        j = z.read()
        m = j.strip(string.punctuation)
        if m.split('|')[0] == m.split('|')[-1]:
            Version = "版本："+m.split('|')[0]
        else:
            Version = "版本："+m.split('|')[0]+"~"+m.split('|')[-1]
        try:
            Priority = "Mojang优先级："+tr.translate(file['fields']['customfield_12200']['value'],dest='zh-cn').text
            print(Title+'\n'+Titleg+'\n'+Type+'\n'+Project+'\n'+TStatus+'\n'+Priority+'\n'+Resolution+'\n'+Version+'\n'+Link+'\n'+"由Google翻译提供支持。")
            z.close()
            os.remove('bug_cache_text.txt')
        except Exception:
            print(Title+'\n'+Titleg+'\n'+Type+'\n'+Project+'\n'+TStatus+'\n'+Resolution+'\n'+Version+'\n'+Link+'\n'+"由Google翻译提供支持。")
    except Exception:
        try:
            respose_str.encoding = 'utf-8'
            root = ElementTree.XML(respose_str.text)
            for node in root.iter("channel"):
                for node in root.iter("item"):
                    Title = node.find("title").text
                    Titleg = tr.translate(node.find("title").text,dest='zh-cn').text
                    Type = "类型：" + node.find("type").text
                    TStatus = "进度：" + tr.translate(node.find("status").text,dest='zh-cn').text
                    Resolution = "状态：" + tr.translate(node.find("resolution"),dest='zh-cn').text
                    Priority = "优先级：" + tr.translate(node.find("priority"),dest='zh-cn').text
                    Link = node.find("link").text
                    print(Title+'\n'+Titleg+'\n'+Type+'\n'+TStatus+'\n'+Priority+'\n'+Resolution+'\n'+Link+'\n'+"由Google翻译提供支持。")
        except Exception:
            try:
                respose_str.encoding = 'utf-8'
                root = ElementTree.XML(respose_str.text)
                for node in root.iter("channel"):
                    for node in root.iter("item"):
                        Link = node.find("link").text
                        print(Link)
            except Exception as e:
                print("发生错误："+str(e)+".")
except Exception as e:
    print("发生错误："+str(e)+".")