from __future__ import division
from . import prob, solutionUsingLogs
from django.shortcuts import render
import ipdb


def dice(request):
	title = "DICE PROBABILITY CALCULATOR"
	res = ""
	if request.method == 'GET':
		context = { "title":title }
		return render(request, "index.html",context)
	
	if request.method == 'POST':
		sides = long(request.POST['sides'])
		try:
			# different algorithm for different range
			if sides <= 8800:
				probability = prob.Probability(sides=sides)
				res = 'Solution using denominator truncation : ' + str(probability.calculate_probability())
			elif sides >8800 and sides < 999999999:
				print res
				res =  'Solution using Logs : ' + solutionUsingLogs.probability(sides)
			
			else:
				pass
			context = { "result" : res, "title":title}
			return render(request, "index.html", context)


		except Exception as e:
			context = {error : "index"}
			return render(request, "index.html", context)