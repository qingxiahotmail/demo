#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import messagebox
import _tkinter
import tkinter as tk
import tkinter.messagebox
import os
from typing import Any

root = tk.Tk()
root.geometry('300x300')
#设置窗口大小
root.title("自动生成文摘")
canvas_width = 160
canvas_height =160
canvas = tk.Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

img = tk.PhotoImage(file="hello.gif")
canvas.create_image((60,60),  image=img)
def hello():
    print ("hello!")
def newfile():
        file = open(r'test.txt', 'w')
        file.close()
        messagebox.showinfo('新建文件','您已成功新建文档test.txt')   # 显示对话框
def sendpic():
        str1=('python sendpic.py')
        p=os.system(str1)
        messagebox.showinfo('已经成功识别微信发送照片')   # 显示对话框
        return p
def openfile():
        f = open(r'ocr1.txt', 'r')
        try:
            f_read=f.read()
            #f_read_decode=f_read.decode('utf-8')
            print(f_read)
        finally:
            f.close()
        messagebox.showinfo('请对ocr1.txt进行编辑')   # 显示对话框
def savefile():
        messagebox.showwarning('保存文件', '亲，中文保存为cntext.txt，title.txt;其他语种保持：news.txt,newsf等提交哦！')    # 显示对话框
def sendback():
        str1=('python sendfile.py')
        p=os.system(str1)
        return p
# 帮助栏
def description():
        messagebox.showinfo('Description', '1.对于一个文件进行摘要生成\n2.实现手机微信上传和接受摘要\n3.支持多语种功能 ')   # 显示对话框
def about():
        messagebox.showinfo('about', 'version 1\n,本项目由李济阳....同学完成，任何问题可以\n微信： ，邮件反馈')
menubar = tk.Menu(root)
# 语言
def zhongwen():
	str1=('python cntitle.py')
	p=os.system(str1)
	return p
	

def english():
	str1=('python NewsSummary.py')
	p=os.system(str1)
	return p
	
def french():
	str1=('python NewsSummaryfr.py')
	p=os.system(str1)
	return p    

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Upload", command=sendpic)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="feedback", command=sendback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more Language menus
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Chinese", command=zhongwen)
editmenu.add_command(label="English", command=hello)
editmenu.add_command(label="French", command=hello)
menubar.add_cascade(label="Languages", menu=editmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Description", command=description)
menubar.add_cascade(label="Help", menu=helpmenu)



# display the menu
root.config(menu=menubar)
root.mainloop()