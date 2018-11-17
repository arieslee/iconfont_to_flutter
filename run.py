#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/17 上午8:51
# @Author  : Aries (i@iw3c.com)
# @Site    : http://iw3c.com
# @File    : run.py
# @Software: PyCharm
import re
import os
import sys
import getopt
import time

# 配置信息
__CONST_ICONFONT__ = 'iconfont'
class_name = ''
dist_name = ''
font_name = ''
css_file_name = ''


# 帮助信息
def help_info():
    print('run.py -c <class_name> -d <dist_name> -f <font_name> -cs <css_file_name>')


# 从入参中获取配置
try:
    opts, args = getopt.getopt(sys.argv[1:], "c:d:f:cs:", ["class_name=", "font_name=", "dist_name=", "css_file_name="])
except getopt.GetoptError:
    help_info()
    sys.exit(2)


for opt, arg in opts:
    if opt in ("-c", "--class_name"):
        class_name = arg
    elif opt in ("-d", "--dist_name"):
        dist_name = arg
    elif opt in ("-f", "--font_name"):
        font_name = arg
    elif opt in ("-cs", "--css_file_name"):
        font_name = arg

if class_name == '':
    print('错误的配置信息：class_name=%s' % (class_name,))
    sys.exit()

if dist_name == '':
    dist_name = __CONST_ICONFONT__

if font_name == '':
    font_name = __CONST_ICONFONT__

if css_file_name == '':
    css_file_name = __CONST_ICONFONT__
    

def convert():
    print('开始转换...')
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    flutter_code = '''
/**
 * @Author: sunmoon
 * @Url: http://blog.iw3c.com
 * @Description: Flutter项目自定义字体图标.
 * @Date: %s
 */

import 'package:flutter/widgets.dart';
class %s{
    static const __FONT_NAME__ = '%s';
{FLUTTER_CODE}
}
    '''.strip() % (date, class_name, font_name,)
    regex = re.compile(r'.icon-(.*?):.*?"\\(.*?)";')
    css_file = os.path.join(os.path.dirname(__file__), 'iconfont/'+css_file_name+'.css')
    string = ''
    for line in open(css_file):
        line = line.strip()
        if line:
            res = regex.findall(line)
            if res:
                name, value = res[0]
                name = name.replace('-', '_')
                icon_name = name.lower()
                string += f'    static const IconData {icon_name} = const IconData(0x{value}, fontFamily: __FONT_NAME__);\n'

    flutter_code = flutter_code.replace('{FLUTTER_CODE}', string)
    flutter_file = os.path.join(os.path.dirname(__file__), 'dist/'+dist_name+'.dart')
    open(flutter_file, 'w').write(flutter_code)

    print('转换完成...')


if __name__ == '__main__':
    convert()