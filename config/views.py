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

    # Template으로 전달해줄 dict 객체
    context = {
        "burgers" : burgers, # burgers 키에 burgers 변수( QuerySet 객체 )를 전달한다.
    }

    # render 함수의 마지막에 context 전달
    return render( request, "burger_list.html", context ) # render함수의 3번째 인수는 Template에 전달해줄 사전( dict )객체여야 한다. ( 2번째는 html파일 )


def burger_search( request ):

    print( request.GET ) # request.GET으로 전달된 데이터를 출력

    # request.GET에서 "keyword" 키의 값을 가져와 출력
    keyword = request.GET.get( "keyword" )
    print( keyword )


    """
    objects에서 호출한 filter 함수는 조건과 일치하는 객체를 모두 돌려준다. 함수 호출에 사용한 인수인
    name__contains = keyword는 name 속성이 keyword 변수의 값( 위 경우에는 '더블' )을 포함하는 경우를 말한다.    
    """

    # keyword 값이 주어진 경우
    if keyword is not None:
        # keyword 값으로 검색된 QuerySet 할당
        # 이름( name 속성 )에 전달받은 키워드 값이 포함된 burger를 검색한다.
        burgers = Burger.objects.filter(name__contains=keyword)

    # 주소표시줄을 통해 keyword가 주어지지 않아, None이 할당된 경우
    else:
        # 검색 결과가 없는 것과 같은 빈 QuerySet을 할당
        burgers = Burger.objects.none()


    context = {
        "burgers" : burgers,
    }

    return render( request, "burger_search.html", context )