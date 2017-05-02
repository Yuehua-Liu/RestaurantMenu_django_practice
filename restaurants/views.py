#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response

def menu(request):
	food1 = {'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
	food2 = {'name':'蒜泥白肉','price':90,'comment':'推薦!','is_spicy':True}
	foods = [food1,food2]

	return render_to_response('menu.html',locals())