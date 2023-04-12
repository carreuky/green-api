from django.urls import path
from herbal.views import herbal_list

urlpatterns = [
    path('list',herbal_list.as_view)
]
