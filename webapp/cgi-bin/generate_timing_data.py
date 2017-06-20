#! /usr/local/bin/python3

# 以下两行代码用于追踪服务器运行，在Web界面上显示错误信息，一般调试时使用
# import cgitb
# cgitb.enable()

# 一系列实用的CGI脚本
import cgi

import athletemodel
import yate

# 从模型得到数据
athletes = athletemodel.get_from_store()

# 以下两行为获取某一特定选手的数据
# 获取表单数据存放在一个字典
form_data = cgi.FieldStorage()
# 从表单访问一个指定数据
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))    
print(yate.header("Athlete: " + athlete_name + ", DOB: " +
                      athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3))
# 在页面上增加两个链接
print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete": "cgi-bin/generate_list.py"}))