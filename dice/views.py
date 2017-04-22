from __future__ import division
from . import prob
from django.shortcuts import render
import ipdb


def dice(request):
	if request.method == 'GET':
		context = { "title":"DICE ROLLER"}
		return render(request, "index.html",context)
	
	if request.method == 'POST':
		sides = long(request.POST['sides'])
		probability = prob.Probability(sides=sides)
		res = str(probability.calculate_probability())
		context = { "result" : res,"title":"DICE ROLLER"}
		return render(request, "index.html", context)