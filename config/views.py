"""
Django에서 views.py파일은 비지니스 로직이라고 생각하면 됨.
"""

from django.http import HttpResponse
from django.shortcuts import render # render 함수를 import
from burgers.models import Burger

def main( request ):
    return render( request, "main.html" ) # HttpResponse 대신 render 함수 사용

def burger_list( request ):
    burgers = Burger.objects.all()
    print( 'All burger list : ', burgers )
    return render( request, "burger_list.html" )