import itchat, time
import requests  # 库文件
#import os
from itchat.content import *
from aip import AipOcr
import re



@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])
    with open('temp.png' ,'wb') as f:
      f1=open (msg.fileName, 'rb')
      f.write(f1.read())
      f1.close()
    f = open('ocr.txt', 'w')
    f.close() 
    ocrtxt()
    f2=open('ocr1.txt','a')
    f = open ('ocr.txt','r')
    f2.write(f.read())#ocr1.txt保存识别后的资料
    f2.close()
    f.close()
    itchat.send_file('ocr.txt','filehelper')#发送回手机当下识别的文本内容
    with open('cntext.txt','w') as f2:
      f = open ('ocr1.txt','r')
      f2.write(f.read())#ocr1.txt写入中文保存为cntext.txt，其他语种保持：news.txt
      f.close()
    with open('title.txt' ,'w') as f:
      f.write(" ")
    return '%s received' % msg['Type']


def ocrtxt():
    APP_ID='16303087'
    API_KEY ='UYXyertIkA14rItyRoA9ua6x'
    SECRECT_KEY='kyZEtPXdHcjLVxXUvTC9cgOw8BAdb77o'
    client=AipOcr(APP_ID,API_KEY,SECRECT_KEY)
    i=open(r'temp.png','rb')
    img=i.read()
    message=client.basicGeneral(img)
    output=open('ocr.txt','a')
    for i in message.get('words_result'):
         print(i.get('words'))
         print(i.get('words').strip(),file=output)
    output.close()
    return



itchat.auto_login(enableCmdQR=True)
itchat.run(True)      



