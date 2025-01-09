# URLs
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('users/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
]
#git pull example


#git pull example

# git remote add origin https://github.com/baukamobile/DRF-AUTh.git