#-*-coding:utf8-*-<br>
import requests<br>
import pymysql<br>
import time<br>
import colorama<br>
import urllib.parse<br>
<br>
���а������ⲿ���ļ�<br>
class Mysql<br>
    db_list���ݿ����� #lib.db_list����<br>
    run_sql(sql) ����sql��䡣 #�����ؽ��<br>
	run_sql_beark(sql) ����sql��䷵�ز�ѯ���<br>
<br><br>
class Url<br>
	url_code(list) ��Ԫ����룬����url�������������� {"aa":"bb","cc":123} ���� aa=bb&cc=123<br>
	str_pure(str) ��str�ַ�����ʽ��ȥ��������š����ظ�ʽ����Ľ�� ["'","��","��","\\","*","|","/","-",";"]<br>
<br>
class Web
	GET(url,head,pro) 3�������ֱ�Ϊurl��headͷ����pro�Ƿ������ʹ�ô���0��ʹ�ô������ش���Ķ˿ں�<br>
	POST(url,head,data,pro) ��get��һ��post data,��Ҫpost�ύ�����ݴ����ﴫ�롣<br>
	download_img(url,file) ����ͼƬ��url,���·��(��Ҫ�����ļ���)<br>
	download_video(url,file) ������Ƶ ����<br><br>
class heart:<br>
	run_heart("lib\open.txt",20,"close.txt") #һ�����׵�������� <br>