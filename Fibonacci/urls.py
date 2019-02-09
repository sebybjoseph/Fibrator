from . import views
from django.urls import path

app_name = 'Fibonacci'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_result/', views.get_result, name="get_result"),
    path('clear_cache/', views.clear_cache, name="clear_cache"),
]
