import requests

def get_content(url):
    resp=requests.get(url)
    return resp.text

if __name__=='__main__':
    url = "http://www.phei.com.cn"

    content = get_content(url)

    print('前50个字符：', content[:50])

    content_len = len(content)
    print('内容的长度为：', content_len)

    if content_len >= 40 * 1024:
        print('内容长度大于等于40KB；')
    else:
        print('内容长度小于等于40KB；')