from __future__ import division
from django.http import JsonResponse
from . import prob
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
import ipdb


def dice(request):
	if request.method == 'GET':
		context = { "title":"DICE ROLLER"}
		return render(request, "index.html",context)
	
	if request.method == 'POST':
		# ipdb.set_trace()
		sides = long(request.POST['sides'])
		probability = prob.Probability(sides=sides)
		res = str(probability.calculate_probability())
		context = { "result" : res,"title":"DICE ROLLER"}
		return render(request, "index.html", context)