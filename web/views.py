# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            print(200)
            return JsonResponse({'msg': 'hello '+username}, status=200)
        else:
            print(403)
            return JsonResponse({'msg': 'not allowed'}, status=403)

