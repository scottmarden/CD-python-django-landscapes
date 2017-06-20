# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'landscape_app/index.html')

def landscape(request, num):
	print num
	if int(num) <= 50:
		print "less than 50"
		if int(num) >= 1 and int(num)<= 10:
			print "snow"
			loc = "snow"
			alt = "A snowy landscape"
		elif int(num) >= 11 and int(num)<= 20:
			print "desert"
			loc = "desert"
			alt = "A desert landscape"
		elif int(num) >= 21 and int(num)<= 30:
			print "forest"
			loc = "forest"
			alt = "A forest landscape"
		elif int(num) >= 31 and int(num)<= 40:
			print "vineyard"
			loc = "vineyard"
			alt = "A landscape featuring a vineyard"
		elif int(num) >= 41 and int(num)<= 50:
			print "tropical"
			loc = "tropical"
			alt = "A tropical landscape"
		context = {
			'num': num,
			'landscape': loc,
			'alt_tag': alt
		}
		return render(request, 'landscape_app/landscape.html', context)
	else:
		return redirect('/')


def invalid(request):
	return redirect('/')
