from Data.get_content import *

url='http://www.sina.com.cn'

sina_content=get_content(url)

print("---------------------------------------")
print("sina_get得到内容前60个字符：",sina_content[:60])
print("sina_get得到的内容长度：",len(sina_content))