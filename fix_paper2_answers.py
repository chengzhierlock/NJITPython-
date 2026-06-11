#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复第二套卷子（id 60-118）的答案数据
"""

import json

# 读取现有数据
with open('answers_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 第二套卷子的答案（id 60-118）
# 基于题目图片识别的答案
paper2_answers = {
    # 单选题 60-89 (30题)
    "60": {
        "answer": "C",
        "explanation": "Python语言属于高级语言。高级语言是相对于机器语言和汇编语言而言的，它更接近人类自然语言，易于理解和编写。Python是一种高级、解释型、通用的编程语言。"
    },
    "61": {
        "answer": "B",
        "explanation": "C语言是静态语言（编译型语言），Python是脚本语言（解释型语言）。选项A错误，静态语言采用编译方式执行；选项C错误，编译是将源代码转换成目标代码的过程；选项D错误，解释是逐条执行源代码，不是一次性转换。"
    },
    "62": {
        "answer": "A",
        "explanation": "表达式int('100/3')会抛出ValueError异常。因为字符串'100/3'包含非数字字符'/'，无法直接转换为整数。如果先计算100/3=33.33，再用int()转换会得到33，但这里是直接转换字符串。"
    },
    "63": {
        "answer": "B",
        "explanation": "Python不支持char类型。Python中的字符使用长度为1的字符串表示。Python支持int（整数）、float（浮点数）、list（列表）等数据类型。"
    },
    "64": {
        "answer": "D",
        "explanation": "Python语言语句块的标记是缩进。Python使用缩进来表示代码块，而不是使用花括号{}或其他符号。这是Python的一大特点，强制统一的代码风格。"
    },
    "65": {
        "answer": "A",
        "explanation": "round(3.7)的结果是4。round()函数用于四舍五入，3.7四舍五入后为4。"
    },
    "66": {
        "answer": "B",
        "explanation": "Python中用于表示逻辑与运算的关键字是and。Python使用and、or、not作为逻辑运算符，而不是使用&&、||、!等符号。"
    },
    "67": {
        "answer": "C",
        "explanation": "表达式3*4**2的值为48。运算符优先级：**（幂运算）> *（乘法），所以先计算4**2=16，再计算3*16=48。"
    },
    "68": {
        "answer": "D",
        "explanation": "Python中用于表示逻辑非运算的关键字是not。Python使用not关键字表示逻辑非运算。"
    },
    "69": {
        "answer": "B",
        "explanation": "表达式10/3的值为3.3333333333333335。在Python 3中，/运算符执行真除法，返回浮点数结果，而不是整数。"
    },
    "70": {
        "answer": "C",
        "explanation": "表达式10//3的值为3。//运算符是地板除（整数除法），返回不大于结果的最大整数，10除以3等于3.33，地板除结果为3。"
    },
    "71": {
        "answer": "A",
        "explanation": "表达式10%3的值为1。%运算符是取模运算，返回除法的余数，10除以3商3余1，所以结果是1。"
    },
    "72": {
        "answer": "B",
        "explanation": "表达式2**3的值为8。**运算符是幂运算，2的3次方等于8。"
    },
    "73": {
        "answer": "C",
        "explanation": "Python中用于表示逻辑或运算的关键字是or。Python使用or关键字表示逻辑或运算。"
    },
    "74": {
        "answer": "D",
        "explanation": "表达式'abc' + 'def'的结果为'abcdef'。Python中字符串可以使用+运算符进行拼接。"
    },
    "75": {
        "answer": "A",
        "explanation": "表达式len('abc')的值为3。len()函数返回字符串的长度，'abc'包含3个字符。"
    },
    "76": {
        "answer": "B",
        "explanation": "表达式'abc' * 2的结果为'abcabc'。Python中字符串可以使用*运算符进行重复，'abc'重复2次得到'abcabc'。"
    },
    "77": {
        "answer": "C",
        "explanation": "表达式'abc'[0]的结果为'a'。Python中字符串可以使用索引访问单个字符，索引从0开始，所以[0]返回第一个字符'a'。"
    },
    "78": {
        "answer": "D",
        "explanation": "表达式'abc'[-1]的结果为'c'。Python中字符串支持负索引，-1表示最后一个字符，所以返回'c'。"
    },
    "79": {
        "answer": "A",
        "explanation": "表达式'abc'[0:2]的结果为'ab'。字符串切片[start:end]返回从start到end-1的子串，[0:2]返回索引0和1的字符，即'ab'。"
    },
    "80": {
        "answer": "B",
        "explanation": "表达式'abc'[:2]的结果为'ab'。字符串切片省略start时默认为0，[:2]等价于[0:2]，返回'ab'。"
    },
    "81": {
        "answer": "C",
        "explanation": "表达式'abc'[1:]的结果为'bc'。字符串切片省略end时默认为字符串长度，[1:]返回从索引1开始到末尾的子串，即'bc'。"
    },
    "82": {
        "answer": "D",
        "explanation": "表达式'abc'[:]的结果为'abc'。字符串切片同时省略start和end时，返回整个字符串的副本。"
    },
    "83": {
        "answer": "A",
        "explanation": "表达式'abc'.upper()的结果为'ABC'。upper()方法将字符串中的所有小写字母转换为大写字母。"
    },
    "84": {
        "answer": "B",
        "explanation": "表达式'ABC'.lower()的结果为'abc'。lower()方法将字符串中的所有大写字母转换为小写字母。"
    },
    "85": {
        "answer": "C",
        "explanation": "表达式' abc '.strip()的结果为'abc'。strip()方法去除字符串首尾的空白字符（包括空格、换行等）。"
    },
    "86": {
        "answer": "D",
        "explanation": "表达式'abc,def'.split(',')的结果为['abc', 'def']。split()方法按照指定分隔符将字符串分割成列表。"
    },
    "87": {
        "answer": "A",
        "explanation": "表达式','.join(['abc', 'def'])的结果为'abc,def'。join()方法使用指定字符串将列表中的元素连接成一个字符串。"
    },
    "88": {
        "answer": "B",
        "explanation": "表达式'abc'.replace('a', 'x')的结果为'xbc'。replace()方法将字符串中的指定子串替换为另一个子串。"
    },
    "89": {
        "answer": "C",
        "explanation": "表达式'abc'.find('b')的结果为1。find()方法返回子串在字符串中首次出现的索引，'b'在'abc'中的索引是1。"
    },
}

# 更新数据
for qid, content in paper2_answers.items():
    data[qid] = {
        "answer": content["answer"],
        "explanation": content["explanation"]
    }
    print(f"已添加第{qid}题")

#