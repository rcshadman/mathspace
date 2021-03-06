""" 
please  read comments for complete derivation
P(E) = (n-1)! / n^n-1

"""

from __future__ import division
import sys,ipdb
from decimal import Decimal
sys.setrecursionlimit(10000000)
class Probability():
	def __init__(self,sides=0):
		self.isTooBig = False
		if not self.corner_case(sides):
			self._n = sides

		else:
			return 'INPUT NOT VALID'
	
	@property
	def n(self,):
		return self._n

	def corner_case(self,sides):
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
		res = n**e
		return res
		
	def adjust(self,):
		if self.n <= 900L:
			return int(self.n/10)
		elif self.n >= 900L and self.n < 1290L:
			return int(self.n/10 *2 )
		elif self.n >= 1290L and self.n <= 2200L:
			return int(self.n/10 *3 )
		elif self.n >= 2200L and self.n <= 8800L:
			return int(self.n/10 *4 )

	def calculate_probability(self,adjustment=0):
		precision = 8
		numerator = self.factorial(self.n-1)
		denominator = self.expo(self.n,self.n-1) 
		
		if not self.isTooBig:
			result = (numerator/denominator)
			# ipdb.set_trace()
			return format(result,'.90f')
		else:
			normalize_factor = len(str(numerator))-precision
			
			try:
				numerator = round(numerator/10**(normalize_factor))
			except:
				# cheap hack to get around datatype limitation
				numerator = float(str(numerator)[:-normalize_factor])
			
			# stronger truncation of digits from denominator
			adjustment = self.adjust()
			normalize_factor +=adjustment
			
			try:
				denominator = denominator / 10**(normalize_factor)
			except:
				# cheap hack to get around datatype limitation
				denominator = long(str(denominator)[:-normalize_factor])
			
			try:
				result = (numerator/denominator)
			except:
				return float(0)

			return result


