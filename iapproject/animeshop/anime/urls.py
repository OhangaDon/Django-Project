from django.urls import path
from . import views

urlpatterns = [
    path('anime/',views.anime,name='anime'),
    path('anime/login/',views.login,name='login'),
    path('anime/shop/',views.shop,name='shop'),
]