import socket

from home import Ui_MainWindow
from home import Room
# from table import Ui_Table
from user import user
# from createRoom import Ui_createRoom

# while True:
# 	print(s.recv(1024).decode())

class client():
	"""docstring for client""" 
	def __init__(self):
		sk = socket.socket()
		port = 9797
		# i = socket.gethostbyname('tcp://4.tcp.ngrok.io:19374')
		# sk.connect(("26.221.173.150",port))
		sk.connect(("26.94.35.175",port))
		u = user(sk)
		name = input("nhap ten cua ban:")
		u.sendMsg("login,"+name)
		while(u.recvMsg() != "legal"):
			name = input("nhap ten cua ban:")
			u.sendMsg("login,"+name)
		u.setName(name)
		import sys
		from PyQt5 import QtWidgets
		app = QtWidgets.QApplication(sys.argv)
		self.UI_home = Ui_MainWindow(u)
		sys.exit(app.exec_())

	


if __name__=="__main__":
	client()

		