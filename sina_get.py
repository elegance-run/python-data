from Data.get_content import *

url='http://www.sina.com.cn'

sina_content=get_content(url)

print("____________________________")
print("sina_get得到内容前500个字符：",sina_content[:500])
print("sina_get得到的内容长度：",len(sina_content))