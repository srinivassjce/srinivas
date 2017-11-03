#!/usr/bin/python


class lcmGcd ()  :
	def __init__(self,num1,num2) :
		self.num1=num1
		self.num2=num2

	def gcd(self) :

		#print self.num1,self.num2

		if (self.num1 > self.num2 ) :
			rem=self.num1%self.num2 
		#	print rem
			if rem != 0 :
				self.num1 = self.num2 
				self.num2 = rem
				self.gcd ()
			else :
				return self.num2


		elif (self.num2 > self.num1 ) :
                        rem=self.num2%self.num1 

                        if rem != 0 :
                                self.num2 =self.num1
				self.num1=rem
                                self.gcd()
                        else :
                                return self.num1


	def lcm(self,n1,n2) :
			 a= self.gcd()	
			 return (n1 * n2) / a
				
	



if __name__ == '__main__' :
	l=lcmGcd(50,1222)
	
print 	l.gcd() 
	


	

