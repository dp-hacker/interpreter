#-*- coding:UTF-8 -*-
__author__ = 'dhs'
import sys
from tree import SetTree , ExpressionValue
from get_token import getToken

token = []  # token_list
length = 0  # length of token
count = 0  #  用于递归过程中计数
origin = [0.0,0.0]  # origin
rot = 0.0  # value of rot
scale = [1,1]  # value of scale
loop = [0.0,0.0,None,' ',' ']  # start,end,step,x,y

def DealError(error_num):  # deal with errors
    if error_num == 0:
        print token[count-1]
        print token[count]
        sys.exit('Syntax Error!')
    elif error_num == 1:
        sys.exit('Nothing In The Token List!')
    else:
        return

def FetchToken():  #  import data from get_token
    global token,length
    token = getToken()
    length = len(token)
    if length == 0:
        DealError(1)

def MatchToken(current_token):  # match token
    global count
    if token[count][1]['type'] == current_token:
        count+=1
    else:
        DealError(0)

def Program():
    global count
    while count < length:
        Statement()
        MatchToken('SEMICO')

def Statement():  # 判断首个token，进而选择对应的语句进行匹配
    global count
    if token[count][1]['type'] == 'ORIGIN':
        return OriginStatement()
    elif token[count][1]['type'] == 'SCALE':
        return ScaleStatement()
    elif token[count][1]['type'] == 'ROT':
        return RotStatement()
    elif token[count][1]['type'] == 'FOR':
        return ForStatement()

def OriginStatement():  # origin is (,)
    global origin
    MatchToken('ORIGIN')
    MatchToken('IS')
    MatchToken('L_BRACKET')
    origin[0] = ExpressionValue(Expression())
    MatchToken('COMMA')
    origin[1] = ExpressionValue(Expression())
    MatchToken('R_BRACKET')

def RotStatement():  # rot is
    global rot
    MatchToken('ROT')
    MatchToken('IS')
    rot = ExpressionValue(Expression())

def ScaleStatement():  # scale is (,)
    global scale
    MatchToken('SCALE')
    MatchToken('IS')
    MatchToken('L_BRACKET')
    scale[0] = ExpressionValue(Expression())
    MatchToken('COMMA')
    scale[1] = ExpressionValue(Expression())
    MatchToken('R_BRACKET')

def ForStatement():  # for T from start to end step draw(x,y)
    global loop
    MatchToken('FOR')
    MatchToken('T')
    MatchToken('FROM')
    loop[0] = ExpressionValue(Expression())
    MatchToken('TO')
    loop[1] = ExpressionValue(Expression())
    MatchToken('STEP')
    loop[2] = ExpressionValue(Expression())
    MatchToken('DRAW')
    MatchToken('L_BRACKET')
    loop[3] = ExpressionValue(Expression())
    MatchToken('COMMA')
    loop[4] = ExpressionValue(Expression())
    MatchToken('R_BRACKET')

def Expression():
    global count
    left = Term()
    while token[count][1]['type'] == 'PLUS' or token[count][1]['type'] == 'MINUS':
        tmp = token[count][1]['type']
        MatchToken(tmp)
        right = Term()
        left = SetTree(tmp, left, right)
    return left

def Term():
    global count
    left = Factor()
    while token[count][1]['type'] == 'MUL' or token[count][1]['type'] == 'DIV':
        tmp = token[count][1]['type']
        MatchToken(tmp)
        right = Factor()
        left = SetTree(tmp, left, right)
    return left

def Factor():
    global count
    if token[count][1]['type'] == 'PLUS' or token[count][1]['type'] == 'MINUS':
        left = SetTree('CONST_ID', 0.0)
        tmp = token[count][1]['type']
        MatchToken(tmp)
        right = Factor()
        left = SetTree(tmp, left, right)
    else:
        left = Component()
    return left

def Component():
    global count
    left = Atom()
    if token[count][1]['type'] == 'POWER':
        tmp = token[count][1]['type']
        MatchToken(tmp)
        right = Component()
        left = SetTree(tmp, left, right)
    return left

def Atom():
    global count
    left = None
    if token[count][1]['type'] == 'CONST_ID':
        tmp = token[count][1]['type']
        token_num = token[count][1]['value']
        MatchToken(tmp)
        left = SetTree('CONST_ID', token_num)
    elif token[count][1]['type'] == 'T':
        tmp = token[count][1]['type']
        MatchToken(tmp)
        left = SetTree('T', 'T')
    elif token[count][1]['type'] == 'FUNC':
        func_name = token[count][0]
        MatchToken('FUNC')
        MatchToken('L_BRACKET')
        child = Expression()
        MatchToken('R_BRACKET')
        left = SetTree('FUNC', func_name, child)
    elif token[count][1]['type'] == 'L_BRACKET':
        MatchToken('L_BRACKET')
        left = Expression()
        MatchToken('R_BRACKET')
    else:
        DealError(0)
    return left

def Parser():
    FetchToken()
    Program()
    # print origin
    # print scale
    # print rot
    # print loop

Parser()



