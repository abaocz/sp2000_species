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
        'Cookie': 'JSESSIONID=7CFCE3B79679BC13B190D102A9C28388',
        'X-CSRF-TOKEN': "8639b876-6b49-4637-aaad-07259edc9cf3",
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
        'Cookie': 'JSESSIONID=7CFCE3B79679BC13B190D102A9C28388',
        'X-CSRF-TOKEN': "8639b876-6b49-4637-aaad-07259edc9cf3",
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
    count=0
    # print(json_data[0]['id'])
    # for ids in json_data:
    ids=json_data[0]
    id = str(ids['id'])
    name = str(ids['name'])
    json_data2=req_json(id,name,0)
    ids=json_data2[1]
    id = str(ids['id'])
    name = str(ids['name'])
    json_data3=req_json(id,name,1)
    ids=json_data3[4]
    id = str(ids['id'])
    name = str(ids['name'])
    json_data4=req_json(id,name,2)
    print(json_data4)
    num=-1
    for ids in json_data4:
        num+=1
        if(num<7):
            continue
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
                    isParent=bool(ids['isParent'])
                    # print(isParent)
                    count+=1
                    print(count)
                    if(isParent):
                        test_url="http://www.sp2000.org.cn/species/show_species_details/"+id
                        # print(test_url)
                        file.writelines(test_url+"\n")
                        json_data8=req_json(id,name,6)
                        for ids in json_data8:
                            id = str(ids['id'])
                            name = str(ids['name'])
                            test_url="http://www.sp2000.org.cn/species/show_species_details/"+id
                            # print("******"+test_url)
                            file.writelines(test_url+"\n")
                    else:
                        test_url="http://www.sp2000.org.cn/species/show_species_details/"+id
                        # print(test_url)
                        file.writelines(test_url+"\n")
    file.close()    

                            

if __name__ == '__main__':
    # html = gethtml("http://www.sp2000.org.cn/browse/browse_taxa")
    # print(html+"\n")
    # result=json_data()
    openurl()
    # print(result)