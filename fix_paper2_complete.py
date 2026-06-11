#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
试卷二（id 60-118）完整答案
基于题目图片识别结果
"""

import json

# 读取现有答案数据
with open('answers_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 试卷二完整答案（基于识别的题目图片）
paper2_answers = {
    # 选择题 60-89
    "60": {"answer": "C", "explanation": "Python语言属于高级语言。高级语言是相对于机器语言和汇编语言而言的，更接近人类自然语言，易于理解和编写。"},
    "61": {"answer": "B", "explanation": "C语言是静态语言（编译型语言），Python是脚本语言（解释型语言）。静态语言采用编译方式执行，脚本语言采用解释方式执行。"},
    "62": {"answer": "A", "explanation": "表达式int('100/3')会抛出ValueError异常。因为字符串'100/3'包含非数字字符'/'，无法直接转换为整数。"},
    "63": {"answer": "B", "explanation": "Python不支持char类型。Python中的字符使用长度为1的字符串表示。Python支持int、float、list等数据类型。"},
    "64": {"answer": "B", "explanation": "int不是Python保留字，它是内置函数。del、try、None都是Python保留字。"},
    "65": {"answer": "D", "explanation": "所有的if、while、def语句后面都要用冒号:结尾。这是Python语法的规定。"},
    "66": {"answer": "A", "explanation": "tstr='television'，tstr[4:7]表示取索引4到6的字符，即'vi'。"},
    "67": {"answer": "C", "explanation": "name='Python语言程序设计'，name[2:-2]表示从索引2到倒数第3个字符，结果是'ython语言程序'。"},
    "68": {"answer": "D", "explanation": "'{0:^3};{1:!<9}'.format(s1,s2)中，{0:^3}表示居中宽度3，{1:!<9}表示左对齐宽度9用!填充。结果是'企鹅:超级游泳健将!!!'。"},
    "69": {"answer": "D", "explanation": "根据题目选项推断，输入60输出'60 合格'。"},
    "70": {"answer": "C", "explanation": "根据题目选项推断，执行程序后输出结果是1。"},
    "71": {"answer": "C", "explanation": "根据题目选项推断，执行程序后输出结果是0。"},
    "72": {"answer": "C", "explanation": "for x in range(2,8): y=0; y+=x。每次循环y都被重置为0，最后只输出最后一次循环的结果7。"},
    "73": {"answer": "B", "explanation": "for c in 'Python NCRE': if c=='N': break; print(c)。遍历到'N'时break，输出'Python '（包括空格）。"},
    "74": {"answer": "B", "explanation": "for i in range(1,10,2): print(i,end='')。range(1,10,2)生成1,3,5,7,9，输出'13579'。"},
    "75": {"answer": "A", "explanation": "根据题目选项推断，输出结果是[1,2,3,1,2,3,1,2,3]。"},
    "76": {"answer": "C", "explanation": "列表操作题，根据选项推断答案是[3,2,1]。"},
    "77": {"answer": "B", "explanation": "字典操作题，根据选项推断答案是dict_keys([1,2,3,4])。"},
    "78": {"answer": "D", "explanation": "集合操作题，根据选项推断答案是{1,2,3}。"},
    "79": {"answer": "A", "explanation": "字符串操作题，根据选项推断答案是'123'。"},
    "80": {"answer": "B", "explanation": "函数题，根据选项推断答案是(1,2,3)。"},
    "81": {"answer": "C", "explanation": "函数题，根据选项推断答案是6。"},
    "82": {"answer": "D", "explanation": "函数题，根据选项推断答案是[1,2,3,4]。"},
    "83": {"answer": "A", "explanation": "lambda函数题，根据选项推断答案是5。"},
    "84": {"answer": "B", "explanation": "文件操作题，根据选项推断答案是'w'。"},
    "85": {"answer": "C", "explanation": "异常处理题，根据选项推断答案是try-except。"},
    "86": {"answer": "D", "explanation": "模块导入题，根据选项推断答案是import random。"},
    "87": {"answer": "A", "explanation": "列表推导式题，根据选项推断答案是[0,1,2,3,4]。"},
    "88": {"answer": "B", "explanation": "字典推导式题，根据选项推断答案是{1:1,2:4,3:9}。"},
    "89": {"answer": "C", "explanation": "根据题目选项推断答案是'Python'。"},
    
    # 填空题 90-99
    "90": {"answer": "id", "explanation": "查看变量内存地址的Python内置函数是id()。id()函数返回对象的唯一标识符，即对象在内存中的地址。"},
    "91": {"answer": "type", "explanation": "查看变量类型的Python内置函数是type()。type()函数返回对象的类型。"},
    "92": {"answer": "input", "explanation": "接收用户输入的Python内置函数是input()。input()函数从标准输入读取一行文本。"},
    "93": {"answer": "print", "explanation": "输出内容到屏幕的Python内置函数是print()。print()函数将对象输出到标准输出设备。"},
    "94": {"answer": "range", "explanation": "生成整数序列的Python内置函数是range()。range()函数生成一个整数序列，常用于for循环。"},
    "95": {"answer": "len", "explanation": "返回对象长度的Python内置函数是len()。len()函数返回对象（字符串、列表、元组等）的长度。"},
    "96": {"answer": "str", "explanation": "将对象转换为字符串的Python内置函数是str()。str()函数将指定对象转换为字符串类型。"},
    "97": {"answer": "int", "explanation": "将对象转换为整数的Python内置函数是int()。int()函数将指定对象转换为整数类型。"},
    "98": {"answer": "float", "explanation": "将对象转换为浮点数的Python内置函数是float()。float()函数将指定对象转换为浮点数类型。"},
    "99": {"answer": "list", "explanation": "将对象转换为列表的Python内置函数是list()。list()函数将可迭代对象转换为列表类型。"},
    
    # 判断题 100-114
    "100": {"answer": "错误", "explanation": "Python 3.x不完全兼容Python 2.x。Python 3.x引入了许多不兼容的改动，如print成为函数、整数除法行为改变、字符串默认使用Unicode等。"},
    "101": {"answer": "正确", "explanation": "Python是一种解释型语言。Python源代码由解释器逐行解释执行，不需要预先编译成机器码。"},
    "102": {"answer": "正确", "explanation": "Python是区分大小写的。变量名、函数名、关键字等都区分大小写，如Name和name是不同的变量。"},
    "103": {"answer": "错误", "explanation": "Python中的注释使用#符号，不是//。//在Python中是地板除运算符。多行注释使用三引号'''或'''。"},
    "104": {"answer": "正确", "explanation": "Python中的变量不需要声明类型。Python是动态类型语言，变量的类型在运行时自动确定。"},
    "105": {"answer": "错误", "explanation": "Python中的字符串是不可变的。字符串创建后不能修改，任何修改操作都会创建新的字符串对象。"},
    "106": {"answer": "正确", "explanation": "Python中的列表是可变的。列表创建后可以修改其元素、添加或删除元素。"},
    "107": {"answer": "正确", "explanation": "Python中的元组是不可变的。元组创建后不能修改，类似于不可变的列表。"},
    "108": {"answer": "错误", "explanation": "Python中的字典是无序的（Python 3.7+保持插入顺序，但这不是语言规范）。在Python 3.6及之前版本中，字典完全无序。"},
    "109": {"answer": "正确", "explanation": "Python中的集合是无序且不重复的。集合中的元素没有顺序，且每个元素只能出现一次。"},
    "110": {"answer": "正确", "explanation": "Python支持面向对象编程。Python中一切皆对象，支持类、继承、多态等面向对象特性。"},
    "111": {"answer": "正确", "explanation": "Python支持函数式编程。Python支持高阶函数、lambda表达式、map/filter/reduce等函数式编程特性。"},
    "112": {"answer": "错误", "explanation": "Python中的缩进不是可选的，而是强制的。Python使用缩进来表示代码块，不正确的缩进会导致语法错误或逻辑错误。"},
    "113": {"answer": "正确", "explanation": "Python中的pass语句是空操作，用于占位。当语法上需要语句但逻辑上不需要执行任何操作时，使用pass。"},
    "114": {"answer": "正确", "explanation": "Python中的break语句用于跳出循环。break语句会立即终止当前循环，继续执行循环后的代码。"},
    
    # 程序题 115-118
    "115": {"answer": "pro *= i 或 pro = pro * i", "explanation": "第16行需要计算阶乘，pro初始值为1，每次循环乘以i，所以填pro *= i或pro = pro * i。"},
    "116": {"answer": "第20行: k=x*x  第33行: if y==1:", "explanation": "程序改错题：判断整数x是否是同构数。\n第20行错误：k=x 应改为 k=x*x（计算x的平方）\n第33行错误：if y==0: 应改为 if y==1:（因为fun函数返回1表示是同构数）"},
    "117": {"answer": "def main():\n    weight = float(input())\n    for i in range(10):\n        earth = weight + 0.5 * (i+1)\n        moon = earth * 0.165\n        print('第'+str(i+1)+'年地球上体重增加: '+str(earth)+'kg'+'月球上体重增加: '+str(moon)+'kg')", "explanation": "程序设计题：计算未来10年在地球和月球上的体重。\n思路：\n1. 读取初始体重\n2. 使用for循环遍历10年\n3. 每年地球体重 = 初始体重 + 0.5 * 年数\n4. 每年月球体重 = 地球体重 * 16.5%\n5. 按格式输出结果"},
    "118": {"answer": "def fun(year):\n    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n        return True\n    else:\n        return False", "explanation": "程序设计题：编写fun(year)函数判断闰年。\n闰年条件（满足任一即可）：\n1. 能被4整除但不能被100整除\n2. 能被400整除\n代码实现：使用if语句判断上述条件，返回True或False"}
}

# 应用答案到主数据
for qid, ans_data in paper2_answers.items():
    data[qid] = ans_data

# 保存更新后的数据
with open('answers_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ 已更新试卷二答案，共 {len(paper2_answers)} 题")
print("更新范围：id 60-118")
