#-*-coding:utf-8-*-
#python3.3.5
# 该文件格式为pyx，和py区别不大，可以不用管
# 该文件就是主程序了

from graphics import*  # 导入一个图形库

# Tkinter模块("Tk 接口")是Python的标准Tk GUI工具包的接口
from tkinter.messagebox import askquestion
from tkinter.messagebox import showinfo 
# ConfigParser模块【读写配置文件】  
# model是主控程序
import time,random,model,configparser
# GUI_2048是作者为2048写的一个图形库
import GUI_2048 as g
 
# 唯一的一个类
class Application():
    '''
    初始化应用程序
    '''
    def __init__(self): 
        self.matrix = model.init()
        self.win = g.init()
        self.create_r_2048(self.win)
        self.show_matrix(self.matrix) 
        self.win.master.bind("<Key>", self.bind_key)
        while 1:
            update()
    
    '''
    创建网格上的16个方格、最佳成绩、当前分数
    '''
    # ???
    def create_r_2048(self,win): 
        p = Point(10, 190)
        n = 4
        self.rt =  [0 for row in range(n*n)]
        for i in range(n): 
            for a in range(n): 
                _p = Point(p.x + 60*i, p.y + 60*a) 
                self.rt[i+4*a] = g.rectangle_2048(win,_p)

        #最佳成绩
        self.zjcj = g._text(win,Point(135, 60 + 30),Point(135 + 115, 60 + 30 + 30),self.getMaxScore())
        #当前分数
        self.dqjf = g._text(win,Point(135, 120 + 30),Point(135 + 115, 120 + 30 + 30),'0')
         
    
    '''
    从配置文件中获取最佳成绩
    '''      
    def getMaxScore(self):
        config = configparser.ConfigParser() 
        config.read('config.ini')  
        maxScore = config.get("Score", "maxScore") 
        return maxScore
    
    '''
    把最佳成绩写入配置文件
    '''  
    def setMaxScore(self,score):
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read('config.ini')  
        config.set("Score", "maxScore",str(score)) 
        config.write(open("config.ini", "w"))
    
    '''
    初始化数据和界面，在游戏结束后调用
    '''
    def my_init(self):
        maxScore = self.getMaxScore()
        if int(maxScore) < model.getScore(): 
            self.setMaxScore(model.getScore())
            self.zjcj.setText(model.getScore())
        matrix = model.init() 
        self.dqjf.setText(model.getScore())
        return matrix
    
    '''
    绑定键盘事件 捕获上下左右和Q键
    '''    
    def bind_key(self, event):
        '''
        key event
        '''
        # 判断游戏是否已经结束
        if model.is_over(self.matrix):
            if askquestion("GAME OVER","GAME OVER!\nDo you want to init it?") == 'yes':
                self.matrix = self.my_init() 
                self.show_matrix(self.matrix)
                return
            else:
                self.win.close()
        else:
            if event.keysym.lower() == "q":
                self.win.close()
            elif event.keysym == "Left":
                self.matrix = model.move_left(self.matrix)
            elif event.keysym == "Right":
                self.matrix = model.move_right(self.matrix)
            elif event.keysym == "Up":
                self.matrix = model.move_up(self.matrix)
            elif event.keysym == "Down":
                self.matrix = model.move_down(self.matrix)  
                       
            if event.keysym in ["q", "Left", "Right", "Up", "Down"]:
                try:
                    self.matrix = model.insert(self.matrix)
                    self.dqjf.setText(model.getScore())
                    self.show_matrix(self.matrix)
                except:
                    pass 

        if model.is_win(self.matrix):
            if askquestion("WIN","You win the game!\nDo you want to init it?") == 'yes':
                self.matrix = self.my_init() 
                self.show_matrix(self.matrix)
                return
            else:
                self.win.close() 

    '''
    从二维数组中获取结果数据并展示在16方格中
    ''' 
    def show_matrix(self, matrix): 
        for i in range(16):
            num = matrix[i//4][i%4]
            print(num)
            if num == 0:
                num = ''
            self.rectangle_2048(i,num)
            
    
    '''
    对16个方格做颜色和数字变更
    '''
    def rectangle_2048(self,i,num): 
        # 计算相应数值
        c = color_rgb(200, 190, 180)
        if num == 2:
            c = color_rgb(240, 230, 220)
        elif num == 4:
            c = color_rgb(240, 220, 200) 
        elif num == 8:
            c = color_rgb(240, 180, 120)  
        elif num == 16:
            c = color_rgb(240, 140, 90)  
        elif num == 32:
            c = color_rgb(240, 120, 90)  
        elif num == 64:
            c = color_rgb(240, 90, 60)  
        elif num == 128:
            c = color_rgb(240, 90, 50)   
        elif num == 256:
            c = color_rgb(240, 200, 70) 
        elif num == 512:
            c = color_rgb(240, 200, 70)  
        elif num == 1024:
            c = color_rgb(0, 130, 0)  
        elif num == 2048:
            c = color_rgb(0, 130, 0)
            
        '''
        循环设置颜色和数字
        '''
        self.rt[i][0].setFill(c)
        self.rt[i][1].setText(num)
         
#main
Application()