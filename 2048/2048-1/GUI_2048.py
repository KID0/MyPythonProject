#-*-coding:utf-8-*-
#python3.3.5
from graphics import*

# 该文件为作者基于graphic库写的一个GUI界面
# 初始化并构建2048界面
def init():
    win = GraphWin("2048", 260, 450)
    win.master.geometry('+400+150')  #屏幕位置
    c = color_rgb(206, 194, 180) 
    win.setBackground(c)
    mainGui(win)
    return win 

#2048方格
def rectangle_2048(win, p1 = Point(10, 10),txt='',c = color_rgb(206, 194, 180)): 
    p2 = Point(p1.x + 60, p1.y + 60)
    r = _rectangle(win,p1,p2,c)
    t = _text(win,p1,p2,txt)
    return r,t

#挂牌
def hint(win,p1 = Point(10, 10)): 
    p2 = Point(p1.x + 240, p1.y + 40)
    c = color_rgb(187, 173, 164)
    _rectangle(win,p1,p2,c)
    t = _text(win,p1,p2,'真英雄 挑战2048~') 
    t.setTextColor(color_rgb(238, 231, 221))
    return t
    
#标题logo
def _title(win,p1 = Point(10, 60)): 
    p2 = Point(p1.x + 120, p1.y + 120)
    c = color_rgb(228, 184, 0)
    _rectangle(win,p1,p2,c)
    t = Text(Point((p2.x + p1.x) / 2, (p2.y + p1.y) / 2), '2048')
    t.setSize(35)
    t.setStyle('bold')
    t.setTextColor('white')
    t.draw(win)
    
#画正方形
def _rectangle(win,p1,p2,c):
    r = Rectangle(p1, p2) 
    r.setFill(c) 
    r.setOutline(color_rgb(198, 186, 174))
    r.draw(win)
    return r
    
#写文字    
def _text(win,p1,p2,txt):
    t = Text(Point((p2.x + p1.x) / 2, (p2.y + p1.y) / 2), txt)
    t.draw(win)
    return t

#网格
def _grid(win,p1 = Point(10, 190)):
    #上面 
    p_u_1 = Point(p1.x + 60, p1.y) 
    p_u_2 = Point(p1.x + 120, p1.y)
    p_u_3 = Point(p1.x + 180, p1.y)
    p_u_4 = Point(p1.x + 240, p1.y)

    #左面
    p_l_1 = Point(p1.x, p1.y + 60) 
    p_l_2 = Point(p1.x, p1.y + 120)
    p_l_3 = Point(p1.x , p1.y + 180)
    p_l_4 = Point(p1.x , p1.y + 240)

    #右面
    p_r_1 = Point(p1.x + 240, p1.y + 60)
    p_r_2 = Point(p1.x + 240, p1.y + 120)
    p_r_3 = Point(p1.x + 240, p1.y + 180)
    p_r_4 = Point(p1.x + 240, p1.y + 240)
    
    #下面
    p_d_1 = Point(p1.x + 60 , p1.y + 240)
    p_d_2 = Point(p1.x + 120 , p1.y + 240)
    p_d_3 = Point(p1.x + 180 , p1.y + 240)
    p_d_4 = Point(p1.x + 240 , p1.y + 240)
 
    c = color_rgb(198, 186, 174) 
    #画横线
    l_W_1 = Line(p1, p_u_4)
    l_W_2 = Line(p_l_1, p_r_1)
    l_W_3 = Line(p_l_2, p_r_2)
    l_W_4 = Line(p_l_3, p_r_3)
    l_W_5 = Line(p_l_4, p_r_4)
    
    l_W_1.setFill(c)
    l_W_2.setFill(c)
    l_W_3.setFill(c)
    l_W_4.setFill(c)
    l_W_5.setFill(c)
    
    l_W_1.draw(win)
    l_W_2.draw(win)
    l_W_3.draw(win)
    l_W_4.draw(win)
    l_W_5.draw(win)

    #画竖线
    l_H_1 = Line(p1, p_l_4)
    l_H_2 = Line(p_u_1, p_d_1)
    l_H_3 = Line(p_u_2, p_d_2)
    l_H_4 = Line(p_u_3, p_d_3)
    l_H_5 = Line(p_u_4, p_d_4)
    
    l_H_1.setFill(c)
    l_H_2.setFill(c)
    l_H_3.setFill(c)
    l_H_4.setFill(c)
    l_H_5.setFill(c)
    
    l_H_1.draw(win)
    l_H_2.draw(win)
    l_H_3.draw(win)
    l_H_4.draw(win)
    l_H_5.draw(win)

#最佳成绩
def maxScore(win,p1 = Point(135, 60)): 
    p2 = Point(p1.x + 115, p1.y + 30)
    c = color_rgb(187, 173, 164)
    _rectangle(win,p1,p2,c)
    _text(win,p1,p2,'最佳成绩:')
    
#当前分数
def curScore(win,p1 = Point(135, 120)): 
    p2 = Point(p1.x + 115, p1.y + 30)
    c = color_rgb(187, 173, 164)
    _rectangle(win,p1,p2,c)
    _text(win,p1,p2,'当前分数:')
    
#界面集合
def mainGui(win):
    hint(win)
    _title(win)
    _grid(win)
    maxScore(win)
    curScore(win) 
    
