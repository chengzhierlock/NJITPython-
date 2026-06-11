#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正试卷二所有剩余题目答案
"""

import json

with open('answers_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修正所有剩余题目
fixes = {
    # 判断题第5-15题 (id 104-114)
    "104": {"answer": "正确", "explanation": "Python语法规定，if条件语句后面必须使用冒号:来表示代码块的开始。"},
    "105": {"answer": "错误", "explanation": "break和continue语句不能单独使用，必须在循环体内（for或while循环）使用，用于控制循环流程。"},
    "106": {"answer": "正确", "explanation": "range()函数用于生成一个整数序列，常用于for循环中。例如range(5)生成0,1,2,3,4。"},
    "107": {"answer": "错误", "explanation": "列表x=[1,2,3]，执行x=3后，变量x指向新的整数对象3，内存地址发生改变。整数和列表是不同的对象。"},
    "108": {"answer": "错误", "explanation": "tuple('physics')将字符串拆分为字符元组，结果是('p','h','y','s','i','c','s')，不是('physics')。"},
    "109": {"answer": "错误", "explanation": "Python字典只能通过键索引获取值，不能通过值反向索引获取键。字典是单向映射结构。"},
    "110": {"answer": "正确", "explanation": "删除列表重复元素最简单的方法是转换为集合再转回列表：list(set(lst))。集合会自动去重，但会改变元素顺序。"},
    "111": {"answer": "错误", "explanation": "集合是可变类型，不可哈希，不能作为字典的键。只有不可变类型（如字符串、数字、元组）才能作为字典键。"},
    "112": {"answer": "正确", "explanation": "lambda表达式创建的是匿名函数对象，属于可调用对象，可以像普通函数一样被调用执行。"},
    
    # 程序题 (id 115-118)
    "115": {"answer": "pro *= i 或 pro = pro * i", "explanation": "第16行计算阶乘，pro初始值为1，每次循环乘以i，所以填pro *= i。第29行累加阶乘结果，填s += cal(i)或s = s + cal(i)。"},
    "116": {"answer": "第20行: k=x*x  第33行: if y==1:", "explanation": "程序改错题：判断整数x是否是同构数。第20行k=x应改为k=x*x（计算x的平方）；第33行if y==0:应改为if y==1:（因为fun函数返回1表示是同构数）。"},
    "117": {"answer": "def main():\n    weight = float(input())\n    for i in range(10):\n        earth = weight + 0.5 * (i+1)\n        moon = earth * 0.165\n        print('第'+str(i+1)+'年地球上体重增加: '+str(earth)+'kg'+'月球上体重增加: '+str(moon)+'kg')", "explanation": "程序设计题：计算未来10年在地球和月球上的体重。思路：1.读取初始体重；2.使用for循环遍历10年；3.每年地球体重=初始体重+0.5*年数；4.每年月球体重=地球体重*16.5%；5.按格式输出结果。"},
    "118": {"answer": "def fun(year):\n    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n        return True\n    else:\n        return False", "explanation": "程序设计题：编写fun(year)函数判断闰年。闰年条件（满足任一即可）：1.能被4整除但不能被100整除；2.能被400整除。代码实现：使用if语句判断上述条件，返回True或False。"},
}

# 应用修正
for qid, fix_data in fixes.items():
    data[qid] = fix_data
    print(f"✓ 已修正第 {qid} 题")

with open('answers_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n已修正 {len(fixes)} 道题")
print("试卷二（id 60-118）全部答案已更新完成！")
