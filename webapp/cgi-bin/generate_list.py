#! /usr/local/bin/python3

'''
glob模块是最简单的模块之一，内容非常少。
用它可以查找符合特定规则的文件路径名。
跟使用windows下的文件搜索差不多
'''
import glob
# 作者自己建立的一个用于调用选手数据的模型
import athletemodel
# 这是一个用于生成HTML文件的模块
import yate

# Return a list of paths matching a pathname pattern.
data_files = glob.glob("data/*.txt")
# 将搜索到的txt文件内容存储到athletes中
athletes = athletemodel.put_to_store(data_files)

# 下面是页面内容
print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
# 这个地址是表格内容的发送地址
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))