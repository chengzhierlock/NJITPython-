#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正试卷二剩余题目答案（id 89-118）
"""

import json

with open('answers_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修正答案
fixes = {
    # 第30题 (id=89) - 需要看到代码才能确定，暂时保留原答案
    
    # 填空题 (id 90-99)
    "90": {"answer": "id", "explanation": "查看变量内存地址的Python内置函数是id()。id()函数返回对象的唯一标识符，即对象在内存中的地址。"},
    "91": {"answer": "'2'", "explanation": "x, y, z = '123'是序列解包，字符串'123'被拆分为三个字符，y对应第二个字符'2'。注意答案是字符串'2'。"},
    "92": {"answer": "512", "explanation": "2**3**2 = 2**(3**2) = 2**9 = 512。幂运算从右向左结合（右结合）。"},
    "93": {"answer": "14", "explanation": "range(10, 20)生成[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]，索引4对应的值是14。"},
    "94": {"answer": "[1, 2, 3]", "explanation": "[1, 2] + [3]是列表拼接操作，结果是[1, 2, 3]。"},
    "95": {"answer": "[1, 2, 3]", "explanation": "x.extend([3])将列表[3]的元素添加到x末尾，x从[1, 2]变为[1, 2, 3]。"},
    "96": {"answer": "[7, 5, 3]", "explanation": "x.sort(reverse=True)对列表进行降序排序，[3, 7, 5]排序后为[7, 5, 3]。"},
    "97": {"answer": "4", "explanation": "x.get(3, 4)获取键3对应的值，键3不存在则返回默认值4。"},
    "98": {"answer": "True", "explanation": "x.values()返回字典的值视图，'b'是字典的值之一，所以'b' in x.values()返回True。"},
    "99": {"answer": "[1, 13, 89, 237, 100]", "explanation": "按数字的字符串长度排序：1(长度1), 13(长度2), 89(长度2), 237(长度3), 100(长度3)。sorted是稳定排序，相同长度保持原顺序。"},
    
    # 判断题 (id 100-114)
    "100": {"answer": "错误", "explanation": "Python 3.x不完全兼容Python 2.x。Python 3.x引入了许多不兼容的改动，如print成为函数、整数除法行为改变等。"},
    "101": {"answer": "正确", "explanation": "Python变量名必须以字母(a-z, A-Z)或下划线(_)开头，不能以数字开头，且区分大小写（name和Name是不同的变量）。"},
    "102": {"answer": "正确", "explanation": "如果只需要math模块中的sin()函数，建议使用from math import sin来导入。这样可以避免导入整个模块，提高代码效率和可读性。"},
    "103": {"answer": "正确", "explanation": "在Python中，单引号和双引号都可以用来定义字符串，两者功能完全相同，print()输出的结果也一样。"},
}

# 应用修正
for qid, fix_data in fixes.items():
    data[qid] = fix_data
    print(f"✓ 已修正第 {qid} 题")

with open('answers_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n已修正 {len(fixes)} 道题")
