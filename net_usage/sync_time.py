from wifi import Wifi
import ntptime, time
from machine import Timer

def sync_ntp(tim=0): # 回调函数将Timer做为参数传入
    """通过网络校准时间"""
    ntptime.NTP_DELTA = 3155644800  # 可选 UTC+8偏移时间（秒），不设置就是UTC0
    ntptime.host = 'ntp1.aliyun.com'  # 可选，ntp服务器，默认是"pool.ntp.org" 这里使用阿里服务器
    ntptime.settime()  # 修改设备时间 
    print(time.localtime())


if __name__=='__main__':
    a=Wifi()
    a.connect()
    a.wait()
    
    sync_ntp()

    # ESP32模块RTC的精度存在一定的缺陷，每过7:45h便会有秒级别的误差
    # 官方建议每隔7小时进行一次时间的校准
    timer = Timer(1)
    # timer.init(period=1000 * 7, mode=Timer.PERIODIC, callback=sync_ntp)
    timer.init(period=1000 * 60 * 60 * 7, mode=Timer.PERIODIC, callback=sync_ntp)
