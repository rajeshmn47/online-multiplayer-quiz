from django.urls import path,include
from quiz.views import *

urlpatterns = [
    path('',home,name='homequiz'),
    path('register/',register,name='register'),
    path('login/',loginform,name='login'),
    path('add/',addquestion,name='login'),
    path('logout/',logoutin,name='logout'),

]
