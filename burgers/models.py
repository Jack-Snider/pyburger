"""
Django에서 models.py파일은 spring에서 vo와 같은 역할을 한다고 보면 됨

여기서 하나의 클래스( 모델 )가 vo와 같은 의미이며 하나의 DB 테이블과 같다고 생각하면 된다.

"""
from django.db import models # Django가 가진 모듈 가져오기

# Create your models here.

class Burger( models.Model ): # 햄버거를 나타내는 Model 클래스 정의 시작

    name = models.CharField( max_length = 20 ) # 문자열을 저장하는 CharField
    price = models.IntegerField( default = 0 ) # 숫자를 저장하는 IntegerField
    calories = models.IntegerField( default = 0 )  # 숫자를 저장하는 IntegerField