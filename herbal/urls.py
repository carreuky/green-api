from django.urls import path
from django.contrib import admin
from herbal.views import herbal_list, HerbalCreate

urlpatterns = [
    path('list/',herbal_list.as_view()),
    path('create/',HerbalCreate.as_view())
]
