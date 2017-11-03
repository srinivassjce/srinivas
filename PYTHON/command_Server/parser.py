#!/user/bin/python


class Parser() :
	def __init__(self,output) :
		self.output=output.split()
		
	def check_message(self) :
		print self.output
		print self.output[0],self.output[1::] 
		return (self.output[0] ,self.output[1::] )


	def check_message(self) :
		print self.output
		
