#-*-coding:utf8-*-
import requests
import pymysql
import time
import colorama
import urllib.parse
colorama.init(autoreset=True)
lettime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
requests.packages.urllib3.disable_warnings() #抑制ssl错误

db_list ={
    "localhost":"127.0.0.1",
    "port":3306,
    "db":"jingdong",
    "user":"root",
    "pass":"root",
}

class Mysql:
    def run_sql(self,sqlx):#不返回查询结果
        self.conn = pymysql.connect(host=db_list['localhost'],port=db_list['port'],user=db_list['user'],password=db_list['pass'],database=db_list['db'],charset="utf8") #链接数据库
        self.cursor = self.conn.cursor()#创建数据库游标
        self.cursor.execute(sqlx)#载入sql
        self.conn.commit()#执行sql
        self.cursor.close()#关闭mysql


    def run_sql_beark(self,sql): #会返回查询结果。
        self.conn = pymysql.connect(host=db_list['localhost'],port=db_list['port'],user=db_list['user'],password=db_list['pass'],database=db_list['db'],charset="utf8") #链接数据库
        self.cursor = self.conn.cursor()#创建数据库游标
        self.sql = sql
        self.cursor.execute(sql)
        self.results = self.cursor.fetchall()
        self.conn.commit()#执行sql
        self.cursor.close()#关闭mysql
        return self.results

class Url:
    def url_code(self,data):
        self.list = str(urllib.parse.urlencode(data))
        self.list = self.list.replace("+", "")
        self.list = self.list.replace("/", '%2f')
        return self.list

    def str_pure(self,x):
        self.tempr = str(x)
        self.list = ["'","（","）","\\","*","|","/","-",";"]
        for self.key in self.list:
            self.tempr = self.tempr.replace(self.key, " ")
        return str(self.tempr)

class Web:
    def GET(self,url,head,pro):
        if pro!=0:
            self.proxies = {'http': 'http://localhost:'+pro, 'https':'http://localhost:'+pro}
            self.httpdata = requests.get(url,headers=head,verify=False,proxies=proxies)
        else:
            self.httpdata = requests.get(url,headers=head,verify=False)
        return self.httpdata.text

    def POST(self,url,head,data,pro):
        if pro!=0:
            self.proxies = {'http': 'http://localhost:'+pro, 'https':'http://localhost:'+pro}
            self.httpdata = requests.post(url,headers=head,data=data,verify=False,proxies=proxies)
        else:
            self.httpdata = requests.post(url,headers=head,data=data,verify=False)
        return self.httpdata.text

    def download_img(self,url,file):
        self.r = requests.get(url, stream=True)
        self.status = r.status_code 
        if self.status == 200:
            open(str(file), 'wb').write(self.r.content) # 将内容输出到文件
        del self.r
        return self.status

    def download_video(self,url,file):
        self.r = requests.get(url, stream=True)
        self.status = self.r.status_code 
        if self.status == 200:
            open(str(file), 'wb').write(self.r.content) # 将内容输出到文件
        del self.r
        return self.status

class heart:
    #run_heart("lib\open.txt",20,"close.txt")
    def run_heart(self,filex):#心跳

        self.tims = str(time.time())#时间戳心跳包
        self.filename = filex
        with open(self.filename, 'w') as self.file_object:
            self.file_object.write(self.tims)
    def wlop(self,text,jg):
        self.filename = jg
        with open(self.filename, 'w+') as self.file_object:
            self.file_object.write(str(text))

    def run_heart(self,filex,nx,jg): #监测的文件，判定掉线的次数，一次为3秒推荐20次(60秒)，结果输出文件
        self.rk = ""
        self.n = 1
        self.f = open(filex,'r')
        self.rk = str(self.f.read())
        self.f.close
        self.wlop("open",jg) #初始化结果状态
        while True:    
            self.f = open(filex,'r')
            self.rks = str(self.f.read())
            
            if self.rk == self.rks:
                print("\033[33m[一致状态]",self.rks,self.n,"次")
                self.n += 1
            else:
                self.n = 1
                print("\033[32m[心跳]",self.rks)
            self.rk = self.rks
            self.f.close
            if self.n > self.nx:
                print("\033[31m[进程结束]判定无心跳")
                self.wlop("close",jg) #修改结果状态
                exit()            
            time.sleep(3)




