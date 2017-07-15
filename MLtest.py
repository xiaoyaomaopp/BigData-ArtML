# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:14:53 2016

@author: Administrator
"""
#数据库中读取数据
'''
from numpy import NaN
import re
print re.compile(r'\d{4}').search('15March1894;Budapest,Hungary*').group()
print re.compile(r'[^;]*.$').search('15March1894;Budapest,Hungary*').group()
print re.compile(r'[^,]*.$').search('Budapest,Hungary*').group()
print 'Budapest,Hungary*'.split(',')[0]

print type(NaN)
'''
a = dict();
filed = {
     'painting':u'油画',
     'fresco':u'壁画',
     'graphics':u'graphics',
     'illustration':u'装置艺术',
     'drawing':u'drawing',
     'sculpture':u'雕塑',
     'installation':u'installation',
     'printmaking':u'版画',
     'architecture':u'建筑学',
     'performance':u'表演艺术',
     'etching':u'蚀刻版画',
     'photography':u'摄影',
     'design':u'design',
     'mosaic':u'镶嵌工艺',
     'engraving':u'雕刻',
     'lithography':u'石印',
     'collage':u'拼贴艺术',
     'assemblage':u'assemblage',
     'arttheory':u'arttheory',
     'digitalart':u'digitalart',
     'tapestry':u'tapestry'
     }
nationality = {
    'German': u'德国',
    'American':u'美国',
    'Hungarian':u'匈牙利',
    'Iranian':u'伊朗',
    'Indonesian':u'印度尼西亚', 
    'Armenian':u'亚美尼亚人',
    'Italian':u'意大利',
    'French':u'法国',
    'Romanian':u'罗马尼亚',
    'British':u'英国',
    'Dutch':u'荷兰',
    'Swedish':u'瑞典',
    'Polish':u'波兰',
    'Ethiopian':u'埃塞俄比亚',
    'Portuguese':u'葡萄牙',
    'Jewish':u'犹太人',
    'Israeli':u'以色列',
    'Russian':u'俄罗斯',
    'Argentinean':u'阿根廷',
    'Emirati':u'阿拉伯联合大公国',
    'Australian':u'澳大利亚',
    'Belgian':u'比利时',
    'Spanish':u'西班牙',
    'Turkish':u'土耳其',
    'Austrian':u'奥地利',
    'Greek':u'希腊',
    'Ukrainian':u'乌克兰',
    'Brazilian':u'巴西',
    'Swiss':u'瑞士',
    'NewZealander':u'新西兰',
    'Japanese':u'日本',
    'Slovenian':u'斯洛文尼亚',
    'Norwegian':u'挪威',
    'Serbian':u'塞尔维亚',
    'Chinese':u'中国',
    'Canadian':u'加拿大',
    'Cuban':u'古巴',
    'Flemish':u'佛兰德人',
    'Indian':u'印度',
    'Mexican':u'墨西哥',
    'Colombian':u'哥伦比亚',
    'Catalan':u'加泰罗尼亚',
    'Bulgarian':u'保加利亚',
    'Lithuanian':u'立陶宛',
    'SouthAfrican':u'南非',
    'Irish':u'爱尔兰',
    'Moroccan':u'摩洛哥',
    'Barbadian':u'巴贝多人',
    'Croatian':u'克罗地亚',
    'Guyanese':u'圭亚那人'      
}

value = 'painting,fresco'
value = value.split(',')
value_zh = "";
for i in range(len(value)):
    value_zh = value_zh + filed[value[i]] + ','
print value_zh[0:len(value_zh) - 1]