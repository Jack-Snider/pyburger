from django.http import HttpResponse
from django.shortcuts import render # render 함수를 import

def main( request ):
    return render( request, "main.html" ) # HttpResponse 대신 render 함수 사용

def burger_list( request ):
    return render( request, "burger_list.html" ) # HttpResponse 대신 render 함수 사용