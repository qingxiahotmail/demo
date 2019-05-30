import itchat, time
import requests  # 库文件
from itchat.content import *
def sendfile():
    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    itchat.send_file('output.txt','filehelper')

	
if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=True)
    sendfile

