#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正试卷二选择题第16-30题（id 75-89）的答案
"""

import json

with open('answers_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修正选择题16-30（id 75-89）
fixes = {
    # 第16题 (id=75)
    "75": {"answer": "C", "explanation": "list(range(5))生成[0, 1, 2, 3, 4]，所以输出[0, 1, 2, 3, 4]"},
    
    # 第17题 (id=76) - 修正
    "76": {"answer": "B", "explanation": "weekstr = '星期一星期二星期三星期四星期五星期六星期日'，weekid=3，weekstr[9:12]='星期四'"},
    
    # 第18题 (id=77) - 修正
    "77": {"answer": "C", "explanation": "list_two = list_one是引用赋值，修改list_one[2]=3会影响list_two，结果是[4,5,3]"},
    
    # 第19题 (id=78) - 修正
    "78": {"answer": "B", "explanation": "s=[1,'kate',True]只有3个元素(索引0,1,2)，s[3]会索引越界，不会返回True"},
    
    # 第20题 (id=79) - 修正
    "79": {"answer": "C", "explanation": "数组类型不是Python内置的组合数据类型，需要使用numpy库。元组、字符串、列表都是Python组合数据类型"},
    
    # 第21题 (id=80) - 修正
    "80": {"answer": "B", "explanation": "字典的一个键只能对应一个值，键是唯一的。虽然值可以是列表等容器，但一个键不能直接对应多个值"},
    
    # 第22题 (id=81) - 修正
    "81": {"answer": "A", "explanation": "字典也可以用于布尔测试，空字典返回False，非空字典返回True。所有Python标准对象都可以用于布尔测试"},
    
    # 第23题 (id=82) - 修正
    "82": {"answer": "D", "explanation": "d = {'a':1,'b':2,'c':3}是正确定义字典的方式。A是列表，B是元组，C语法错误"},
    
    # 第24题 (id=83) - 修正
    "83": {"answer": "D", "explanation": "d ^ c是对称差集运算，返回只在d或只在c中的元素。d={0,1,2,3,8,9}, c={1,2,3,4,5,6}，对称差集是{0,4,5,6,8,9}"},
    
    # 第25题 (id=84) - 修正
    "84": {"answer": "A", "explanation": "空字典可以用{}创建。B错误：集合用add()增加元素；C错误：列表不可哈希不能做键；D错误：items()返回所有键值对"},
    
    # 第26题 (id=85) - 修正
    "85": {"answer": "B", "explanation": "函数没有return语句时，默认返回None。pass是空语句，不返回任何值"},
    
    # 第27题 (id=86) - 修正
    "86": {"answer": "B", "explanation": "calculate()函数有参数number，有return返回值。虽然选项描述不完全准确，但B'无参有返回值'最接近（实际是有参有返回值）"},
    
    # 第28题 (id=87) - 修正
    "87": {"answer": "D", "explanation": "*args可变参数在函数内部是以元组tuple类型存储的。kwargs才是字典类型"},
    
    # 第29题 (id=88) - 修正
    "88": {"answer": "D", "explanation": "changeInt(number1)中number1=2传入，内部number2变为3并打印。但number1是值传递，外部print(number1)仍输出2。所以先打印'changeInt: number2= 3'，后打印'number: 2'"},
}

# 应用修正
for qid, fix_data in fixes.items():
    data[qid] = fix_data
    print(f"✓ 已修正第 {qid} 题")

with open('answers_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n已修正 {len(fixes)} 道选择题")
