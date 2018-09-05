'''
GIS工具类
@author: wusq
@date: 2018-06-21
'''

from math import *

'''计算两点之间直线距离'''
def get_distance1(lon_a, lat_a, lon_b, lat_b):
    radlat1 = radians(lat_a)
    radlat2 = radians(lat_b)
    a = radlat1 - radlat2
    b = radians(lon_a) - radians(lon_b)
    s = 2 * asin(sqrt(pow(sin(a/2),2) + cos(radlat1) * cos(radlat2)*pow(sin(b/2),2)))
    earth_radius = 6378137
    s = s * earth_radius
    return s

'''计算两点之间直线距离'''
def get_distance2(lon_a, lat_a, lon_b, lat_b):
    if abs(lon_a - lon_b) < 0.000001 and abs(lat_a - lat_b) < 0.000001:
        return 0
    re = 6378140  # 赤道半径 (m)
    rp = 6356755  # 极半径 (m)
    oblateness = (re - rp) / re  # 地球扁率
    rad_lat_a = radians(lat_a)
    rad_lon_a = radians(lon_a)
    rad_lat_b = radians(lat_b)
    rad_lon_b = radians(lon_b)
    atan_a = atan(rp / re * tan(rad_lat_a))
    atan_b = atan(rp / re * tan(rad_lat_b))
    tmp = acos(sin(atan_a) * sin(atan_b) + cos(atan_a) * cos(atan_b) * cos(rad_lon_a - rad_lon_b))
    if tmp == 0:
        return 0
    c1 = (sin(tmp) - tmp) * (sin(atan_a) + sin(atan_b)) ** 2 / cos(tmp / 2) ** 2
    c2 = (sin(tmp) + tmp) * (sin(atan_a) - sin(atan_b)) ** 2 / sin(tmp / 2) ** 2
    dr = oblateness / 8 * (c1 - c2)
    distance = re * (tmp + dr)
    return distance


def manhattan_distance(lon_a:float, lat_a:float, lon_b:float, lat_b:float):
    '''
    计算曼哈顿距离
    Args:
        lon_a: a点经度
        lat_a: a点纬度
        lon_b: b点经度
        lat_b: b点纬度
    Returns:
        曼哈顿距离
    '''
    return get_distance1(lon_a, lat_a, lon_b, lat_a) + get_distance1(lon_b, lat_a, lon_b, lat_b)

def main():
    lon_a = 116.320866
    lat_a = 39.814506
    lon_b = 116.301322
    lat_b = 39.87874
    print(get_distance1(lon_a, lat_a, lon_b, lat_b))
    print(get_distance2(lon_a, lat_a, lon_b, lat_b))

if __name__ == '__main__':
    main()