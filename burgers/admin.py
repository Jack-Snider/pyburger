from django.contrib import admin
from burgers.models import Burger

# Register your models here.

@admin.register( Burger )
class BurgerAdmin( admin.ModelAdmin ): # burgers앱에 관한 관리자
    pass
