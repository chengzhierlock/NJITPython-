#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复试卷二（id 60-118）的答案
根据实际题目图片重新核对并修正答案
"""

import json

# 读取现有答案数据
with open('answers_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 试卷二需要修正的答案
paper2_fixes = {
    # 第116题 - 程序改错（同构数判断）
    "116": {
        "answer": "第20行: k=x*x  第33行: if y==1:",
        "explanation": "程序改错题：判断整数x是否是同构数。\n第20行错误：k=x 应改为 k=x*x（计算x的平方）\n第33行错误：if y==0: 应改为 if y==1:（因为fun函数返回1表示是同构数）"
    },
    # 第117题 - 程序设计（体重计算）
    "117": {
        "answer": "def main():\n    weight = float(input())\n    for i in range(10):\n        earth = weight + 0.5 * (i+1)\n        moon = earth * 0.165\n        print('第'+str(i+1)+'年地球上体重增加: '+str(earth)+'kg'+'月球上体重增加: '+str(moon)+'kg')",
        "explanation": "程序设计题：计算未来10年在地球和月球上的体重。\n思路：\n1. 读取初始体重\n2. 使用for循环遍历10年\n3. 每年地球体重 = 初始体重 + 0.5 * 年数\n4. 每年月球体重 = 地球体重 * 16.5%\n5. 按格式输出结果"
    },
    # 第118题 - 程序设计（闰年判断）
    "118": {
        "answer": "def fun(year):\n    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n        return True\n    else:\n        return False",
        "explanation": "程序设计题：编写fun(year)函数判断闰年。\n闰年条件（满足任一即可）：\n1. 能被4整除但不能被100整除\n2. 能被400整除\n代码实现：使用if语句判断上述条件，返回True或False"
    }
}

# 应用修正
for qid, fix_data in paper2_fixes.items():
    if qid in data:
        data[qid] = fix_data
        print(f"✓ 已修正第 {qid} 题")
    else:
        print(f"✗ 第 {qid} 题不存在")

# 保存修正后的数据
with open('answers_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n试卷二答案修复完成！")
print("修正的题目：116（程序改错）、117（体重计算程序设计）、118（闰年判断程序设计）")
