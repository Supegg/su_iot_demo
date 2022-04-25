from wifi import Wifi
import requests, time
 
 
url = 'http://192.168.0.47:5000/message/cock'
r = requests.get(url)
print(r.json)
r.close()

url = 'http://192.168.0.47:5000/upload?key1=value1&key2=value2' # url附带args
with open('elegance.jpg','rb') as f: # 以二进制形式读取文件
    img=f.read()
s = time.ticks_ms()    
r = requests.post(url, data=img, # 二进制img数组
                  headers = {'header0':'header0', 'header1':'header1'}) # header里附带信息
print(f'{len(img)* 1.0 /(time.ticks_ms() - s):.1f} kB/s')
print(r.text) #接收服务器数据
r.close()
