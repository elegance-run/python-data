import requests

def get_content(url):
    resp=requests.get(url)
    return resp.text


if __name__=="__main__":
    url="http://www.phei.com.cn"

    content=get_content(url)

    print("前50个字符：",content[:50])

    content_len=len(content)
    print("内容的长度为：",content_len)

    if content_len>=40*1024:
        print("内容的长度大于40KB；")
    else:
        print("内容的长度小于40KB；")

    #第一种方式的文件写入与读取：
    #写入：
    print('-'*20)
    print('方式一写入：','文件写入')
    f1=open('home_page.html','w',encoding='utf8')
    f1.write(content)
    f1.close()

    #读取：
    print('方式一读取：','文件读取')
    f2=open("home_page.html",'r',encoding='utf8')
    content_read=f2.read()
    print('方式一读取的前50个字符为：',content_read[:50])
    f2.close()

    #第二种方式的文件写入与读取：
    #写入：
    print('-' * 20)
    print('方式二写入：', '文件写入')
    with open('home_page.html', 'w', encoding='utf8') as f3:
        f3.write(content)


    #读取：
    print('方式二读取：', '文件读取')
    with open('home_page.html','r',encoding='utf8') as f4:
        content_read_2=f4.read()
        print('方式二读取的前50个字符为：', content_read_2[:50])