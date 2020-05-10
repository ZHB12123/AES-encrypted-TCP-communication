import sys
import socket
import threading
from PyQt5.QtCore import QRegExp,QThread,pyqtSignal
from PyQt5.QtGui import QIntValidator,QRegExpValidator
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from server_ui import Ui_Form
import Aes

class ListenThread(QThread):
    signal = pyqtSignal(bytes)
    def __init__(self,Sock):
        super(ListenThread,self).__init__()
        self.TCPSock=Sock
     

    def run(self):
        (connection,c_addr)=self.TCPSock.accept()
        
        while True:
            data=connection.recv(1024)
            if data!="":
                self.signal.emit(data)
        pass


class TestGUI(Ui_Form):

    def __init__(self, MainWindow):
        """
        初始化界面 ，连接槽函数，以及设置校验器
        """
        self.setupUi(MainWindow)
        
        ipValidator = QRegExpValidator(QRegExp('^((2[0-4]\d|25[0-5]|\d?\d|1\d{2})\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'))
        portValidator = QIntValidator(0,65535)
        self.ipAddress.setValidator(ipValidator)
        self.port.setValidator(portValidator)
        self.ipAddress.setPlaceholderText("请输入ip地址")
        self.port.setPlaceholderText("端口")

        self.pushButton.clicked.connect(self.start_tcp_server)
        self.sendButton.clicked.connect(self.send_text)
        self.buttonEncode.clicked.connect(self.Encode)
        self.buttonDecode.clicked.connect(self.Decode)
        self.buttonClear.clicked.connect(self.Clear)
        self.sendButton.clicked.connect(self.send_text)

        self.TCPSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection=""
        self.c_addr=""
        self.messages=[]
        self.is_send_encrypt=0

    def start_tcp_server(self):
        try:
            ip = self.ipAddress.text()
            port = int(self.port.text())
            addr=(ip,port)
            self.TCPSock.bind(addr)
            self.TCPSock.listen(5)#参数为允许的连接数



            self.thread1 = ListenThread(self.TCPSock)
            self.thread1.signal.connect(self.message_receive)
            self.thread1.start()
            self.pushButton.setDisabled(True)
            #self.thread1.quit()
            self.thread1.exec()
        except:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '服务器建立失败，检查ip地址！')
            msg_box.exec_()

    def send_text(self):
        data={}
        data['data']=self.textCodec.toPlainText()
        data['nickname']=self.name.text()
        data['isEncrypt']=self.is_send_encrypt

        data=str(data).encode("utf-8")
        sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        PORT = 9993
        network = '<broadcast>'
        sender.sendto(data, (network, PORT))

        self.is_send_encrypt=0
        pass

    def message_receive(self,message):
        try:
            message=message.decode("utf-8")
            
            message=eval(message)
            if message["isEncrypt"]==0:
                self.plainText.setText(message["data"])
                self.cipherText.setText("")
            if message["isEncrypt"]==1:
                self.cipherText.setText(message["data"])
                self.plainText.setText("")

            self.messages.append(message)
            
            self.textFromClient.append(message["nickname"]+':'+message["data"])
            self.thread1.start()
            self.thread1.exec()
        except:
            pass
        pass

    def Clear(self):
        self.cipherText.setText("")
        self.plainText.setText("")

    def Decode(self):
        if self.cipherText.text() != "":
            key = self.password.text()
            data=self.cipherText.text()
            
            d = Aes.decrypt(data.encode('utf-8'),key)
            self.plainText.setText(d)
        pass

    def Encode(self):
        if self.password.text()!="":
            if self.plainText.text()!="":
                key = self.password.text()
                #data=self.messages[-1]["data"]
                data=self.plainText.text()
                e = Aes.encrypt(data,key)
                self.cipherText.setText(e.decode("utf-8"))
            if self.textCodec.toPlainText()!="":
                key = self.password.text()
                #data=self.messages[-1]["data"]
                data=self.textCodec.toPlainText()
                e = Aes.encrypt(data,key)
                self.textCodec.setText(e.decode("utf-8"))
                self.is_send_encrypt=1
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