#-*-coding:utf8-*-<br>
import requests<br>
import pymysql<br>
import time<br>
import colorama<br>
import urllib.parse<br>
<br>
所有包含的外部库文件<br>
class Mysql<br>
    db_list数据库配置 #lib.db_list调用<br>
    run_sql(sql) 运行sql语句。 #不返回结果<br>
	run_sql_beark(sql) 运行sql语句返回查询结果<br>
<br><br>
class Url<br>
	url_code(list) 把元组存入，返回url编码机构后的数据 {"aa":"bb","cc":123} 返回 aa=bb&cc=123<br>
	str_pure(str) 把str字符串格式化去掉特殊符号。返回格式化后的结果 ["'","（","）","\\","*","|","/","-",";"]<br>
<br>
class Web
	GET(url,head,pro) 3个参数分别为url，head头部，pro是否代理，不使用代理传0，使用代理传本地代理的端口号<br>
	POST(url,head,data,pro) 比get多一个post data,需要post提交的数据从这里传入。<br>
	download_img(url,file) 下载图片，url,存放路径(需要包含文件名)<br>
	download_video(url,file) 下载视频 如上<br><br>
class heart:<br>
	run_heart("lib\open.txt",20,"close.txt") #一个简易的心跳监测 <br>