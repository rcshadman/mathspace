import math

def probability(n):

	exponential_part = -n*math.log10(n)
	
	factorial_part = reduce(lambda x,y: x+y,[float(math.log10(each)) for each in range(1,n)])
	
	sum = exponential_part + factorial_part
	
	"""
	Admustment technique
	compilor works well till n = 736 , so we make that as a base value and convert all the values 
	bigger than n > 736 in terms of the base value.
	ie probability = multiple * baseValue + fraction
	"""
	
	# n = 736
	base = -320.67503848095225
	baseValue = pow(10,base)

	if sum < base:
		multiple = int(sum/base)
		fraction = sum - int(sum/base)
		fractionValue = pow(10,fraction)
		return '{} X {} + {}'.format(multiple,baseValue,fraction)
	else:
		return str(pow(10,sum))

if __name__ == '__main__':
	n = int(raw_input("enter \n"))
	res = probability(n)
	print res