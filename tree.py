#-*- coding:UTF-8 -*-
__author__ = 'dhs'

class SetTree(object):
    def __init__(self, centerNode, *argv):
        self.centerNode = centerNode
        if centerNode == "CONST_ID":
            self.argv = {"CaseConst":argv[0]}
        elif centerNode == "T":
            self.argv = {"CaseParmPtr":argv[0]}
        elif centerNode == "FUNC":
            self.argv = {"MathFuncPtr": argv[0],"Child": argv[1]}
        else:
            self.argv = {"Left":argv[0],"Right":argv[1]}
    def __str__(self):  # 用于class的返回值
        return self.centerNode

def ExpressionValue(root):
    if root is None:
        return 0.0
    if root.centerNode == "PLUS":
        left = ExpressionValue(root.argv["Left"])
        right = ExpressionValue(root.argv["Right"])
        if isinstance(left, str) or isinstance(right, str):
            return '(' + left + '+' + right + ')'
        return left + right
    elif root.centerNode == "MINUS":
        left = ExpressionValue(root.argv["Left"])
        right = ExpressionValue(root.argv["Right"])
        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '-' + str(right) + ')'
        return left - right
    elif root.centerNode == "MUL":
        left = ExpressionValue(root.argv["Left"])
        right = ExpressionValue(root.argv["Right"])
        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '*' + str(right) + ')'
        return left * right
    elif root.centerNode == "DIV":
        left = ExpressionValue(root.argv["Left"])
        right = ExpressionValue(root.argv["Right"])
        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '/' + str(right) + ')'
        if right == 0:
            return left
        else:
            return left / right
    elif root.centerNode == "POWER":
        left = ExpressionValue(root.argv["Left"])
        right = ExpressionValue(root.argv["Right"])
        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '**' + str(right) + ')'
        return pow(int(left), right)
    elif root.centerNode == "FUNC":
        if root.argv["Child"].centerNode == "T":
            return root.argv["MathFuncPtr"] + "(T)"
        child = ExpressionValue(root.argv["Child"])
        if isinstance(child, str):
            return root.argv["MathFuncPtr"] + child
        temp = 0
        exec("temp = " + str(root.argv["MathFuncPtr"]) + '(' + str(ExpressionValue(root.argv["Child"])) + ')')
        return temp
    elif root.centerNode == "CONST_ID":
        return root.argv["CaseConst"]
    elif root.centerNode == "T":
        return "T"