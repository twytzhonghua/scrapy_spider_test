# coding: utf-8

import requests

from prettytable import PrettyTable

#import time
import datetime

from email.header import Header
from email.mime.text import MIMEText
import smtplib
import os
import pygame


ISOTIMEFORMAT = '%Y-%m-%d'
my_tickets_list = ['G7035', 'G7062', 'G7064', 'G7030']


def test(pt, date, from_station, to_station):
#    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-02-07&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=KNH&purpose_codes=ADULT'
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (date, from_station, to_station)

    r = requests.get(url, verify=False)
    rows = r.json()['data']
#    print(rows)
    all_ret = []
    for row in rows:
        info = row['queryLeftNewDTO']
        station_train_code = info['station_train_code']
        from_station_name = info['from_station_name']
        to_station_name = info['to_station_name']
        arrive_time = info['arrive_time']
        start_train_date = info['start_train_date']
        start_time = info['start_time']
        yideng_zuo = info['zy_num']
        erdeng_zuo = info['ze_num']
        wu_zuo = info['wz_num']
        # Mheaders = u'列车 二等座 出发地 发车 时间  '.split()
        ret = [station_train_code,  erdeng_zuo,from_station_name, 
                    start_time, start_train_date
            ]
        all_ret.append(ret)
        
#    print(all_ret)
    
    
    # 设置每一列的标题
    pt._set_field_names(Mheaders)
    
    for ret in all_ret:
        if ret[0] in my_tickets_list:
            pt.add_row(ret)
            
#    print('type = ', type(pt))
#    print(pt)
    

def query_day_is_holiday(date):
    url = 'http://www.easybots.cn/api/holiday.php?d=%s' % date
    r = requests.get(url, verify=False)
    ret = r.json()
#    print(type(ret))
    return ret[date]
    

def send_mail(str):
    from_addr = "zhonghuaqrs@163.com"
    to_addr = ['zhonghuaqrs@163.com']
    # to_addr = ['zhonghuaqrs@163.com', '466636092@qq.com']
    smtp_server = "smtp.163.com"
    password = "twyt_159"

    msg = MIMEText(str, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] =   ','.join(to_addr)
    today = datetime.date.today()
    sbuject_str = u'火车票提示 %s'  %  today
    msg['Subject'] = Header(sbuject_str, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())

    server.quit() 
  

def transfer_text_to_pic(str):
    pygame.init()
    font = pygame.font.SysFont('microsoftyahei', 10)
    rtext = font.render(str, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(rtext, "t.jpg")


if __name__ == '__main__':
#    test()
    # SHH 上海
    # KNH 昆山

    today =  datetime.date.today()
    day_list = []

    for i in range(15):
        day = today + datetime.timedelta(i)
        fmt_day = str(day).replace('-','')
        if query_day_is_holiday(fmt_day) == '0':
            day_list.append(str(day))

    # Mheaders = u'列车 一等座 二等座 无座 出发地   目的地 发车 到达 时间  '.split()
    Mheaders = u'列车 二等座 出发地 发车 时间  '.split()
    pt = PrettyTable()
    
    for day in day_list:
        test(pt, day,  'KNH', 'SHH')


    pt.add_row(['-', '-', '-', '-', '-'])
    for day in day_list:
        test(pt, day, 'SHH', 'KNH')
    
    print(str(pt))
    
    send_mail(str(pt))
    #transfer_text_to_pic(str(pt))
    # with open ('ticket_ret.txt', 'w') as f:
    # 	f.write(str(pt))


 