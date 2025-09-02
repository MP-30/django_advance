from django.urls import path
from home.views import index, contact, dynamic_route, about

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('about/',about),
    path('dynamic_route/<int:number>',dynamic_route),
]
