'''
时间工具类
@author: wusq
@date: 2018-05-08
'''

from datetime import datetime, timedelta


date_pattern = '%Y%m%d'
time_pattern = '%Y%m%d%H%M%S'


def get_date_list(begin_date, end_date):

    '''
    获取起止日期之间的所有日期列表
    Args:
        begin_date: 开始日期
        end_date: 结束日期
    Returns:
        日期列表
    '''

    result = []
    a_day = timedelta(days=1)
    result.append(begin_date)
    while begin_date < end_date:
        begin_date += a_day
        result.append(begin_date)
    return result


def get_day_list(begin_day, end_day):

    '''
    获取起止日期字符串之间的所有日期字符串列表
    与函数get_date_list的区别是输入输出均是日期字符串
    Args:
        begin_day: 开始日期字符串
        end_day: 结束日期字符串
    Returns:
        日期字符串列表
    '''

    result = []
    begin_date = datetime.strptime(begin_day, date_pattern)
    end_date = datetime.strptime(end_day, date_pattern)
    date_list = get_date_list(begin_date, end_date)
    for date in date_list:
        result.append(date.strftime(date_pattern))
    return result


if __name__ == '__main__':
    print(get_day_list('20180501', '20180510'))