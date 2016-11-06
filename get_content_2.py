import requests

#定义一系列字典：
urls_dict={
    '电子工业出版社':'http://www.phei.com.cn/',
    '在线资源':'http://www.phei.com.cn/module/zygl/zxzyindex.jsp',
    'xyz':'www.phei.com.cn',
    '网上书店 1':'http://www.phei.com.cn/module/goods/wssd_index.jsp',
    '网上书店 2':'http://www.phei.com.cn/module/goods/wssd_index.jsp'
}


#定义列表：
urls_list=[
    ('电子工业出版社','http://www.phei.com.cn/'),
    ('在线资源','http://www.phei.com.cn/module/zygl/zxzyindex.jsp'),
    ('xyz','www.phei.com.cn'),
    ('网上书店 1','http://www.phei.com.cn/module/goods/wssd_index.jsp'),
    ('网上书店 2','http://www.phei.com.cn/module/goods/wssd_index.jsp'),
]


#利用字典抓取：
get_urls_for_dict=set()
for ind,name in enumerate(urls_dict.keys()):
    name_url=urls_dict[name]
    if name_url in get_urls_for_dict:
        print(ind,name,'已经抓取过了；')
    else:
        try:
            resp=requests.get(name_url)
        except Exception as e:
            print(ind,name,':',str(e)[0:50])
            continue
        content=resp.text
        get_urls_for_dict.add(name_url)
        with open("bydict_"+name+'.html','w',encoding='utf8') as f:
            f.write(content)
            print("抓取完成：{} {}，内容长度为{}".format(ind,name,len(content)))
for u in get_urls_for_dict:
    print(u)
print('-'*60)


#利用列表抓取：
get_urls_for_list=set()
for ind,tup in enumerate(urls_list):
    name=tup[0]
    name_url=tup[1]
    if name in get_urls_for_list:
        print(ind,name,'已经抓取过了；')
    else:
        try:
            resp=requests.get(name_url)
        except Exception as e:
            print(ind,name,':',str(e)[:50])
            continue
        content=resp.text
        get_urls_for_list.add(name_url)
        with open('bylist_'+name+'.html','w',encoding='utf8') as f:
            f.write(content)
            print("抓取完成：{} {}，内容长度为{}".format(ind,name,len(content)))

for u in get_urls_for_list:
    print(u)