import sys
import socket
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from client_ui import Ui_Form
from PyQt5.QtGui import QIntValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp,QThread,pyqtSignal
import Aes
import time

class ListenThread(QThread):
    signal = pyqtSignal(str)
    def __init__(self,Sock):
        super(ListenThread,self).__init__()
        self.socketReceiver=Sock
        self.message0=''
        self.time0=0

    def run(self):
        while True:
            data, address = self.socketReceiver.recvfrom(65535)
            #try:
            if data!="":
                
                data=data.decode("utf-8")
                data=eval(data)
                if data['data']!=self.message0 or (time.time()-self.time0>1):
                    self.signal.emit(str(data))
                self.message0=data['data']
            self.time0=time.time()
            #except:
                #pass
        pass



class TestGUI(Ui_Form):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        

        ipValidator = QRegExpValidator(QRegExp('^((2[0-4]\d|25[0-5]|\d?\d|1\d{2})\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'))
        portValidator = QIntValidator(0,65535)
        self.ipAddress.setValidator(ipValidator)
        self.port.setValidator(portValidator)
        self.ipAddress.setPlaceholderText("请输入ip地址")
        self.port.setPlaceholderText("端口")

        self.connectButton.clicked.connect(self.connect_server)
        self.sendButton.clicked.connect(self.send_data)
        self.sendCodecButton.clicked.connect(self.send_codec_data)
        self.jiami.clicked.connect(self.Encode)
        self.jiemi.clicked.connect(self.Decode)
        self.qingchu.clicked.connect(self.Clear)

        self.TCPSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


        self.socketReceiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socketReceiver.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        PORT = 9993
        self.socketReceiver.bind(('', PORT))
        self.message0=''
        self.time0=0

    def connect_server(self):
        try:
            ip = self.ipAddress.text()
            port = int(self.port.text())
            addr=(ip,port)
            self.TCPSock.connect(addr)

            self.connectButton.setDisabled(True)

            self.thread1 = ListenThread(self.socketReceiver)
            self.thread1.signal.connect(self.message_receive)
            self.thread1.start()
            self.thread1.exec()

        except:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '连接服务器失败，检查ip地址！')
            msg_box.exec_()
        pass

    def message_receive(self,message):
        message=eval(message)
        self.textBrowser.append(message["nickname"]+":"+message["data"])
        if message["isEncrypt"]==0:
            self.lineEdit.setText(message["data"])
            self.lineEdit_2.setText("")
        if message["isEncrypt"]==1:
            self.lineEdit_2.setText(message["data"])
            self.lineEdit.setText("")

        self.thread1.start()
        self.thread1.exec()

        

    def send_data(self):
        data0={"data":self.message.toPlainText()}   #消息内容
        data0["nickname"]=self.nickName.text()  #昵称
        data0["isEncrypt"]=0    #是否加密
        self.textBrowser.append(data0["nickname"]+":"+data0["data"])
        data0=str(data0)
        data=data0.encode("utf-8")
        self.TCPSock.send(data)
        
        self.message.clear()
        pass
    def send_codec_data(self):
        key = self.key.text()
        if key!="":
            message=self.message.toPlainText()
            e = Aes.encrypt(message,key)
            data0={"data":e}   #消息内容
            data0["nickname"]=self.nickName.text()  #昵称
            data0["isEncrypt"]=1    #是否加密
            data0["data"]=data0["data"].decode("utf-8")
            self.textBrowser.append(data0["nickname"]+":"+data0["data"])
            data0=str(data0)
            data=data0.encode("utf-8")
            self.TCPSock.send(data)
            self.message.clear()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '输入密码')
            msg_box.exec_()
        pass


    def Clear(self):
        self.lineEdit_2.setText("")
        self.lineEdit.setText("")

    def Decode(self):
        if self.lineEdit_2.text() != "":
            key = self.key.text()
            data=self.lineEdit_2.text()
            d = Aes.decrypt(data.encode('utf-8'),key)
            self.lineEdit.setText(d)
        pass

    def Encode(self):
        if self.key.text()!="":
            if self.lineEdit.text()!="":
                key = self.key.text()
                #data=self.messages[-1]["data"]
                data=self.lineEdit.text()
                e = Aes.encrypt(data,key)
                self.lineEdit_2.setText(e.decode("utf-8"))
        else:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '输入密码')
            msg_box.exec_()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = TestGUI(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())