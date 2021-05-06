#coding =utf-8
import os
import pymssql
import re
# import trsData
import datetime
import time
#获取当时时间
import queue
import threading


def get_date():
    date = datetime.datetime.now()
    strDate = date.strftime("%Y-%m-%d")
    return strDate

class Kuaishou_Account:
    #10.20.66.204
    def __init__(self):
        self.server = "10.20.66.203"   #203
        # user ="CTRCHINA\wenxin"
        self.user = "sa"
        self.password = "123!@#qwe"
        self.sql ="SELECT top 10000 *FROM KuaishouVideoComment where CreateTime >{}"

    def sql_init(self):
        conn = pymssql.connect(self.server, self.user, self.password, "datafusion")  # 获取连接
        cursor = conn.cursor(as_dict=True)  # 获取光标
        return cursor, conn

    def reptile_d(self):
        now = int(time.time())  # 1533952277
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        return otherStyleTime

    def getDate(self, beforeOfDay):
        today = datetime.datetime.now()
        # 计算偏移量
        offset = datetime.timedelta(days=-beforeOfDay)
        # 获取想要的日期的时间
        re_date = (today + offset).strftime('%Y-%m-%d')  # %Y-%m-%d %H:%M:%S
        return re_date

    def Get_Account(self):
        cursor,conn = self.sql_init()
        cursor.execute(self.sql.format(self.getDate(1)))  # 调用游标指针的execute方法执行sql语句
        Accountid_list = []
        for row in cursor:
            Accountid_list.append(row["UserID"])
        print(len(Accountid_list))
        return Accountid_list

    def work(self,device):
        hours = datetime.datetime.now().hour
        while hours >= 14 and hours <= 15:
            hours = datetime.datetime.now().hour
            time.sleep(3)


        while not q.empty():
            share_id = q.get()
            open = 'adb -s '+ device + ' shell am start -a android.intent.action.VIEW -d kwai://profile/{0}'.format(share_id)
            os.system(open)
            time.sleep(3)
            for j in range(7):
                backcmd = "adb -s " + device + " shell input keyevent 4"
                os.system(backcmd)
                time.sleep(0.5)


    def main(self):

        accountid_list = self.Get_Account()
        for accountid in accountid_list:
            q.put(accountid)
        thread_list = []
        for devices in devices_list:
            thread1 = threading.Thread(target =self.work,args=(devices,))
            thread1.start()
            thread_list.append(thread1)
        for thread1 in thread_list:
            thread1.join()

if __name__ == '__main__':

    while True:
        #启动
        try:
            hours = datetime.datetime.now().hour
            while hours >= 8 and hours <= 22:
                hours = datetime.datetime.now().hour
                ka = Kuaishou_Account()
                #ka.Get_Account()
                q = queue.Queue()
                devices_list = []
                ka.main()
        except Exception as e:
            time.sleep(3)
        time.sleep(5)



