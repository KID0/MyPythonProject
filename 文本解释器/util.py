#!/usr/bin/python
# encoding: utf-8

def lines(file):
    """
    生成器,在文本最后加一空行
    """
    for line in file: yield line
    yield '\n'
    '''
    yield是一个高阶用法，一个带有 yield 的函数就是一个 generator
    （有利复用，减少了内存占用）

    虽然执行流程仍按函数的流程执行，
    但每执行到一个 yield 语句就会中断，并返回一个迭代值，
    下次执行时从 yield 的下一个语句继续执行。
    看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
    每次中断都会通过 yield 返回当前的迭代值。
    '''

def blocks(file):
    """
    生成器,生成单独的文本块
    """
    block = []
    for line in lines(file):
        # 如果该行中有东西
        if line.strip():
            '''
            strip() 函数可以去除一个字符串前后的空格以及换行符，
            如果在strip()函数添加不同的参数，如strip("me")，
            则可以去除字符串前后的"me"字符。
            '''
            block.append(line)
        # 否则如果block里有东西
        elif block:
            yield ''.join(block).strip()
            # 将block中的所有元素连接起来，连接符为空；清楚所有空白字符，输出
            '''
            join():连接字符串数组。
            将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
            '''
            # 将block置为空
            block = []
