# 工具函数
import json
import random
from datetime import datetime, date
import sys, os


def get_error_json(form):
    # 解析错误信息并返回error_json
    errors = {}     # 解析错误
    error_json = {}     # 要返回的json
    for key in form.errors:
        errors[key] = form.errors[key][0]
    error_json['status'] = 'error'
    error_json['error'] = 1000
    error_json['data'] = errors
    return json.dumps(error_json)


def get_data_json(data, single=True):
    # 得到返回的data
    data_json = {}
    data_json['status'] = 'success'
    if single:
         data_json['data'] = convert_to_dicts(data)[0]
    else:
        data_json['data'] = convert_to_dicts(data)
    return json.dumps(data_json, default=__default)


def convert_to_dicts(objs):
    # 解析django查询结果 转化 为 dict
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict
        dict = {}
        dict.update(o.__dict__)
        dict.pop("_state", None)  # 去除掉多余的字段
        obj_arr.append(dict)
    return obj_arr


def __default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


class CreatePage:
    @staticmethod
    def get_random_str():
        return ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 15))

    @staticmethod
    def render_page(openid, itemid, link, randomStr):
        mapTemplate = open('./api/mapTemplate', 'r', encoding='utf-8')
        with open('./dw/templates/dw/{0}.html'.format(randomStr), 'w', encoding='utf-8') as ff:
            ff.write(mapTemplate.read().replace('{openid}', openid).replace('{itemid}', itemid).replace('{link}', link))


#CreatePage.render_page('22', '22', '232', CreatePage.get_random_str())

