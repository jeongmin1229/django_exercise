from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index1),
    path('index2/', views.index2),
    path('insert/', views.insert),
    path('show/', views.show)
]
