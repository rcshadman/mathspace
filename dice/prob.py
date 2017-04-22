from __future__ import division
import sys,ipdb,numpy
from decimal import Decimal
sys.setrecursionlimit(10000000)
class Probability():
	def __init__(self,sides=0):
		self.isTooBig = False
		if not self.corner_case(sides):
			self._n = sides
			# self.calculate_probability()
			
		else:
			return 'INPUT NOT VALID'
	
	@property
	def n(self,):
		return self._n

	def corner_case(self,sides):
		# ipdb.set_trace()
		if sides > 30L:
			self.isTooBig = True
		if all([sides==None,sides<=0L,sides=='',sides>8800L]):
			return True
		else:
			return False

	def factorial(self,n):
		if n == 0:
			return 1
		else:
			return n * self.factorial(n - 1)

	def expo(self,n,e):
		# ipdb.set_trace()
		res = e**n
		# res = Decimal(int(n))**int(e)
		return res
		

	def calculate_probability(self,adjustment=0):
		precision = 8
		numerator = self.factorial(self.n-1)
		denomenator = self.expo(self.n,self.n-1) 
		
		if not self.isTooBig:
			result = (numerator/denomenator)
			return format(result,'.90f')
		else:
			de = len(str(denomenator))-precision
			nu = len(str(numerator))-precision
			normalize_factor = de if nu > de else nu
			try:
				numerator = round(numerator/10**(normalize_factor))
			except:
				numerator = float(str(numerator)[:-normalize_factor])
			
			if self.n <= 900L:
				adjustment = int(self.n/10)
			elif self.n >= 900L and self.n < 1290L:
				adjustment = int(self.n/10 *2 )
			elif self.n >= 1290L and self.n <= 2200L:
				adjustment = int(self.n/10 *3 )
			elif self.n >= 2200L and self.n <= 8800L:
				adjustment = int(self.n/10 *4 )


			normalize_factor +=adjustment
			try:
				denomenator = denomenator / 10**(normalize_factor)
			except:
				denomenator = long(str(denomenator)[:-normalize_factor])
			
			try:
				result = (numerator/denomenator)
			except:
				return float(0)

			# ipdb.set_trace()
			return result


# def cal(n):
# 	obj = Probability(n)
# 	res = obj.calculate_probability()
# 	print 'number : {}      -------        result : {}'.format(n,res)

# if __name__ == '__main__':
# 	n = long(raw_input('enter range \n'))
# 	map(cal,[i for i in range(8800,n+1)])




