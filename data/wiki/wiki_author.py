# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:14:53 2016

@author: 曹茂国
"""
import re
import sys 
sys.path.append('../../') 
import mongodb.pymongo_class as mongdb_class
class wiki_author:
    def __init__(self,author,ip,port,dataBase):
        self.changeData(author)
        author_table = mongdb_class.MongoClass(ip,port,dataBase,'author');
        return None
        
    def changeData(self,author):
        for i in range(len(author)):
            name = author['name'][i]
            print i,name
            name = name.replace('-',' ')
            print name
            born = author['born'][i];
            year = '';
            heath = '';
            diedYear = '';
            if born:
                searchYear = re.compile(r'\d{4}').search(born);
                if searchYear:
                   year = searchYear.group()
                searchHeath = re.compile(r'[^;]*.$').search(born)
                heathAll = None
                if searchHeath:
                    heathAll = searchHeath.group()
                if heathAll and  (not self.is_number(heathAll)):
                    heath = heathAll.split(',')[0]
            died = author['died'][i];
            if died:
                searchDiedYear = re.compile(r'\d{4}').search(died);
                if searchDiedYear:
                    diedYear =  searchDiedYear.group();
            
            filed = self.getFiled(author['field'][i])
            nationality = self.getNationality(author['nationality'][i])
            

            
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
    
        return False
        
    def getFiled(self,value):
        if value:
            value = value.split(',');
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
                 'tapestry':u'tapestry',
                 'caricature':u'漫画',
                 'goldsmith':u'金匠',
                 'enamel':u'搪瓷',
                 'animation':u'动画',
                 'interactiveart':u'互动艺术',
                 'calligraphy':u'书法'
            }
            value_zh = '';
            for i in range(len(value)):
                value_zh = value_zh + filed[value[i]] + ','
            return value_zh[0:len(value_zh) - 1]
        return ''
                         
                         
                         
    def getNationality(self,value):
        print value
        if value:
            value = value.split(',');
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
                'Guyanese':u'圭亚那人',
                'Jamaican':u'牙买加',
                'Qatari':u'卡塔尔',
                'SouthKorean':u'朝鲜',
                'Finnish':u'芬兰',
                'Vietnamese':u'越南',
                'Belarusian':u'白俄罗斯',
                'Macedonian':u'马其顿',
                'Danish':u'丹麦',
                'Icelandic':u'冰岛',
                'Latvian':u'拉脱维亚',
                'Iraqi':u'伊拉克',
                'Uruguayan':u'乌拉圭',
                'Czech':u'捷克',
                'Georgian':u'格鲁吉亚',
                'Ecuadorian':u'厄瓜多尔',
                'Thai':u'泰国',
                'Dominican':u'多米尼加',
                'Egyptian':u'埃及',
                'Nigerian':u'尼日利亚',
                'Venezuelan':u'委内瑞拉',
                'Filipino':u'菲律宾',
                'PuertoRican':u'波多黎各',
                'Ghanaian':u'加纳',
                'Libyan':u'利比亚',
                'Lebanese':u'黎巴嫩',
                'Albanian':u'阿尔巴尼亚',
                'Estonian':u'爱沙尼亚',
                'Persian':u'波斯人',
                'Syrian':u'叙利亚',
                'Slovak':u'斯洛伐克',
                'Chilean':u'智利',
                'Guatemalan':u'危地马拉',
                'Kenyan':u'肯尼亚',
                'Sudanese':u'苏丹',
                'Azerbaijani':u'阿塞拜疆',
                'Cameroonian':u'喀麦隆',
                'Peruvian':u'秘鲁'
            }
            value_zh = '';
            for i in range(len(value)):
                value_zh = value_zh + nationality[value[i]] + ','
            return value_zh[0:len(value_zh) - 1]
        return '';
        
