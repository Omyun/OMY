#-*-coding:utf8-*-
import requests
import pymysql
import time
import colorama
import urllib.parse

���а������ⲿ���ļ�
class Mysql
    db_list���ݿ����� #lib.db_list����
    run_sql(sql) ����sql��䡣 #�����ؽ��
	run_sql_beark(sql) ����sql��䷵�ز�ѯ���

class Url
	url_code(list) ��Ԫ����룬����url�������������� {"aa":"bb","cc":123} ���� aa=bb&cc=123
	str_pure(str) ��str�ַ�����ʽ��ȥ��������š����ظ�ʽ����Ľ�� ["'","��","��","\\","*","|","/","-",";"]

class Web
	GET(url,head,pro) 3�������ֱ�Ϊurl��headͷ����pro�Ƿ������ʹ�ô���0��ʹ�ô������ش���Ķ˿ں�
	POST(url,head,data,pro) ��get��һ��post data,��Ҫpost�ύ�����ݴ����ﴫ�롣
	download_img(url,file) ����ͼƬ��url,���·��(��Ҫ�����ļ���)
	download_video(url,file) ������Ƶ ����
class heart:
	run_heart("lib\open.txt",20,"close.txt") #һ�����׵�������� 