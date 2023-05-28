## 导包
import json
import requests as rq
from bs4 import BeautifulSoup as bs
import requests
import re
from openpyxl import Workbook, load_workbook

def req_json(id,name,lv):
    head = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        'Cookie': 'JSESSIONID=E0363C9354DDFB548FA36626FE37A60D',
        'X-CSRF-TOKEN': "762c1458-ff20-49e2-8151-52b603c95cb2",
    }
    data1 = {
        'id': id,
        'name': name,
        'lv': lv,
        'otherParam': 'zTreeAsyncTest'
    }
    url_response1 = requests.post("http://www.sp2000.org.cn/browse/taxa_tree_children", data=data1, headers=head,timeout=60* 10)

    json_obj1 = json.loads(url_response1.text)
    # print(json_obj1)
    return json_obj1


def openurl():
    head = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        'Cookie': 'JSESSIONID=E0363C9354DDFB548FA36626FE37A60D',
        'X-CSRF-TOKEN': "762c1458-ff20-49e2-8151-52b603c95cb2",
    }
    data={
        #'id':'',
        'name': '',
        'lv': 0,
        'otherParam':'zTreeAsyncTest'
    }
    url_response = requests.post("http://www.sp2000.org.cn/browse/taxa_tree_children", data= data, headers=head,timeout=60* 10)
    json_data=json.loads(url_response.text)
    file = open("file.txt", "w")
    # print(json_data)
    # print(json_data[0])
    # print(json_data[0]['id'])
    for ids in json_data:
        id = str(ids['id'])
        name = str(ids['name'])
        json_data2=req_json(id,name,0)
        for ids in json_data2:
            id = str(ids['id'])
            name = str(ids['name'])
            json_data3=req_json(id,name,1)
            for ids in json_data3:
                id = str(ids['id'])
                name = str(ids['name'])
                json_data4=req_json(id,name,2)
                for ids in json_data4:
                    id = str(ids['id'])
                    name = str(ids['name'])
                    json_data5=req_json(id,name,3)
                    for ids in json_data5:
                        id = str(ids['id'])
                        name = str(ids['name'])
                        json_data6=req_json(id,name,4)
                        for ids in json_data6:
                            id = str(ids['id'])
                            name = str(ids['name'])
                            json_data7=req_json(id,name,5)
                            for ids in json_data7:
                                id = str(ids['id'])
                                name = str(ids['name'])
                                test_url="http://www.sp2000.org.cn/species/show_species_details/"+id
                                print(test_url)
                                file.writelines(test_url+"\n")
    file.close()    

                            
                        


def gethtml(rooturl, encoding="utf-8"):
    # 默认解码方式utf-8
    response = rq.get(rooturl)
    response.encoding = encoding
    html = response.text
    return html  # 返回链接的html内容

def getherf(html):
    # 使用BeautifulSoup函数解析传入的html
    soup = bs(html, features="lxml")
    allnode_of_a = soup.find_all("a")
    result = [_.get("href") for _ in allnode_of_a]
    # print(result)
    return result

def filterurl(result):
    # result参数：get到的所有a标签内herf的内容
    # 对列表中每个元素进行筛选
    urlptn = r"http://(.+)"  # 匹配模式: 所有http://开头的链接
    urls = [re.match(urlptn, str(_)) for _ in result]  # 正则筛选
    # print(urls)
    while None in urls:
        urls.remove(None)  # 移除表中空元素
    urls = [_.group() for _ in urls]  # group方法获得re.match()返回值中的字符
    # print(urls)
    return urls

if __name__ == '__main__':
    # html = gethtml("http://www.sp2000.org.cn/browse/browse_taxa")
    # print(html+"\n")
    # result=json_data()
    openurl()
    # print(result)