# -*- coding:UTF-8 -*-  
#! /usr/bin/python3  
# 本游戏使用WASD控制
  
import random  
# 定义一个矩阵储存数据
v = [[0, 0, 0, 0],  
     [0, 0, 0, 0],  
     [0, 0, 0, 0],  
     [0, 0, 0, 0]]  

# 显示界面
# 输入矩阵和总分
def display(v, score):  
        # 将每一行使用标准格式输出
        # '{第n个数据：占几个字符的空间}'.format(需要格式化的数据)
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[0][0], v[0][1], v[0][2], v[0][3]))  
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[1][0], v[1][1], v[1][2], v[1][3]))  
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[2][0], v[2][1], v[2][2], v[2][3]))  
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[3][0], v[3][1], v[3][2], v[3][3]))   
        print('Total score: ', score)  

# 初始化
def init(v):      
        # 重复四次
        for i in range(4): 
                # v本身就是一个含有四个数据的“列表”
                v[i] = [random.choice([0, 0, 0, 2, 2, 4]) for x in v[i]]  
  
# 对齐非零的数字
# vList: 列表结构，存储了一行（列）中的数据 
# direction: 移动方向,向上和向左都使用方向'left'，向右和向下都使用'right' 
def align(vList, direction):  
        # 移除列表中的0  
        # count()方法返回子字符串在字符串中出现的次数
        # remove()方法移除一个“0”(用一次这个方法去掉一个“0”)
        for i in range(vList.count(0)):  
                vList.remove(0)
        # 这里将“0”补到后面（觉得好笨拙）
        # 这里的vList是移除“0”后的vList，长度不一定是4
        zeros = [0 for x in range(4 - len(vList))]  
        # 在非0数字的一侧补充0  
        if direction == 'left':  
                vList.extend(zeros)  
        else:  
                # 这里不是很懂？
                vList[:0] = zeros


# 在列表查找相同且相邻的数字相加,找到符合条件的返回True,同时还返回增加的分数
def addSame(vList, direction):  
        score = 0  
        if direction == 'left':  
                for i in [0, 1, 2]:  
                        # 注意这个连等式
                        if vList[i] == vList[i+1] != 0:   
                                vList[i] *= 2  
                                vList[i+1] = 0  
                                score += vList[i]  
                                # 返回了一个字典
                                return {'bool':True, 'score':score}  
        # direction == 'right'
        else:  
                for i in [3, 2, 1]:  
                        if vList[i] == vList[i-1] != 0:  
                                vList[i-1] *= 2  
                                vList[i] = 0  
                                score += vList[i-1]  
                                return {'bool':True, 'score':score} 
        # 如果既没有left，也没有right
        return {'bool':False, 'score':score}  

# 处理一行（列）中的数据，得到最终的该行（列）的数字状态值, 返回得分
def handle(vList, direction):  
        # 加总分
        totalScore = 0  
        # 这算一个触发
        align(vList, direction)  
        result = addSame(vList, direction)  

        # 'bool' == True --> 这是一次成功的移动
        while result['bool'] == True:  
                # 然后不断循环下去
                totalScore += result['score']  
                align(vList, direction)  
                result = addSame(vList, direction)  
        return totalScore  
          
# 根据移动方向重新计算矩阵状态值，并记录得分
def operation(v):  

        totalScore = 0  
        gameOver = False  
        direction = 'left'  
        op = input('operator:')  
        if op in ['a', 'A']:    # 向左移动  
                direction = 'left'  
                for row in range(4):  
                        totalScore += handle(v[row], direction)  
        elif op in ['d', 'D']:  # 向右移动  
                direction = 'right'  
                for row in range(4):  
                        totalScore += handle(v[row], direction)  
        elif op in ['w', 'W']:  # 向上移动  
                direction = 'left'  
                for col in range(4):  
                        # 将矩阵中一列复制到一个列表中然后处理  
                        vList = [v[row][col] for row in range(4)]  
                        totalScore += handle(vList, direction)  
                        # 从处理后的列表中的数字覆盖原来矩阵中的值  
                        for row in range(4):  
                                v[row][col] = vList[row]  
        elif op in ['s', 'S']:  # 向下移动  
                direction = 'right'  
                for col in range(4):  
                        # 同上  
                        vList = [v[row][col] for row in range(4)]  
                        totalScore += handle(vList, direction)  
                        for row in range(4):  
                                v[row][col] = vList[row]  
        else:  
                print('Invalid input, please enter a charactor in [W, S, A, D] or the lower')  
                return {'gameOver':gameOver, 'score':totalScore}  
  
        # 统计空白区域数目 N  
        N = 0  
        # 就是计算四次
        for q in v:  
            N += q.count(0)  
        # 不存在剩余的空白区域时，游戏结束  
        if N == 0:  
                gameOver = True  
                return {'gameOver':gameOver, 'score':totalScore}  
  
        # 按2和4出现的几率为3：1来产生随机数2和4  
        num = random.choice([2, 2, 2, 4])   
        # 产生随机数k，上一步产生的2或4将被填到第k个空白区域  
        # randrange()方法：输出x，1<=x<N+1
        k = random.randrange(1, N+1)  
        n = 0  
        for i in range(4):  
                for j in range(4):  
                        if v[i][j] == 0:  
                                n += 1  
                                if n == k:  
                                        v[i][j] = num  
                                        break  
  
        return {'gameOver':gameOver, 'score':totalScore}  

# 初始化
init(v)  
score = 0  
print('Input：W(Up) S(Down) A(Left) D(Right), press <CR>.')  
while True:
        # 展示计分板
        display(v, score)  
        # 输入WASD，计算一次
        # operation()中，gameOver一开始的定义是False
        result = operation(v)  
        if result['gameOver'] == True:  
                print('Game Over, You failed!')  
                print('Your total score:', score)  
        else:  
                score += result['score']  
                if score >= 2048:  
                        print('Game Over, You Win!!!')  
                        print('Your total score:', score)  