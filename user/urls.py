from django.urls import path

from user.views import *

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
]