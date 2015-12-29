# -*- coding=utf-8 -*-
import sys
import re
from token_tab import dict


def findIndex(item,numlist):
    indexlist = []
    count = 0
    for i in numlist:
        indexlist.append(count+item[count:].index(i))
        count+=(item[count:].index(i)+1)
    return indexlist

class getTokenMain():
    def __init__(self):
        self.file = 'test'
        self.data = []  # 存放每行数据
        self.flow = []  # 存放输出流

    def getFileData(self):
        with open(self.file,'r') as f:
            datalist = f.readlines()
            f.close()
        for i in datalist:
            if i.strip().startswith('--') or i.strip().startswith('//'):  # 整行注释pass
                continue
            else:
                self.data.append(((i.strip().split(';')[0]).upper()+';').split(' '))  # 结尾注释消除

    def findDictValue(self,itemlist):
        num_pattern = re.compile(r'^[0-9]*(\.)?[0-9]*$')  # 常数正则式
        findNumPattern = re.compile(r'.*?([0-9]+\.?[0-9]*).*?')  # 查找常数
        for item in itemlist:
            if dict.has_key(item):  # 在字典查找
                self.flow.append([item,dict[item]])
            elif re.search(num_pattern,item):  # 匹配常熟
                self.flow.append([item,{'type':'CONST_ID','value':item}])
            else:
                l = len(item)
                indexList = []  # 索引列表
                if l == 1:
                    sys.exit('ERRTOKEN')
                numList = re.findall(findNumPattern,item)  # 查找常数
                #print numList
                if len(numList):
                    indexList = findIndex(item,numList)
                #print indexList
                count = 0
                while count < l:
                    if count in indexList:  # 常数索引
                        del indexList[0]
                        self.findDictValue([numList[0]])
                        count+=len(numList[0])
                        del numList[0]
                    elif item[count:count+2] in ['PI','**']:
                        self.findDictValue([item[count:count+2]])
                        count+=2
                    elif item[count:count+3] in ['TAN','COS','SIN']:
                        self.findDictValue([item[count:count+3]])
                        count+=3
                    else:
                        self.findDictValue(item[count])
                        count+=1

    # def resultPrint(self):  # 输出结果
    #    print "类别        名称        值"
    #    for i in self.flow:
    #        print('%-12s%-12s%-13s'%(i[1]['type'],i[0],i[1]['value']))  # 输出格式
    #    sys.exit('输出结束')

    def hackerStart(self):  # class开始函数
        self.getFileData()
        for item in self.data:
            self.findDictValue(item)
        #self.resultPrint()
# if __name__ == '__main__':
#    r = getTokenMain()
#    r.hackerStart()

def getToken():
    r = getTokenMain()
    r.hackerStart()
    return r.flow
#getToken()