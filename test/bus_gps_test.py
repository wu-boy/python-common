#!/usr/bin/python
# -*- coding: UTF-8

import os

from datetime import datetime,timedelta


def main():

    dir_gps_minute = 'bus_gps_minute'
    os.mkdir(dir_gps_minute)

    day = datetime(2018, 4, 12)
    minute_dict = {}
    for i in range(0, 1440):
        minute_dict[day.strftime('%H%M')] = []
        day += timedelta(minutes=1)

    dir_name = 'gps_20160905'
    file_list = os.listdir(os.path.join(dir_name))
    for file in file_list:
        for line in open(os.path.join(dir_name, file), 'rt'):
            #1503520,2016-09-05 00:03:44.0,113.5583,34.80898333333333,1,0,19,1,1
            minute = line.rstrip().split(',')[1][11:16].replace(':', '')
            minute_dict[minute].append(line)
            if len(minute_dict[minute]) == 1000:
                with open(os.path.join(dir_gps_minute, minute), 'at') as f:
                    f.writelines(minute_dict[minute])

    for k, v in minute_dict.items():
        with open(os.path.join('bus_gps_minute', k), 'at') as f:
            f.writelines(v)


if __name__ == '__main__':
    main()