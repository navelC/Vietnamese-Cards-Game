class user:
	def __init__(self,socket):
		# self.socket = socket
		self.cards = []
		self.socket = socket
		self.read = self.socket.makefile(encoding = 'utf-8',newline='\n')
		self.write = self.socket.makefile('w',encoding = 'utf-8',newline='\n')
		self.name = "abc"
		
	def sendMsg(self,msg):
		self.write.write(msg+"\n")
		self.write.flush()	

	def getIn4User(self):
		return self.name

	def setSkip(self,b):
		self.skip = b

	def setName(self,name):
		self.name = name

	def recvMsg(self):
		msg = self.read.readline().strip()
		print(msg)
		return msg

	def setThread(self,thread):
		self.thread = thread

	def addCard(self,card):
		self.cards.append(card)

	def removeCards(self,cards):
		for x in cards:
			self.cards.remove(x)
			

