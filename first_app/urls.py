from django.urls import path 
# There is three way to import a file 
"""  
----------1st one ---------- 
   from first_app.views import home 
------------2nd  one ------------
 from first_app import views
"""
# 3rd one 
from . import views

urlpatterns = [
    path('',views.home),
]