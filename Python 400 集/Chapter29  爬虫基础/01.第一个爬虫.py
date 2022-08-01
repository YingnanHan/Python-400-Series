import requests
#请求的url地址
url = 'http://www.baidu.com'
#1.发送请求
resp = requests.get(url)
resp.encoding = 'utf-8' #设置编码
#2.获取响应内容
print(resp.text)
#3. 解析html内容 获取有价值的数据
#4.保存数据
