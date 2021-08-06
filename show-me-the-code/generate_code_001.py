# -*- coding:utf-8 -*-
# coding=utf-8
# 第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）


import string
import random

forSelect = string.ascii_letters+string.digits


def generate_code(count, length):
    for i in range(count):
        code = ""
        for j in range(length):
            code += random.choice(forSelect)
        print('%s): %s' % (i+1, code))


def generate_code_to_txt(count, length, path):
    f = open(path, 'w')
    for i in range(count):
        code = ""
        for j in range(length):
            code += random.choice(forSelect)
        # print('%s): %s' % (i+1, code))
        f.write(code+"\n")
    f.close()


if __name__ == "__main__":
    generate_code(200, 20)
    generate_code_to_txt(
        200, 20, "编程练习/python练习/show-me-the-code/coupon.txt")
