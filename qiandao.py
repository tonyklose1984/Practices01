#coding:utf-8
from splinter import Browser
import time

def login():
    b = Browser(driver_name="chrome")
    b.visit("http://www.iqiyi.com/lib/m_200197614.html")
    # b.fill("qq","154293106")
    # b.fill("pass","19840807hxc!")
    button = b.find_by_value("登 录")
    button.click()
    button2 = b.find_by_value("立即签到")
    button2.click()
    time.sleep(10)

# def qiandao():
#     #判断是否到签到时间
#     mytime = time.strftime("%H:%M:%S")
#     mytime = mytime.split(":")
#     if  int(mytime[0]) > 20 and int(mytime[0]) <21:
#         login()
#     elif int(mytime[0]) > 21:
#         print("超过了签到时间了")
#     else:
#         print("还没到签到时间哦")

if __name__ == "__main__":
    login()