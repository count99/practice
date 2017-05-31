# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:11:41 2017

@author: eli

"""

import re
import requests
from bs4 import BeautifulSoup
import MySQLdb

def get_html(url):
    """get tw stock code information """
    
#    url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2' 上市
#    url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=4' 上櫃
    r = requests.get(url)
    r.encoding = 'Big5'
    url_text = r.text
    soup = BeautifulSoup(url_text, 'html.parser')
    result = soup.find_all("td", attrs={"bgcolor":"#FAFAD2"})
    return result

def parse_result(result, pattern):
    
#pattern = "ESVUFR" 上市 OTC

    td_list=[]
    round_list=[]
    for i in range(len(result)):
        if (result[i].text)==pattern:
            new_i = i - 5
            for j in range(new_i, i+1):
                if j == new_i:
                    get1 = re.findall('(.{4})(?<!u3000).+', result[j].text)
                    get2 = re.findall('([\u2E80-\u9FFF|碁]+\w*[-KY]*)', result[j].text)
                    round_list.append(get1[0])
                    round_list.append(get2[0])
                else:
                    round_list.append(result[j].text)
            else:
                td_list.append(round_list)
                round_list=[]
    return td_list

def insert_sql(get_list):

    db=MySQLdb.connect(host='localhost', user="root", passwd='', db='twstock', charset="utf8")
    cur = db.cursor()
    for i in get_list:
        sql = """INSERT INTO `twotc`(`a_seq`, `tw_index`, `tw_name`, `tw_isin`, `issue_day`, `a_market`, `a_industry`, `a_cfi`) VALUES (NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')""".format(*i)
        cur.execute(sql)
         
    db.commit()
    db.close()

def lstrip_list(get_list):
    for i in range(len(get_list)):
        get_list[i][1]=get_list[i][1].lstrip('\u3000')
    return get_list
    
    
if __name__ == "__main__":
    result = get_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=4')
    get_list = parse_result(result, "ESVUFR")
    get_list = lstrip_list(get_list)
    insert_sql(get_list)
    