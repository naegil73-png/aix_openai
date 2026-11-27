from django.urls import path,include
from ..board2 import views

app_name = 'board2'
urlpatterns = [
    path('blist/', views.blist,name='blist'),
    path('blist2/', views.blist2,name='blist2'),
]
