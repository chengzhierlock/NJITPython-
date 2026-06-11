#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正判断题第8题（id=107）答案
"""

import json

with open('answers_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修正第8题（id=107）
data["107"] = {
    "answer": "正确",
    "explanation": "列表的pop()方法在省略参数时，默认删除并返回列表的最后一个元素。例如：[1,2,3].pop()删除3，返回3，列表变为[1,2]。"
}

print("✓ 已修正第107题（判断题第8题）")

with open('answers_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("修正完成！")
