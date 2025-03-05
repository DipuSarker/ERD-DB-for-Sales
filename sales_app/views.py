from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Customer, Category, Product, Invoice, InvoiceProduct, User
from django.core.serializers import serialize
from django.db.models import Avg, Max, Min, Sum, Count, Q

def home(request):
    return HttpResponse('Hello django')

def setSessionData(request):
    request.session['username'] = 'Dipu'
    request.session['user_id'] = '382'
    return HttpResponse('Session data set successfully')


def getSessionData(request):
    username = request.session.get('username', 'Default')
    user_id = request.session.get('user_id', '0')
    return HttpResponse(f'Username: {username} and User ID: {user_id}')

def clearSessionData(request):
    if 'username' in request.session:
        del request.session['username']
    return HttpResponse('Session username cleared successfully')


def allSessionData(request):
    request.session.flush()
    return HttpResponse('All session data cleared successfully')
    
