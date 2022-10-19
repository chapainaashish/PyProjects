# Author: Daniela Grothe
# GitHub: https://github.com/DGrothe-PhD

# Replace blanks in a text with an asterisk, replace words of the text with blanks
# to create a (pseudo-)random snow pattern

class Scatter:
	__piece = ["*"]
	__textsample = ""
	__lineslist = []
	def __init__(self, tx):
		self.__textsample = tx
	def SetTextSample(self, tx):
		self.__textsample = tx
	
	#choose your own symbol or string to be scattered
	def SetPrintableObject(self, p):
		self.__piece.append(p)
	def ClearPrintableObjects(self):
		self.__piece = []
	
	# Split (roughly all of) the text in portions (lines) of linelength (integer) characters
	# note: TextCarpet ignores the last len(text) modulo linelength characters.
	# For splitting readable text, use SplitToShort instead.
	def TextCarpet(self, linelength):
		self.__lineslist = []
		for i in range(0,len(self.__textsample)//linelength):
			self.__lineslist.append(self.__textsample[i*linelength:(i+1)*linelength])

	def SplitToShort(self, tx, linelength):
		self.__lineslist = []
		for i in range(0,len(__textsample)//linelength):
			self.__lineslist.append(self.__textsample[i*linelength:(i+1)*linelength])
		self.__lineslist.append(self.__textsample[(i+1)*linelength+1:len(tx)])
		return self.__lineslist
	# 
	def scatter(self):
		foo = []
		i=0
		if len(self.__lineslist)<2:
			pass#return "Too low number of lines or text too short."
		for x in self.__lineslist:
			if i<100: # don't generate too large output
				buf= x.split()
				a = ""
				k = len(self.__piece)
				for j in range(0,len(buf)):
					a+= (" "*len(buf[j]))
					a+=self.__piece[j%k]
				foo.append(a)
			i+=1
		print("\n".join(foo))
