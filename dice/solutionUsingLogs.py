"""
please  read comments for complete derivation

P(E) = (n-1)! / n^n-1

log(p) = -nlog(n) + log(n) + log(n-1) + log(n-2) + log(n-3) + log(n-4) + log(n-5) ..... log(1)

log(p) = (sum of series)

p = 10^(sum of series)


variable declarations:

sum of series = exponential_part + actorial_part

factorial_part = log(n) + log(n-1) + log(n-2) + log(n-3) + log(n-4) + log(n-5) ..... log(1)

exponential_part = (n-1)!

"""

import math

def probability(n):

	exponential_part = -n*math.log10(n)
	
	factorial_part = reduce(lambda x,y: x+y,[float(math.log10(each)) for each in range(1,n)])
	
	sum_of_series = exponential_part + factorial_part
	
	"""
	Admustment technique:
	compilor works well till n = 736 , so we make that as a base value and convert all the values 
	bigger than n > 736 in terms of the base value.
	ie probability = multiple * baseValue + fraction
	"""

	# side = 736
	base = -320.67503848095225
	baseValue = pow(10,base)

	if sum_of_series < base:
		
		multiple = int(sum_of_series/base)
		
		fraction = sum_of_series - int(sum_of_series/base)
		
		fractionValue = pow(10,fraction)
		
		return '{} X {} + {}'.format(multiple,baseValue,fraction)
	
	else:
		
		return str(pow(10,sum_of_series))

