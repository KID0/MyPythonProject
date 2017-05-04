#! /usr/bin/env python
# coding: UTF-8
# python3.3

# 2048的逻辑模型

import random

SIDE = 4
num = 0
# 初始化
def init():
    '''
    init matrix
    '''
    global num
    num = 0
    # matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # 创造一个4X4的矩阵
    matrix = [[0 for i in range(SIDE)] for i in range(SIDE)]

    # generate 2 different number
    # random.sample(seq, n) 从序列seq中选择n个随机且独立的元素；
    random_lst = random.sample( range(SIDE*SIDE), 2 )

    # 将上一行选出来的两个位置的数值设置为“2”
    matrix[random_lst[0]//SIDE][random_lst[0]%SIDE] = 2
    matrix[random_lst[1]//SIDE][random_lst[1]%SIDE] = 2
    
    return matrix

def move_right(matrix):
    '''
    move right
    '''
    # 其实还是将4X4的矩阵分成4行，逐行处理
    right_list = []
    for item_list in matrix:
        right_list.append(handle_list_item_right(item_list))
    return right_list

def move_left(matrix):
    '''
    move left
    '''
    right_list = []
    for item_list in matrix:
        right_list.append(handle_list_item_left(item_list))
    return right_list

# 一般来说，上下就是左右的变形
def move_down(matrix):
    '''
    move down
    '''
    down_list = []
    # 这个真心看不懂
    config_list = [0, 0, 1, matrix]
    matrix = inversion_data_list(config_list)
    for item_list in matrix:
        down_list.append(handle_list_item_right(item_list))

    config_list = [0, 0, 1, down_list]
    down_list = inversion_data_list(config_list)

    return down_list

def move_up(matrix):
    '''
    move up
    '''
    up_list = []
    config_list = [0, 0, 1, matrix]
    matrix = inversion_data_list(config_list)
    for item_list in matrix:
        up_list.append(handle_list_item_left(item_list))

    config_list = [0, 0, 1, up_list]
    up_list = inversion_data_list(config_list)

    return up_list

def insert(matrix):
    """
    insert one 2 or 4 into the matrix. return the matrix list
    """
    getZeroIndex = []
    for i in range(SIDE):
        for j in range(SIDE):
            if matrix[i][j] == 0:
                getZeroIndex.append([i, j])
    if getZeroIndex != []:
        randomZeroIndex = random.choice(getZeroIndex)
        matrix[randomZeroIndex[0]][randomZeroIndex[1]] = random.choice([2,4])
    return matrix

def is_over(matrix):
    """
    is game over? return bool
    """
    for item_list in matrix:
        if 0 in item_list:
            return False

    for i in range(SIDE):
        for j in range(SIDE):
            if i < SIDE - 1:
                if matrix[i][j] == matrix[i+1][j]:
                    return False
            if j < SIDE - 1:
                if matrix[i][j] == matrix[i][j+1]:
                    return False
    return True

def is_win(matrix):
    """
    is game win? return bool
    """
    for item_list in matrix:
        if 2048 in item_list:
            return True
    return False

def handle_list_item_right(my_list):
    '''
    '''
    list_0 = del_item_0(my_list)
    list_0 = add_same_number(list_0)
    list_1 = del_item_0(list_0)
    list_1 = add_item_0(list_1, 'right')
    return list_1

def handle_list_item_left(my_list):
    '''
    '''
    list_0 = del_item_0(my_list)
    list_0 = add_same_number(list_0)
    list_1 = del_item_0(list_0)
    list_1 = add_item_0(list_1, 'left')
    return list_1

def del_item_0(my_list):
    '''
    del when the item is 0. eg:[0, 0, 0, 2] -> [2]
    '''
    list_0 = []
    for item in my_list:
        if item != 0:
            list_0.append(item)
    return list_0

def add_item_0(my_list, direction):
    '''
    add the item 0. eg:[2] -> [0, 0, 0, 2]
    '''
    for i in range(SIDE - len(my_list)):
        if direction == 'right':
            my_list.insert(0, 0)
        elif direction == 'left':
            my_list.append(0)
    return my_list

def add_same_number(my_list):
    '''
    add same number. eg:[2, 2, 4] -> [0, 4, 4]
    '''
    global num
    for i in range(len(my_list)-1, -1, -1):
        if i >= 1:
            if my_list[i-1] == my_list[i]:
                my_list[i-1] = 0
                my_list[i] = 2*my_list[i]
                num += my_list[i]
                break
    return my_list

def getScore():
    global num
    return num 

def inversion_data_list(config_list):
    ''' 
    @action: Return a inversion list
    @param: config_list:
            [inversion_x_flag, inversion_y_flag, inversion_xy_flag, data_list]
    @return: the inversion_result_list  
    '''
    data_list = config_list[3]

    if config_list[2] == 1:
        new_list = []
        for i in range(len(data_list[0])):
            temp_list = []
            for j in range(len(data_list)):
                temp_list.append(data_list[j][i])
            new_list.append(temp_list)
        data_list = new_list

    if config_list[0] == 1:
        new_list = []
        for temp_list in data_list:
            new_list.insert(0,temp_list)
        data_list = new_list

    if config_list[1] == 1:
        new_list = []
        for temp_list in data_list:
            new_list.append(temp_list[::-1])
        data_list = new_list
    return data_list


#if __name__ == '__main__':
    '''
    '''
#    print(add_same_number([2, 2, 4]))
