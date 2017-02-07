# coding: utf-8

import requests

from prettytable import PrettyTable

class TrainCollection(object):

    # 显示车次、出发/到达站、 出发/到达时间、历时、一等坐、二等坐、软卧、硬卧、硬座
    header = 'train station time duration first second softsleep hardsleep hardsit'.split()

    def __init__(self, rows):
        self.rows = rows

    def _get_duration(self, row):
        """
        获取车次运行时间
        """
        duration = row.get('lishi').replace(':', 'h') + 'm'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for row in self.rows:
            train = [
                # 车次
                row['station_train_code'],
                # 出发、到达站
                '\n'.join([row['from_staion_name'], row['to_station_name']]),
                # 出发、到达时间
                '\n'.join([row['start_time'], row['arrive']]),
                # 历时
                self._get_duration(row),
                # 一等坐
                row['zy_num'],
                # 二等坐
                row['ze_num'],
                # 软卧
                row['rw_num'],
                # 软坐
                row['yw_num'],
                # 硬坐
                row['yz_num']
            ]
            yield train

    def pretty_print(self):
        """
        数据已经获取到了，剩下的就是提取我们要的信息并将它显示出来。
        `prettytable`这个库可以让我们它像MySQL数据库那样格式化显示数据。
        """
        pt = PrettyTable()
        # 设置每一列的标题
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    print(arguments)

def test():
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-02-07&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=KNH&purpose_codes=ADULT'
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
        ret = [station_train_code, from_station_name, to_station_name,  
            start_time, arrive_time, start_train_date
            , yideng_zuo, erdeng_zuo, wu_zuo]
        all_ret.append(ret)
        
#    print(all_ret)
    
    Mheaders = u'列车  出发地   目的地 发车 到达 时间 一等座 二等座 无座 '.split()
    pt = PrettyTable()
    # 设置每一列的标题
    pt._set_field_names(Mheaders)
    
    for ret in all_ret:
        pt.add_row(ret)
    print('type = ', type(pt))
    print(pt)
    

if __name__ == '__main__':
    test()

