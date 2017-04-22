from __future__ import division
from . import prob
from django.shortcuts import render
import ipdb


def dice(request):
	title = "DICE PROBABILITY CALCULATOR"
	if request.method == 'GET':
		context = { "title":title }
		return render(request, "index.html",context)
	
	if request.method == 'POST':
		sides = long(request.POST['sides'])
		try:
			probability = prob.Probability(sides=sides)
			res = str(probability.calculate_probability())
			context = { "result" : res, "title":title}
			return render(request, "index.html", context)

		except Exception as e:
			context = {error : "index"}
			return render(request, "index.html", context)