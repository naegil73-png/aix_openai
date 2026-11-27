from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
    path('',views.blist,name='index'),
    path('blist/',views.blist,name='blist'),
    path('blist2/',views.blist2,name='blist2'),
]