from django.urls import path
from django.contrib import admin
from herbal.views import *

urlpatterns = [
    path('list/',herbal_list.as_view()),
    path('create/',herbal_create.as_view()),
    path('each/<int:pk>/',herbal_each.as_view())
]
