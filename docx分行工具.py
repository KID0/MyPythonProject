# 作者：刘浩
# 脚本作用：从docx文件中提取所有文字，每遇到一个标点符号就进行分行，将这些数据打印出来


# 帮助文档：https://python-docx.readthedocs.io/en/latest/
# 参考文献：http://blog.csdn.net/qianchenglenger/article/details/51582005


'''
组织结构：
document
  --heading
  --paragraphs(a list)
    --paragraph1
    --paragraph2
    --paragraph3
    --......
  --picture
  --table

'''

from docx import Document
document = Document('史昊正.docx')
for paragraph in document.paragraphs:
	for word in paragraph.text:
		# 注意：这里不能用and or ，这样是布尔运算
		if word in ["!","?",".",",",'！','。','？','，']:
			print(word)
		else:
			# end='' —— 不分行
			print(word,end='')

	


# document.save('test.docx')